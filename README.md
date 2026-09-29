# LegalEase: AI-Powered Legal Document Generator

LegalEase is an AI-powered web application designed to simplify legal document preparation. It uses Google Gemini AI to generate structured legal document drafts based on user-provided information.

The application provides an easy-to-use interface where users can generate, preview, edit, and download documents in multiple formats.

## Problem Statement

Preparing legal documents manually can be time-consuming and challenging, especially for individuals unfamiliar with legal terminology and document formats.

LegalEase aims to simplify this process by using Artificial Intelligence to assist users in generating structured document drafts.

## Objectives

* Simplify legal document preparation.
* Reduce the time required to create document drafts.
* Provide a user-friendly interface.
* Generate editable legal document content.
* Support multiple document download formats.
* Demonstrate the practical application of AI in document generation.

## Key Features

* AI-powered document generation using Google Gemini.
* Simple and interactive Streamlit interface.
* FastAPI backend integration.
* Editable document preview.
* TXT, DOCX, and PDF download support.
* Input validation and error handling.
* Modular project architecture.

## Technologies Used

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python        | Core programming language |
| Streamlit     | Frontend development      |
| FastAPI       | Backend API               |
| Google Gemini | AI document generation    |
| GitHub        | Version control           |
| Pytest        | Automated testing         |

## System Architecture

**User Input → Streamlit Frontend → FastAPI Backend → Google Gemini AI → Generated Document → Preview and Editing → Download**

## Project Structure

```text
LegalEase/
├── backend/
│   ├── ai_core/
│   ├── utils/
│   ├── main.py
│   ├── routes.py
│   ├── schemas.py
│   └── config.py
├── frontend/
│   └── app.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/prabu270/Naan-Mudhalvan.git
```

### 2. Navigate to the Project Directory

```bash
cd Naan-Mudhalvan
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file and add your Gemini API key.

**Security Note:** Never upload your `.env` file or API keys to a public GitHub repository.

## Running the Application

### Start the Backend

```bash
python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

### Start the Frontend

Open another terminal and execute:

```bash
python -m streamlit run frontend/app.py
```

The application will open in your web browser at:

```text
http://localhost:8501
```

## Project Documentation

The project is documented in eight phases:

1. Brainstorming and Ideation
2. Requirement Analysis
3. Project Design
4. Project Planning
5. Project Development
6. Project Testing
7. Project Documentation
8. Project Demonstration

## Project Links

* **GitHub Repository:** https://github.com/prabu270/Naan-Mudhalvan
* **Live Application:** Coming soon — Render deployment
* **Demo Video:** Coming soon — Demo video

## Future Enhancements

* Support for additional legal document templates.
* Multilingual document generation.
* Improved document formatting.
* User authentication.
* Document history and storage.
* Enhanced AI response validation.

## Disclaimer

LegalEase is intended for drafting assistance and educational purposes. AI-generated documents may contain errors or omissions and should be reviewed by a qualified legal professional before official use.

## Author

**M.K. Prabu**
