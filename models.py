# from config import USE_PRO_MODE


# # --- Embeddings ---
# def load_embeddings(langchain_openai=None):
#     if USE_PRO_MODE:
#         from langchain_openai import OpenAIEmbeddings
#         return OpenAIEmbeddings(model="text-embedding-3-small")
#     else:
#         from sentence_transformers import SentenceTransformer
#         return SentenceTransformer("all-MiniLM-L6-v2")


# # --- LLM ---
# def load_llm():
#     if USE_PRO_MODE:
#         from langchain_openai import ChatOpenAI
#         return ChatOpenAI(model="gpt-4o-mini", temperature=0)
#     else:
#         from transformers import pipeline
#         return pipeline("text-generation", model="tiiuae/falcon-7b-instruct")
#         # You can replace with "HuggingFaceH4/zephyr-7b-alpha" or smaller models for speed

# from config import USE_PRO_MODE

# def load_embeddings():
#     if USE_PRO_MODE:
#         from langchain_openai import OpenAIEmbeddings
#         return OpenAIEmbeddings(model="text-embedding-3-small")
#     else:
#         from sentence_transformers import SentenceTransformer
#         # small, fast model for embeddings
#         return SentenceTransformer("all-MiniLM-L6-v2")

# def load_llm():
#     if USE_PRO_MODE:
#         from langchain_openai import ChatOpenAI
#         return ChatOpenAI(model="gpt-4o-mini", temperature=0)
#     else:
#         from transformers import pipeline
#         # Use a tiny model that runs on Streamlit Cloud without memory issues
#         return pipeline("text-generation", model="sshleifer/tiny-gpt2")





# from config import USE_PRO_MODE

# def load_embeddings():
#     if USE_PRO_MODE:
#         from langchain_openai import OpenAIEmbeddings
#         return OpenAIEmbeddings(model="text-embedding-3-small")
#     else:
#         from sentence_transformers import SentenceTransformer
#         # small, fast model for embeddings
#         return SentenceTransformer("all-MiniLM-L6-v2")

# def load_llm():
#     from config import USE_PRO_MODE
#     if USE_PRO_MODE:
#         from langchain_openai import ChatOpenAI
#         return ChatOpenAI(model="gpt-4o-mini", temperature=0)
#     else:
#         from transformers import pipeline
#         # Use a lightweight model with safetensors to avoid torch issues
#         return pipeline("text-generation", model="distilgpt2")




from config import USE_PRO_MODE

def load_embeddings():
    if USE_PRO_MODE:
        from langchain_openai import OpenAIEmbeddings
        return OpenAIEmbeddings(model="text-embedding-3-small")
    else:
        from sentence_transformers import SentenceTransformer
        # small, fast model for embeddings
        return SentenceTransformer("all-MiniLM-L6-v2")


def load_llm():
    from config import USE_PRO_MODE
    if USE_PRO_MODE:
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model="gpt-4o-mini", temperature=0)
    else:
        # Instead of a real LLM, just return a dummy function
        class DummyLLM:
            def __call__(self, prompt, **kwargs):
                return [{"generated_text": f"(Demo Mode) You asked: {prompt}"}]
        return DummyLLM()
