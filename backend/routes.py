from fastapi import APIRouter, HTTPException

from backend.ai_core.gemini_generator import (
    generate_demo_document,
    generate_with_gemini,
)
from backend.schemas import DocumentRequest, DocumentResponse


router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "LegalEase API",
    }


@router.post(
    "/generate",
    response_model=DocumentResponse,
)
def generate_document(request: DocumentRequest):

    try:

        if request.demo_mode:

            document = generate_demo_document(
                document_type=request.document_type,
                parties=request.parties,
                terms=request.terms,
                effective_date=request.effective_date,
                jurisdiction=request.jurisdiction,
                language=request.language,
                company_name=request.company_name,
            )

            return DocumentResponse(
                success=True,
                document=document,
                document_type=request.document_type,
                language=request.language,
                message="Demo document generated successfully.",
            )

        document = generate_with_gemini(
            document_type=request.document_type,
            parties=request.parties,
            terms=request.terms,
            effective_date=request.effective_date,
            jurisdiction=request.jurisdiction,
            language=request.language,
            company_name=request.company_name,
            additional_instructions=request.additional_instructions,
        )

        return DocumentResponse(
            success=True,
            document=document,
            document_type=request.document_type,
            language=request.language,
            message="Document generated successfully.",
        )

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=str(exc),
        ) from exc