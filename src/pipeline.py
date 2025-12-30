
from query import normalize_query, keyword_map, build_retrieval_constraints
from ranking import apply_document_bias
from llm import prompt, model, parser
from retrieval import db

def frage_stellen(frage: str):
    # 1) Query normalisieren & Constraints bauen
    signals = normalize_query(frage, keyword_map)
    constraints = build_retrieval_constraints(signals)

    # 2) Relevante Dokumente holen
    docs = db.similarity_search(
        frage,
        k=20,
        filter=constraints["filters"]
    )
    
    docs = apply_document_bias(docs, signals)

    # 3) Kontext bauen
    context_parts = []
    for d in docs:
        meta = d.metadata or {}
        header = (
            f"[PARTEI: {meta.get('partei','?')} | "
            f"KAPITEL: {meta.get('chapter','?')} | "
            f"JAHR: {meta.get('jahr','?')} | "
            f"QUELLE: {meta.get('source','?')}]"
        )
        context_parts.append(header + "\n" + d.page_content)

    context = "\n\n".join(context_parts)

    # 4) LLM aufrufen
    chain = prompt | model | parser


    antwort = chain.invoke({"context": context, "question": frage})

    
    return antwort, docs
