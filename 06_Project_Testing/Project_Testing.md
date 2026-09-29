# Phase 6: Project Testing

## 1. Introduction

Project testing is performed to verify the functionality, reliability, and performance of the LegalEase application. The purpose is to identify errors, validate system behavior, and ensure that the application meets the defined requirements.

## 2. Testing Objectives

* Verify that the frontend works correctly.
* Ensure proper communication between frontend and backend.
* Validate AI-based document generation.
* Check document editing functionality.
* Verify TXT, DOCX, and PDF exports.
* Identify and resolve errors.
* Ensure appropriate handling of invalid inputs and API failures.

## 3. Types of Testing

### Functional Testing

Checks whether the application features work according to requirements.

### Integration Testing

Verifies communication between Streamlit, FastAPI, and Google Gemini.

### API Testing

Checks whether backend endpoints receive requests and return appropriate responses.

### Error Handling Testing

Verifies that the application handles invalid inputs, API failures, and export errors properly.

### Export Testing

Ensures that generated documents can be downloaded in the supported formats.

## 4. Test Cases

| Test Case ID | Test Scenario                 | Expected Result                            |
| ------------ | ----------------------------- | ------------------------------------------ |
| TC01         | Open the application          | Homepage loads successfully                |
| TC02         | Enter valid document details  | Inputs are accepted                        |
| TC03         | Generate a document           | AI-generated draft is displayed            |
| TC04         | Submit incomplete information | Appropriate validation message appears     |
| TC05         | Edit generated content        | Changes are reflected in the preview       |
| TC06         | Download TXT file             | TXT file is generated successfully         |
| TC07         | Download DOCX file            | Editable Word document is generated        |
| TC08         | Download PDF file             | PDF document is generated                  |
| TC09         | Simulate API failure          | User receives an appropriate error message |
| TC10         | Check backend API             | API responds as expected                   |

## 5. Testing Tools

* **Swagger UI:** Used to test FastAPI endpoints.
* **Postman:** Used for API request testing.
* **Pytest:** Used to execute automated tests.
* **Browser:** Used to verify the Streamlit interface.

## 6. Testing Process

1. Start the FastAPI backend.
2. Start the Streamlit frontend.
3. Enter sample document details.
4. Generate a document using Gemini AI.
5. Verify the generated content.
6. Test editing functionality.
7. Download the document in TXT, DOCX, and PDF formats.
8. Check the behavior when invalid inputs or API errors occur.
9. Record the test results and fix identified issues.

## 7. Test Results

Test results should be recorded after executing each test case.

| Test Case           | Status         |
| ------------------- | -------------- |
| Application loading | To be verified |
| Document generation | To be verified |
| Document editing    | To be verified |
| TXT export          | To be verified |
| DOCX export         | To be verified |
| PDF export          | To be verified |
| API error handling  | To be verified |

**Note:** Update the test status based on actual execution results.

## 8. Conclusion

Testing helps ensure that LegalEase functions as expected and provides a reliable user experience. It verifies the integration of the frontend, backend, AI generation, and document export modules before the final demonstration.
