# ranking.py

from typing import List, Dict, Any


def build_ranking_bias(signals: dict) -> dict:
    """
    Erzeugt Gewichtungen für Dokumenttypen abhängig von den erkannten Signalen.
    """

    party = signals.get("party")
    parties = signals.get("parties", [])
    government = signals.get("government")
    comparison = signals.get("comparison")
    doc_exp = signals.get("document_expectation")

    # Regierungsfrage → Beschlüsse / Verträge bevorzugen
    if government:
        return {
            "beschluss": 1.0,
            "vertrag": 0.8
        }

    # Parteifrage oder Vergleich → Programme priorisieren
    if party or (comparison and len(parties) >= 1):
        return {
            "programm": 1.0,
            "beschluesse": 0.6
        }

    # Lose / offene politische Frage
    return {
        "beschluss": 1.0,
        "vertrag": 0.8,
        "programm": 0.5,
        "beschluesse": 0.3
    }


def apply_document_bias(docs: List[Any], signals: dict) -> List[Any]:
    """
    Sortiert Dokumente anhand der durch build_ranking_bias definierten Gewichtung.
    """

    bias = build_ranking_bias(signals)

    def score(doc):
        doc_type = (doc.metadata or {}).get("dokument_typ")
        return bias.get(doc_type, 0.1)

    return sorted(docs, key=score, reverse=True)
