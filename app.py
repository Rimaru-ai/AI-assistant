# import streamlit as st
# from models import load_llm, load_embeddings
# from tools import sales_forecast_tool, pdf_search_tool

# # Load models
# llm = load_llm()
# embeddings = load_embeddings()

# st.title("InsightForge AI - Free/Pro Mode Demo")

# # File upload
# sales_file = st.file_uploader("Upload Sales CSV", type="csv")

# # Run sales forecast
# if sales_file:
#     st.write("### Sales Forecast")
#     forecast = sales_forecast_tool(sales_file)
#     st.success(forecast)

# # Simple Q&A demo
# st.write("### Ask a Question")
# query = st.text_input("Type your question here")

# if query:
#     if callable(llm):  # Local pipeline
#         answer = llm(query, max_length=200)[0]['generated_text']
#     else:  # OpenAI LLM
#         answer = llm.invoke(query).content
#     st.write("**Answer:**", answer)


import streamlit as st

# ------------------------------
# Page Setup
# ------------------------------
st.set_page_config(page_title="InsightForge AI", layout="wide")
st.title("📊 InsightForge AI")
st.write("An AI-powered business analytics assistant.")

# ------------------------------
# Safe Startup Wrapper
# ------------------------------
try:
    import config
    import models
    import tools
    import pandas as pd

    st.success("✅ App loaded successfully! You can now use the features below.")

    # --------------------------
    # Sales Data Upload + Preview
    # --------------------------
    st.header("Upload Sales Data")
    uploaded_csv = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_csv:
        try:
            df = pd.read_csv(uploaded_csv)
            st.write("Preview of uploaded data:")
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"Error reading CSV: {e}")

    # --------------------------
    # PDF Upload + Preview
    # --------------------------
    st.header("Upload Research Papers (PDFs)")
    uploaded_pdfs = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

    if uploaded_pdfs:
        st.write(f"Uploaded {len(uploaded_pdfs)} PDF(s).")
        # You can later process them via tools.py

    # --------------------------
    # Free/Pro Mode Info
    # --------------------------
    st.sidebar.header("⚙️ App Settings")
    st.sidebar.write(f"**Pro Mode Enabled:** {config.USE_PRO_MODE}")
    if config.USE_PRO_MODE:
        st.sidebar.info("🔑 Make sure to set your OPENAI_API_KEY in Streamlit Secrets.")
    else:
        st.sidebar.info("🆓 Running in Free Mode (local models).")

except Exception as e:
    st.error(f"🚨 Startup error: {e}")
    st.stop()

# --------------------------
# Q&A / Chat with AI
# --------------------------
st.header("💬 Ask InsightForge AI")

user_query = st.text_input("Type your question:")

if user_query:
    try:
        # Load model
        llm = models.load_llm()

        # Run Free Mode (local Hugging Face) or Pro Mode (OpenAI)
        if config.USE_PRO_MODE:
            response = llm.invoke(user_query)  # OpenAI via LangChain
            answer = response.content
        else:
            response = llm(user_query, max_length=100, num_return_sequences=1)
            answer = response[0]["generated_text"]

        st.subheader("Answer:")
        st.write(answer)

    except Exception as e:
        st.error(f"Error generating response: {e}")


# --------------------------
# Sidebar Settings
# --------------------------
st.sidebar.header("⚙️ App Settings")
st.sidebar.write(f"**Pro Mode Enabled:** {config.USE_PRO_MODE}")

if config.USE_PRO_MODE:
    api_key = st.sidebar.text_input("🔑 Enter OpenAI API Key", type="password")

    if api_key:
        import os
        os.environ["OPENAI_API_KEY"] = api_key
        st.sidebar.success("API key set for this session ✅")
    else:
        st.sidebar.warning("Please enter your OpenAI API key to use Pro Mode.")
else:
    st.sidebar.info("🆓 Running in Free Mode (local/demo models).")


