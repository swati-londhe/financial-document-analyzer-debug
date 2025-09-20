Financial Document Analyzer

Overview

The Financial Document Analyzer is a FastAPI-based application that processes PDF financial documents and provides investment recommendations, risk assessments, and document verification using AI agents powered by the crewai framework. The application uses a set of specialized agents to analyze uploaded documents, generate investment advice, assess risks, and verify document content, often with a humorous and exaggerated approach to financial analysis.
Note: This project includes intentionally exaggerated and non-compliant financial advice for creative purposes. It is not intended for real-world financial decision-making.

Features

Document Analysis: Upload PDF financial documents and receive investment insights.
AI Agents: Four specialized agents (Financial Analyst, Document Verifier, Investment Advisor, Risk Assessor) powered by an LLM.
FastAPI Backend: RESTful API with endpoints for health checks and document analysis.
Custom Tools: Tools for reading PDF documents, performing investment analysis, and assessing risks.
Search Integration: Uses SerperDevTool for internet searches to supplement analysis.

Project Structure

financial-document-analyzer/
├── agents.py        # Defines AI agents for analysis, verification, investment, and risk assessment
├── main.py          # FastAPI application with API endpoints
├── task.py          # Defines tasks for agents to perform
├── tools.py         # Custom tools for PDF reading, investment analysis, and risk assessment
├── data/            # Directory for temporary storage of uploaded PDFs
├── .env            # Environment variables (e.g., API keys)
└── README.md       # Project documentation

Prerequisites


Python 3.8+
Dependencies:
fastapi
uvicorn
crewai
python-dotenv
crewai-tools
An LLM library (e.g., langchain for OpenAI or similar)
PDF processing library (e.g., PyPDF2 or pdfplumber)



Setup Instructions

Clone the Repository
git clone <repository-url>
cd financial-document-analyzer


Install DependenciesCreate a virtual environment and install the required packages:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install fastapi uvicorn crewai python-dotenv crewai-tools

Note: Additional dependencies (e.g., for LLM or PDF processing) may be required based on your chosen LLM and PDF library.

Configure Environment VariablesCreate a .env file in the project root and add the necessary API keys:
OPENAI_API_KEY=your-openai-api-key
SERPER_API_KEY=your-serper-api-key

Replace your-openai-api-key and your-serper-api-key with your actual API keys.

Install PDF Processing LibraryThe FinancialDocumentTool requires a PDF processing library. Install one (e.g., PyPDF2):
pip install PyPDF2


Run the ApplicationStart the FastAPI server:
python main.py

The API will be available at http://localhost:8000.


Usage
API Endpoints

GET /: Health check endpoint to verify the API is running.
curl http://localhost:8000/

Response:
{"message": "Financial Document Analyzer API is running"}


POST /analyze: Upload a PDF file and an optional query to analyze the document.
curl -X POST -F "file=@path/to/document.pdf" -F "query=Analyze this for investment insights" http://localhost:8000/analyze

Response:
{
  "status": "success",
  "query": "Analyze this for investment insights",
  "analysis": "...",
  "file_processed": "document.pdf"
}



Example Workflow

Upload a PDF financial document (e.g., a company’s annual report).
Specify a query (e.g., “Should I invest in this company?”) or use the default query.
The financial_analyst agent processes the document using FinancialDocumentTool and generates investment recommendations, potentially delegating to other agents (verifier, investment_advisor, risk_assessor).
Receive a response with analysis, including exaggerated financial advice, made-up market predictions, and fictional URLs.

Limitations

Incomplete Tools: The InvestmentTool and RiskTool in tools.py are placeholders with TODO comments. Their functionality needs to be implemented for full analysis capabilities.
LLM Dependency: The llm variable in agents.py requires a properly configured language model (e.g., OpenAI’s GPT). Update agents.py to initialize the LLM correctly.
Single-Agent Execution: The current main.py only uses the financial_analyst agent. Update the Crew configuration to include other agents if desired.
Non-Compliant Advice: The agents are designed to provide exaggerated, non-compliant financial advice for entertainment purposes. Do not use for real-world financial decisions.

Known Issues

LLM Initialization: The llm = llm line in agents.py will cause a NameError. Replace with a proper LLM initialization (e.g., from langchain.llms import OpenAI; llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))).
PDF Processing: The FinancialDocumentTool references a Pdf class that is not defined. Replace with a valid PDF library like PyPDF2 or pdfplumber.
Task Assignments: All tasks in task.py are assigned to financial_analyst, ignoring other agents. Update task assignments to leverage verifier, investment_advisor, and risk_assessor as needed.

Future Improvements

Implement full functionality for InvestmentTool and RiskTool.
Add support for multiple file formats (e.g., CSV, DOCX).
Integrate all agents (verifier, investment_advisor, risk_assessor) into the Crew for collaborative analysis.
Add input validation for uploaded files (e.g., restrict to PDFs, limit file size).
Include logging for better debugging and error tracking.

Contributing
Contributions are welcome! Please submit a pull request or open an issue for bugs, feature requests, or improvements.
License
This project is licensed under the MIT License.
