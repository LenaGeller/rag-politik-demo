import yaml
from pathlib import Path
def load_keyword_map(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

from config import BASE_DIR

keyword_map = load_keyword_map(BASE_DIR / "knowledge_base" / "query_normalization.yaml"
)

# --------------------------------------------------
# 2) Query normalisieren
# --------------------------------------------------

def normalize_query(question: str, keyword_map: dict) -> dict:
    q = question.lower()

    result = {
        "party": None,
        "parties": [],
        "government": False,
        "document_expectation": None,
        "comparison": False
    } 

    # --- Vergleich ---
    for kw in keyword_map.get("comparison", []):
        if kw.lower() in q:
            result["comparison"] = True
            break

    # --- Parteien ---
    parties_map = keyword_map.get("parties", {})
    found_parties = []

    for party, keywords in parties_map.items():
        for kw in keywords:
            if kw.lower() in q:
                found_parties.append(party.lower())
                break

    if len(found_parties) == 1:
        result["party"] = found_parties[0]
        result["parties"] = found_parties
        result["government"] = False

    elif len(found_parties) > 1:
        result["party"] = None
        result["parties"] = found_parties
        result["government"] = False

    # --- Regierung ---
    for kw in keyword_map.get("government", []):
        if kw.lower() in q:
            result["government"] = True
            result["party"] = None
            break

    # --- Dokument-Erwartung ---
    doc_exp = keyword_map.get("document_expectations", {})
    for doc_type, keywords in doc_exp.items():
        for kw in keywords:
            if kw.lower() in q:
                result["document_expectation"] = doc_type
                break
        if result["document_expectation"]:
            break

    return result

# --------------------------------------------------
# 3) Retrieval-Constraints bauen
# --------------------------------------------------


def build_retrieval_constraints(signals: dict) -> dict:
    filters = []

    party = signals.get("party")
    parties = signals.get("parties", [])
    government = signals.get("government")
    doc_exp = signals.get("document_expectation")
    comparison = signals.get("comparison")

    # -------------------------
    # Sonderfall: Vergleich Regierung vs. Programme
    # -------------------------
    if comparison and government is True and doc_exp == "programm":
        return {
            "filters": {
                "$or": [
                    {"government": {"$eq": True}},
                    {
                        "$and": [
                            {"government": {"$eq": False}},
                            {"dokument_typ": {"$eq": "programm"}}
                        ]
                    }
                ]
            }
        }

    # Partei-Frage → Regierung ausschließen
    if (party or len(parties) > 0) and government is not True:
        filters.append({"government": {"$eq": False}})

    if government is True:
        filters.append({"government": {"$eq": True}})

    if comparison:
  
        pass
    
    # Einzelpartei
    if party and not comparison:
        filters.append({"partei": {"$eq": party}})

    # Vergleich mehrerer Parteien
    if len(parties) >= 2:
        filters.append({"partei": {"$in": parties}})
        filters.append({"government": {"$eq": False}})

    # --- Vertrag ---
    if doc_exp == "vertrag":
        filters.append({"dokument_typ": {"$eq": "vertrag"}})
        filters.append({"government": {"$eq": True}})

    # --- Programm ---
    elif doc_exp == "programm":
        filters.append({"dokument_typ": {"$eq": "programm"}})
        filters.append({"government": {"$eq": False}})
        if party:
            filters.append({"partei": {"$eq": party}})

    # --- Beschluss ---
    elif doc_exp == "beschluss":
        filters.append({
            "$or": [
                {"dokument_typ": {"$eq": "beschluesse"}},
                {"dokument_typ": {"$eq": "beschluss"}}
            ]
        })

        if party:
            filters.append({"government": {"$eq": False}})
            filters.append({"partei": {"$eq": party}})
        else:
            filters.append({"government": {"$eq": True}})

    # -------------------------
    # Vergleichsfall: Partei + Dokumenttyp kombiniert oder nur Parteien
    # -------------------------
    if comparison and party and doc_exp:
        filters.append({"partei": {"$eq": party}})
        filters.append({"dokument_typ": {"$eq": doc_exp}})

    if comparison and len(parties) >= 2 and not doc_exp:
        filters.append({"dokument_typ": {"$eq": "programm"}})    

    # -------------------------
    # WHERE bauen
    # -------------------------
    if not filters:
        where = None
    elif len(filters) == 1:
        where = filters[0]
    else:
        where = {"$and": filters}

    return {
        "filters": where,
        "bias": {}
    }
