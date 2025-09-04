import pandas as pd


def sales_forecast_tool(file_path):
    df = pd.read_csv(file_path)
    # Dummy forecast logic (replace with ARIMA/ML later)
    forecast = df["Sales"].tail(1).values[0] * 1.05
    return f"Predicted next period sales: {forecast:.2f}"


def pdf_search_tool(query, vector_store):
    docs = vector_store.similarity_search(query, k=3)
    return [doc.page_content for doc in docs]
