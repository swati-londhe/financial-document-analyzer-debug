# 💰 Financial Document Analyzer (Debug Version)

The **Financial Document Analyzer** is a **FastAPI-based AI application** that processes PDF financial documents and provides **investment recommendations**, **risk assessments**, and **document verification** using AI agents powered by the **CrewAI** framework.

> ⚠️ **Note:** This project includes intentionally exaggerated and non-compliant financial advice for creative and educational purposes.  
> It is **not intended for real-world financial decision-making.**

---

## 🚀 Overview

This **debug version** includes fixed bugs, improved project structure, and smoother execution for testing and demonstration.

### ✨ Features

- 📄 **Document Analysis:** Upload PDF financial documents and get AI-generated investment insights.  
- 🧠 **AI Agents:** Four specialized agents powered by an LLM:
  - Financial Analyst  
  - Document Verifier  
  - Investment Advisor  
  - Risk Assessor  
- ⚙️ **FastAPI Backend:** RESTful API with health checks and document analysis endpoints.  
- 🧰 **Custom Tools:** PDF reading, investment analysis, and risk assessment.  
- 🔍 **Search Integration:** Uses `SerperDevTool` for supplemental web searches.  
- 🪲 **Debug Fixes:** Corrected agent initialization and PDF processing issues.

---

## 📂 Project Structure

financial-document-analyzer/
├── agents.py # Defines AI agents
├── main.py # FastAPI application with API endpoints
├── task.py # Defines tasks for agents
├── tools.py # Custom tools for PDF reading, investment analysis, and risk assessment
├── data/ # Folder for temporary storage of uploaded PDFs
├── .env # Environment variables (API keys)
└── README.md # Project documentation

yaml
Copy code

---

## 🧩 Prerequisites

- 🐍 **Python 3.8+**
- 📦 **Dependencies:**  
  `fastapi`, `uvicorn`, `crewai`, `crewai-tools`, `python-dotenv`,  
  PDF processing library (`PyPDF2` or `pdfplumber`)  
- 🤖 **LLM library:** `langchain` (for OpenAI or similar)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/swati-londhe/financial-document-analyzer-debug.git
cd financial-document-analyzer-debug
2️⃣ Create Virtual Environment
bash
Copy code
python -m venv venv
Activate it:

Windows:

bash
Copy code
venv\Scripts\activate
macOS/Linux:

bash
Copy code
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Configure Environment Variables
Create a .env file in the project root:

bash
Copy code
OPENAI_API_KEY=your-openai-api-key
SERPER_API_KEY=your-serper-api-key
5️⃣ Install PDF Processing Library
bash
Copy code
pip install PyPDF2
(or use pdfplumber if preferred)

6️⃣ Run the Application
bash
Copy code
python main.py
Access API at: http://localhost:8000

🔌 API Endpoints
✅ Health Check
bash
Copy code
curl http://localhost:8000/
Response:

json
Copy code
{"message": "Financial Document Analyzer API is running"}
📊 Analyze PDF Document
bash
Copy code
curl -X POST -F "file=@path/to/document.pdf" \
     -F "query=Analyze this for investment insights" \
     http://localhost:8000/analyze
Response Example:

json
Copy code
{
  "status": "success",
  "query": "Analyze this for investment insights",
  "analysis": "...",
  "file_processed": "document.pdf"
}
🧠 Debug Notes
LLM Initialization:
Fixed llm initialization in agents.py.
Use a valid LLM such as OpenAI GPT:

python
Copy code
from langchain.llms import OpenAI
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
PDF Processing:
Corrected FinancialDocumentTool to use PyPDF2 or pdfplumber.

Task Assignment:
Tasks are now correctly mapped to respective agents.

⚠️ Limitations
🚧 Incomplete Tools: InvestmentTool and RiskTool have placeholder TODOs.
🧍‍♂️ Single-Agent Execution: Currently, main.py uses only the Financial Analyst.
💬 Non-Compliant Advice: Intended for demonstration, not real-world finance.

🔮 Future Improvements
✅ Complete functionality for InvestmentTool and RiskTool.
📄 Add support for additional file formats (CSV, DOCX).
🤝 Enable collaborative execution among all agents.
🧾 Implement input validation and detailed error tracking.
🪶 Add logging for better debugging.

🤝 Contributing
Contributions are always welcome!
Submit a Pull Request or open an Issue for bugs, new features, or improvements.

📜 License
This project is licensed under the MIT License.

👩‍💻 Author
Swati Londhe
Python Developer | Data Science Enthusiast | Open Source Contributor

🌐 GitHub • LinkedIn
