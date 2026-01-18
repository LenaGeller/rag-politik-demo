import streamlit as st
import sys
from pathlib import Path

# src-Ordner importierbar machen
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR / "src"))

from pipeline import frage_stellen

example_questions = [
    "Wie unterscheiden sich AfD und SPD in der Umweltpolitik?",
    "Was plant die Linke im Umweltschutz?",
    "Welche Rolle spielt Migration im Programm der AfD?",
    "Welche Position vertritt die CDU/CSU zur Energiepolitik?",
    "Welche Beschlüsse hat die Bundesregierung zur Klimapolitik gefasst?"
]

st.markdown("### Beispiel-Fragen")

clicked_question = None

for q in example_questions:
    if st.button(q):
        clicked_question = q

# --- Setup ---
st.set_page_config(page_title="RAG Politik", layout="centered")
st.markdown("## Politik-Analyse")
st.markdown(
    "#### RAG-basierte Auswertung von Regierungs- und Parteidokumenten"
)
st.caption(
    "Beantwortet präzise politische Fragen zu Regierung und Parteien (Linke fehlen noch)"
    "ausschließlich auf Basis offizieller Dokumente."
)
# --- Input ---
frage = frage = st.text_input(
    "Deine Frage:",
    value=clicked_question if clicked_question else ""
)



if st.button("Frage stellen"): 
    if not frage.strip(): 
        st.warning("Bitte gib eine Frage ein.") 
    else: 
        with st.spinner("Antwort wird erzeugt …"): 
            antwort, docs = frage_stellen(frage) 
        
        st.markdown("##### Antwort") 
        st.write(antwort)


        st.markdown("### Quellen & Textstellen")

        for i, d in enumerate(docs, start=1):
            meta = d.metadata or {}

            label = (
                f"Quelle {i}: "
                f"{meta.get('partei', 'regierung')} | "
                f"{meta.get('chapter', '?')} | "
                f"{meta.get('titel', '?')}"
            )

            with st.expander(label):
                
                st.markdown("**Original-Textstelle:**")
                st.write(d.page_content)

 
