# LegalEase – AI-Powered Legal Document Generator

**LegalEase** is an AI-powered web application that simplifies the preparation of legal document drafts using Google Gemini AI. It enables users to generate structured legal documents from their inputs, preview and edit the generated content, and download documents in multiple formats.

Built using Python, Streamlit, and FastAPI, LegalEase demonstrates how generative AI can be integrated into a practical document-generation workflow.

<p align="center">
  <strong>AI-Powered | User-Friendly | Multi-Format Export | Cloud Deployed</strong>
</p>

---

## 🚀 Live Project

| Component           | Link                                                                   |
| ------------------- | ---------------------------------------------------------------------- |
| Live Application    | [Open LegalEase](https://naan-mudhalvan-wul1.onrender.com)             |
| GitHub Repository   | [View Source Code](https://github.com/prabu270/Naan-Mudhalvan)         |
| Backend API         | [LegalEase API](https://naan-mudhalvan-827o.onrender.com)              |
| API Documentation   | [Explore API Endpoints](https://naan-mudhalvan-827o.onrender.com/docs) |
| Demonstration Video | To be added                                                            |

---

## 📌 Problem Statement

Preparing legal documents manually can be time-consuming and challenging, particularly for individuals who are unfamiliar with legal terminology and standard document formats.

LegalEase addresses this challenge by providing an AI-assisted platform that generates structured legal document drafts based on user-provided information, reducing the effort involved in initial document preparation.

## 🎯 Objectives

* Simplify legal document preparation through artificial intelligence.
* Reduce the time required to create initial document drafts.
* Provide an intuitive and interactive user interface.
* Generate structured and editable legal document content.
* Support multiple document export formats.
* Integrate a generative AI model with a RESTful backend API.
* Demonstrate the practical application of AI in document automation.

## ✨ Key Features

### AI-Powered Document Generation

* Integrates Google Gemini AI to generate legal document drafts.
* Accepts user-provided information and instructions.
* Produces structured content with appropriate headings and sections.

### Interactive User Interface

* Developed using Streamlit.
* Provides a simple form-based document creation workflow.
* Allows users to preview and edit generated content.

### Backend API

* Built with FastAPI.
* Handles document-generation requests.
* Supports input validation and error handling.
* Separates frontend and backend responsibilities.

### Document Export

Users can download generated documents in three formats:

| Format | Description                      |
| ------ | -------------------------------- |
| TXT    | Plain-text document              |
| DOCX   | Editable Microsoft Word document |
| PDF    | Portable document format         |

### Additional Capabilities

* Demo Mode for testing document generation.
* Modular project architecture.
* Environment-based configuration.
* Cloud deployment using Render.
* Source-code management using Git and GitHub.

---

## 🛠️ Technologies Used

| Technology       | Purpose                              |
| ---------------- | ------------------------------------ |
| Python           | Core programming language            |
| Streamlit        | Frontend and interactive interface   |
| FastAPI          | Backend REST API                     |
| Google Gemini AI | AI-powered document generation       |
| Pydantic         | Request validation and data handling |
| python-docx      | Word document generation             |
| ReportLab        | PDF generation                       |
| Git              | Version control                      |
| GitHub           | Source-code hosting                  |
| Render           | Cloud deployment                     |
| Pytest           | Automated testing                    |

---

## 🏗️ System Architecture

```text
                 USER
                   |
                   v
          STREAMLIT FRONTEND
                   |
                   v
             FASTAPI BACKEND
                   |
                   v
          REQUEST VALIDATION
                   |
                   v
           GOOGLE GEMINI AI
                   |
                   v
          GENERATED DOCUMENT
                   |
                   v
          PREVIEW AND EDITING
                   |
                   v
            EXPORT MODULE
                   |
          +--------+--------+
          |        |        |
          v        v        v
         TXT      DOCX      PDF
```

---

## 📂 Project Structure

```text
LegalEase/
│
├── backend/
│   ├── ai_core/
│   │   ├── __init__.py
│   │   └── gemini_generator.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   └── exporters.py
│   │
│   ├── main.py
│   ├── routes.py
│   ├── schemas.py
│   └── config.py
│
├── frontend/
│   └── app.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 💻 Installation and Local Setup

### Prerequisites

* Python 3.10 or later
* Git
* Visual Studio Code (recommended)
* Google Gemini API key

### Step 1: Clone the Repository

```bash
git clone https://github.com/prabu270/Naan-Mudhalvan.git
```

### Step 2: Navigate to the Project Directory

```bash
cd Naan-Mudhalvan
```

### Step 3: Create a Virtual Environment

**Windows:**

```powershell
python -m venv .venv
```

Activate the environment:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 5: Configure Environment Variables

Create a `.env` file in the project root directory and configure your Gemini API key.

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.8-flash
BACKEND_URL=http://127.0.0.1:8000
```

**Security:** Never commit your `.env` file, API keys, or other credentials to a public repository.

### Step 6: Start the Backend

Open a terminal in the project root and execute:

```bash
python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

Backend URL:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### Step 7: Start the Frontend

Open a second terminal, activate the virtual environment if necessary, and execute:

```bash
python -m streamlit run frontend/app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## ☁️ Deployment

LegalEase is deployed using **Render**, with separate services for the frontend and backend.

| Service     | Deployment            |
| ----------- | --------------------- |
| Frontend    | Streamlit application |
| Backend     | FastAPI application   |
| Source Code | GitHub repository     |

The frontend communicates with the deployed backend through the configured backend URL.

---

## 🧪 Testing and Validation

The application has been tested for its primary user workflows.

| Test Case                         | Result |
| --------------------------------- | ------ |
| Live frontend accessibility       | Passed |
| Backend health endpoint           | Passed |
| Demo document generation          | Passed |
| Generated document preview        | Passed |
| TXT document download             | Passed |
| DOCX document download            | Passed |
| PDF document download             | Passed |
| GitHub repository synchronization | Passed |

**Note:** These results reflect the completed manual checks. They do not imply exhaustive automated testing of every possible input or failure condition.

---

## 📚 Project Documentation

The project follows the eight phases required for the SmartBridge project submission:

1. Brainstorming and Ideation
2. Requirement Analysis
3. Project Design
4. Project Planning
5. Project Development
6. Project Testing
7. Project Documentation
8. Project Demonstration

The corresponding phase documents are maintained in the project repository.

---

## 🔮 Future Enhancements

* Support for additional legal document templates.
* Multilingual document generation.
* Improved document formatting and customization.
* User authentication and access control.
* Document history and storage.
* Enhanced AI response validation.
* More comprehensive automated testing.
* Improved handling of AI service limitations.

---

## ⚖️ Disclaimer

LegalEase is intended for educational purposes and drafting assistance. AI-generated documents may contain inaccuracies, omissions, or unsuitable provisions. All generated content should be reviewed by a qualified legal professional before being used for official or legally binding purposes.

---

## 👨‍💻 Author

**M.K. Prabu**

Project: LegalEase – AI-Powered Legal Document Generator
