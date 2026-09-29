import os
from datetime import date

import requests
import streamlit as st
from dotenv import load_dotenv

from backend.utils.exporters import (
    format_docx,
    format_pdf,
    format_txt,
)


load_dotenv()


BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000",
)


st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide",
)


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 0;
    }

    .subtitle {
        font-size: 18px;
        color: #666;
        margin-top: 0;
    }

    .document-box {
        border: 1px solid #dddddd;
        border-radius: 10px;
        padding: 20px;
        background: #fafafa;
    }

    .disclaimer {
        font-size: 13px;
        color: #777;
        padding: 12px;
        border-left: 4px solid #999;
        background: #f5f5f5;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# Header
# ============================================================

st.markdown(
    '<div class="main-title">⚖️ LegalEase</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">AI-Powered Legal Document Generator</div>',
    unsafe_allow_html=True,
)

st.divider()


# ============================================================
# Sidebar
# ============================================================

with st.sidebar:

    st.header("LegalEase Settings")

    document_type = st.selectbox(
        "Document Type",
        [
            "Employment Agreement",
            "Lease Agreement",
            "Non-Disclosure Agreement",
            "Service Agreement",
            "Freelance Agreement",
            "Business Agreement",
            "Custom Legal Document",
        ],
    )

    language = st.selectbox(
        "Language",
        [
            "English",
            "Tamil",
            "Hindi",
            "Telugu",
            "Malayalam",
            "Kannada",
        ],
    )

    jurisdiction = st.text_input(
        "Jurisdiction",
        value="India",
    )

    company_name = st.text_input(
        "Company / Brand Name",
        value="LegalEase",
    )

    demo_mode = st.checkbox(
        "Demo Mode",
        value=False,
        help="Use this when you want to test the application without calling Gemini.",
    )


# ============================================================
# Input Section
# ============================================================

st.header("1. Document Information")

col1, col2 = st.columns(2)

with col1:

    party_one_name = st.text_input(
        "Party 1 Name",
        placeholder="Example: ABC Technologies Pvt. Ltd.",
    )

    party_one_role = st.text_input(
        "Party 1 Role",
        placeholder="Example: Employer",
    )

with col2:

    party_two_name = st.text_input(
        "Party 2 Name",
        placeholder="Example: John Kumar",
    )

    party_two_role = st.text_input(
        "Party 2 Role",
        placeholder="Example: Employee",
    )


effective_date = st.date_input(
    "Effective Date",
    value=date.today(),
)


st.header("2. Key Terms")

terms_col1, terms_col2 = st.columns(2)

with terms_col1:

    payment_terms = st.text_area(
        "Payment / Compensation",
        placeholder="Example: ₹30,000 per month",
    )

    duration = st.text_input(
        "Duration",
        placeholder="Example: 12 months",
    )

    termination = st.text_area(
        "Termination Terms",
        placeholder="Example: 30 days written notice",
    )

with terms_col2:

    responsibilities = st.text_area(
        "Responsibilities",
        placeholder="Enter the main responsibilities...",
    )

    confidentiality = st.text_area(
        "Confidentiality",
        placeholder="Enter confidentiality requirements...",
    )

    additional_terms = st.text_area(
        "Additional Terms",
        placeholder="Any other important terms...",
    )


additional_instructions = st.text_area(
    "Additional Instructions for AI",
    placeholder="Example: Make the language professional and easy to understand.",
)


# ============================================================
# Generate
# ============================================================

st.header("3. Generate Document")

generate_button = st.button(
    "⚖️ Generate Legal Document",
    type="primary",
    use_container_width=True,
)


if generate_button:

    parties = {
        "Party 1 Name": party_one_name,
        "Party 1 Role": party_one_role,
        "Party 2 Name": party_two_name,
        "Party 2 Role": party_two_role,
    }

    terms = {
        "Payment / Compensation": payment_terms,
        "Duration": duration,
        "Termination": termination,
        "Responsibilities": responsibilities,
        "Confidentiality": confidentiality,
        "Additional Terms": additional_terms,
    }

    payload = {
        "document_type": document_type,
        "parties": parties,
        "terms": terms,
        "effective_date": effective_date.isoformat(),
        "jurisdiction": jurisdiction,
        "language": language,
        "company_name": company_name,
        "additional_instructions": additional_instructions,
        "demo_mode": demo_mode,
    }

    with st.spinner("Generating your legal document..."):

        try:

            response = requests.post(
                f"{BACKEND_URL}/generate",
                json=payload,
                timeout=120,
            )

            if response.status_code == 200:

                data = response.json()

                if data.get("success"):

                    st.session_state["document"] = data["document"]
                    st.session_state["document_type"] = data[
                        "document_type"
                    ]

                    st.success(
                        data.get(
                            "message",
                            "Document generated successfully.",
                        )
                    )

                else:

                    st.error(
                        "The backend did not generate a document."
                    )

            else:

                try:
                    error_detail = response.json().get(
                        "detail",
                        response.text,
                    )
                except Exception:
                    error_detail = response.text

                st.error(
                    f"Backend error: {error_detail}"
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "Could not connect to the FastAPI backend. "
                "Make sure the backend is running on "
                f"{BACKEND_URL}."
            )

        except requests.exceptions.Timeout:

            st.error(
                "The request timed out. "
                "Please try again."
            )

        except Exception as exc:

            st.error(
                f"Unexpected error: {exc}"
            )


# ============================================================
# Editor / Preview
# ============================================================

if "document" in st.session_state:

    st.divider()

    st.header("4. Edit & Preview")

    edited_document = st.text_area(
        "Editable Document",
        value=st.session_state["document"],
        height=650,
    )

    st.session_state["document"] = edited_document

    st.subheader("Preview")

    st.markdown(
        '<div class="document-box">',
        unsafe_allow_html=True,
    )

    preview_text = edited_document.replace(
        "\n",
        "<br>",
    )

    st.markdown(
        preview_text,
        unsafe_allow_html=True,
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )


    # ========================================================
    # Downloads
    # ========================================================

    st.header("5. Export Document")

    txt_data = format_txt(edited_document)

    docx_data = format_docx(
        edited_document,
        company_name=company_name,
    )

    pdf_data = format_pdf(
        edited_document,
        company_name=company_name,
    )

    export_col1, export_col2, export_col3 = st.columns(3)

    with export_col1:

        st.download_button(
            label="Download TXT",
            data=txt_data,
            file_name="legalease_document.txt",
            mime="text/plain",
            use_container_width=True,
        )

    with export_col2:

        st.download_button(
            label="Download DOCX",
            data=docx_data,
            file_name="legalease_document.docx",
            mime=(
                "application/"
                "vnd.openxmlformats-officedocument."
                "wordprocessingml.document"
            ),
            use_container_width=True,
        )

    with export_col3:

        st.download_button(
            label="Download PDF",
            data=pdf_data,
            file_name="legalease_document.pdf",
            mime="application/pdf",
            use_container_width=True,
        )


    st.markdown(
        """
        <div class="disclaimer">
        LegalEase generates AI-assisted legal document drafts.
        Always review the generated document carefully and obtain
        professional legal advice when appropriate before signing
        or using a legal document.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# Footer
# ============================================================

st.divider()

st.caption(
    "LegalEase | AI-Powered Legal Document Generator"
)