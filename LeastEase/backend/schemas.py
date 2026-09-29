from pydantic import BaseModel
from typing import Any, Optional


class DocumentRequest(BaseModel):
    document_type: str
    parties: Any
    terms: Any
    effective_date: str
    jurisdiction: str
    language: str
    company_name: str
    demo_mode: bool = True
    additional_instructions: Optional[str] = ""


class DocumentResponse(BaseModel):
    success: bool
    document: str
    document_type: str
    language: str
    message: str