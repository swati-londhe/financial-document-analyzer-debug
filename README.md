Financial Document Analyzer (Debug Version)
Overview

The Financial Document Analyzer is a FastAPI-based application that processes PDF financial documents and provides investment recommendations, risk assessments, and document verification using AI agents powered by the crewai framework.

⚠️ Note: This project includes intentionally exaggerated and non-compliant financial advice for creative purposes. It is not intended for real-world financial decision-making.

This debug version includes fixes to the code and updated project structure.

Features

Document Analysis: Upload PDF financial documents and receive AI-generated investment insights.

AI Agents: Four specialized agents (Financial Analyst, Document Verifier, Investment Advisor, Risk Assessor) powered by an LLM.

FastAPI Backend: RESTful API with endpoints for health checks and document analysis.

Custom Tools: PDF reading, investment analysis, and risk assessment.

Search Integration: Uses SerperDevTool for supplemental internet searches.

Debug Fixes: Corrected issues in agent initialization and PDF processing for smoother execution.

Project Structure
financial-document-analyzer/
├── agents.py          # Defines AI agents
├── main.py            # FastAPI application with API endpoints
├── task.py            # Defines tasks for agents
├── tools.py           # Custom tools for PDF reading, investment analysis, and risk assessment
├── data/              # Folder for temporary storage of uploaded PDFs
├── .env               # Environment variables (API keys)
└── README.md          # Project documentation

Prerequisites

Python 3.8+

Dependencies: fastapi, uvicorn, crewai, python-dotenv, crewai-tools, PDF processing library (e.g., PyPDF2 or pdfplumber)

LLM library (e.g., langchain for OpenAI or similar)

Setup Instructions
1. Clone the Repository
git clone https://github.com/swati-londhe/financial-document-analyzer-debug.git
cd financial-document-analyzer-debug

2. Install Dependencies
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt

3. Configure Environment Variables

Create a .env file in the project root:

OPENAI_API_KEY=your-openai-api-key
SERPER_API_KEY=your-serper-api-key

4. Install PDF Processing Library
pip install PyPDF2
# Or pdfplumber if preferred

5. Run the Application
python main.py


Access API at http://localhost:8000.

API Endpoints

GET / – Health check:

curl http://localhost:8000/
# Response: {"message": "Financial Document Analyzer API is running"}


POST /analyze – Upload PDF and optional query:

curl -X POST -F "file=@path/to/document.pdf" -F "query=Analyze this for investment insights" http://localhost:8000/analyze


Response Example:

{
  "status": "success",
  "query": "Analyze this for investment insights",
  "analysis": "...",
  "file_processed": "document.pdf"
}

Debug Notes

LLM Initialization: Fixed llm initialization in agents.py. Use a valid LLM like OpenAI GPT:

from langchain.llms import OpenAI
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


PDF Processing: Corrected FinancialDocumentTool to use PyPDF2 or pdfplumber.

Task Assignment: Tasks are now properly aligned with their respective agents.

Limitations

Incomplete Tools: InvestmentTool and RiskTool still have placeholders (TODO comments).

Single-Agent Execution: Currently, main.py primarily uses financial_analyst. Other agents can be integrated.

Non-Compliant Advice: Exaggerated advice for entertainment only.

Future Improvements

Full functionality for InvestmentTool and RiskTool.

Support for additional file formats (CSV, DOCX).

Collaborative execution of all agents.

Input validation for uploaded files.

Logging and enhanced error tracking.

Contributing

Contributions are welcome! Submit a pull request or open an issue for bugs, features, or improvements.

License

This project is licensed under the MIT License.
