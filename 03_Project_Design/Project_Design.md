# Phase 3: Project Design

## 1. Introduction

Project design defines the architecture, components, workflow, and structure of the LegalEase application. It explains how the frontend, backend, and AI model work together to generate legal document drafts.

## 2. System Architecture

LegalEase follows a client-server architecture consisting of three major components:

1. **Frontend:** Streamlit provides the user interface for entering details, viewing generated documents, editing content, and downloading files.
2. **Backend:** FastAPI handles API requests, validates inputs, communicates with the AI module, and manages document export.
3. **AI Integration:** Google Gemini generates document drafts based on the information provided by the user.

## 3. System Workflow

1. The user opens the LegalEase application.
2. The user selects a document type.
3. The user enters the required information.
4. The frontend sends the information to the FastAPI backend.
5. The backend validates and processes the request.
6. The AI module sends the prompt to Google Gemini.
7. Gemini generates the document draft.
8. The backend returns the generated content to the frontend.
9. The user reviews and edits the document.
10. The user downloads the document in the required format.

## 4. Main Modules

### Frontend Module

* Built using Streamlit.
* Collects user inputs.
* Displays generated document content.
* Provides editing and download options.

### Backend Module

* Built using FastAPI.
* Handles API requests and responses.
* Validates user inputs.
* Connects the frontend with the AI module.
* Manages document export operations.

### AI Generation Module

* Integrates Google Gemini.
* Creates prompts using user-provided details.
* Generates structured legal document drafts.
* Returns generated content to the backend.

### Document Export Module

* Supports TXT, DOCX, and PDF formats.
* Converts generated content into downloadable files.
* Provides documents in a structured format.

## 5. Data Flow Design

The application follows this data flow:

**User Input → Streamlit Frontend → FastAPI Backend → Gemini AI → Backend Response → Document Preview → Export**

## 6. Project Directory Structure

The project is organized into separate folders for better maintainability.

```text
LegalEase/
├── backend/
│   ├── main.py
│   ├── routes.py
│   ├── schemas.py
│   ├── config.py
│   ├── ai_core/
│   │   └── gemini_generator.py
│   └── utils/
│       ├── sanitization.py
│       └── exporters.py
├── frontend/
│   └── app.py
├── assets/
│   └── legalese_logo.svg
├── tests/
│   ├── test_api.py
│   └── test_exporters.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 7. Security Design

* Store API keys in environment variables.
* Avoid exposing sensitive credentials in public repositories.
* Validate and sanitize user inputs.
* Handle API errors safely.
* Remind users to review AI-generated legal drafts before official use.

## 8. User Interface Design

The interface is designed to be simple and accessible. It includes:

* Application title and logo
* Document type selection
* Input fields for required details
* Generate document button
* Editable document preview
* Download buttons for supported formats

## 9. Conclusion

The design of LegalEase provides a clear structure for integrating Streamlit, FastAPI, and Google Gemini. Modular architecture makes the application easier to develop, test, maintain, and improve in the future.
