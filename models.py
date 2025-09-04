from config import USE_PRO_MODE


# --- Embeddings ---
def load_embeddings(langchain_openai=None):
    if USE_PRO_MODE:
        from langchain_openai import OpenAIEmbeddings
        return OpenAIEmbeddings(model="text-embedding-3-small")
    else:
        from sentence_transformers import SentenceTransformer
        return SentenceTransformer("all-MiniLM-L6-v2")


# --- LLM ---
def load_llm():
    if USE_PRO_MODE:
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model="gpt-4o-mini", temperature=0)
    else:
        from transformers import pipeline
        return pipeline("text-generation", model="tiiuae/falcon-7b-instruct")
        # You can replace with "HuggingFaceH4/zephyr-7b-alpha" or smaller models for speed
