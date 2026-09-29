# LegalEase

### AI-Powered Legal Document Generator

LegalEase is an AI-powered application designed to help users generate professional legal documents using artificial intelligence.

## Features

* AI-powered legal document generation
* User-friendly interface
* Document editing
* Export documents as PDF, DOCX, and TXT
* Demo mode for testing

## Technologies Used

* Python
* Streamlit
* FastAPI
* Google Gemini AI
* Python-docx
* ReportLab

## Open LegalEase

**[Click here to open the application](YOUR_RENDER_APP_URL)**

*Replace the placeholder with your deployed Render URL once deployment is complete.*

## Run Locally

1. Clone this repository.

2. Install the dependencies:

   `pip install -r requirements.txt`

3. Create a `.env` file and add your Gemini API key.

4. Start the backend:

   `python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000`

5. Open a second terminal and start the frontend:

   `python -m streamlit run frontend/app.py`

6. Open `http://localhost:8501` in your browser.

## Project Structure

* `backend/` – FastAPI backend and AI integration
* `frontend/` – Streamlit user interface
* `requirements.txt` – Python dependencies
* `.gitignore` – Excludes sensitive and unnecessary files

## Security

API keys and environment variables must be stored locally in `.env` and must never be committed to GitHub.
