# config.py
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_DIR = BASE_DIR / "chroma_db"

print("BASE_DIR:", BASE_DIR)
print("Keyword YAML:", BASE_DIR / "knowledge_base" / "query_normalization.yaml")


# Alte Collection (nicht mehr aktiv genutzt)
ALT_COLLECTION = "langchain"

# Aktive Collection (Projektstandard)
NEU_COLLECTION = "politik_normalized_test"

EMBEDDING_MODEL = "text-embedding-3-large"
CHAT_MODEL = "gpt-5-mini"

TOP_K = 20
TEMPERATURE = 0.1


