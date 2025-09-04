import streamlit as st
from models import load_llm, load_embeddings
from tools import sales_forecast_tool, pdf_search_tool

# Load models
llm = load_llm()
embeddings = load_embeddings()

st.title("InsightForge AI - Free/Pro Mode Demo")

# File upload
sales_file = st.file_uploader("Upload Sales CSV", type="csv")

# Run sales forecast
if sales_file:
    st.write("### Sales Forecast")
    forecast = sales_forecast_tool(sales_file)
    st.success(forecast)

# Simple Q&A demo
st.write("### Ask a Question")
query = st.text_input("Type your question here")

if query:
    if callable(llm):  # Local pipeline
        answer = llm(query, max_length=200)[0]['generated_text']
    else:  # OpenAI LLM
        answer = llm.invoke(query).content
    st.write("**Answer:**", answer)
