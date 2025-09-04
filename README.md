# AI-assistant
An AI-powered business analytics application built with Streamlit.
It analyzes sales data and research papers, generates forecasts, and answers natural language queries.

This project demonstrates both a traditional AI application and an upgraded Agentic AI-ready application, with a toggle to switch between Free Mode (local models) and Pro Mode (OpenAI GPT).

#🚀 Features

📊 Sales Data Analysis → Upload CSV files, view trends, KPIs, and forecasts.

📑 Research Paper Insights → Upload PDFs, search and query with AI.

🤖 Free Mode vs Pro Mode Toggle

Free Mode → Runs on local Hugging Face models (no cost).

Pro Mode → Runs on OpenAI GPT models (requires API key).

🧠 Agentic AI Upgrade Ready → Capable of planning, reasoning, and tool use.

# 🛠️ Installation (Local Development)

Clone the repo and install dependencies:

git clone https://github.com/your-username/insightforge-ai.git
cd insightforge-ai
pip install -r requirements.txt


Run locally:

streamlit run app.py

# ⚙️ Configuration

Control the app mode in config.py:

USE_PRO_MODE = False  # Free Mode (local models)
USE_PRO_MODE = True   # Pro Mode (OpenAI GPT)

# 🔹 Free Mode

Uses sentence-transformers and Hugging Face local models.

No API key required.

Slower but cost-free.

# 🔹 Pro Mode

Uses OpenAI GPT models for higher quality results.

Requires setting your API key:

export OPENAI_API_KEY="your_api_key_here"

# ☁️ Deployment on Streamlit Cloud

Push this repo to GitHub.

Go to Streamlit Cloud
 and deploy your repo.

Choose app.py as the main entry point.

If using Pro Mode, set your OpenAI API key in Streamlit Secrets:

Go to App Settings → Secrets

Add:

OPENAI_API_KEY="your_api_key_here"


Your app will be live at:

https://<your-username>-insightforge-ai.streamlit.app

# 📂 Project Structure
├── app.py              # Main Streamlit app
├── config.py           # Mode toggle (Free / Pro)
├── models.py           # LLMs and embeddings setup
├── tools.py            # Sales + PDF helper tools
├── requirements.txt    # Dependencies
└── README.md           # Project documentation

# 📌 Example Workflow

Upload sales_data.csv.

Ask: “Predict next month’s sales trend.”

App forecasts and shows a chart.

Upload research papers (PDFs).

Ask: “Which forecasting model works best for this dataset?”

App queries the papers and suggests methods.

# 🎯 Why This Project

Demonstrates AI + Data Science + Agentic AI concepts in one application.

Built with cost control in mind (Free vs Pro Mode).

Perfect for portfolio/CV visibility.

# 📦 Requirements

See requirements.txt
 for the full list.
Key libraries include:

Streamlit (UI)

Pandas / Numpy / Matplotlib (data analysis)

LangChain + OpenAI (Pro Mode AI)

SentenceTransformers + Hugging Face Transformers (Free Mode AI)

FAISS, PyPDF, PyMuPDF (document embeddings and PDF parsing)

📝 License

This project is released under the MIT License.
