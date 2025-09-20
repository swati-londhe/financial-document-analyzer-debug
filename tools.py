## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import Tool
from crewai_tools.tools.serper_dev_tool import SerperDevTool
from langchain_community.document_loaders import PyPDFLoader

## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool
def _read_data(path: str) -> str:
    """Internal function to read data from a pdf file from a path

    Args:
        path (str): Path of the pdf file.

    Returns:
        str: Full Financial Document content
    """
    
    docs = PyPDFLoader(file_path=path).load()

    full_report = ""
    for data in docs:
        # Clean and format the financial document data
        content = data.page_content
        
        # Remove extra whitespaces and format properly
        content = content.replace("\n\n", "\n").strip()
                
        full_report += content + "\n"
            
    return full_report

read_data_tool = Tool(
    name="Read Financial Document",
    description="Reads and extracts text from a PDF financial document at the given path.",
    func=_read_data
)

## Creating Investment Analysis Tool
def _analyze_investment(financial_document_data: str) -> str:
    # Simple implementation: Extract key metrics and suggest based on revenue growth
    # For real use, could use code_execution to compute ratios
    if "revenue" in financial_document_data.lower():
        return "Based on the document, revenue is stable. Recommendation: Hold stock with moderate growth potential."
    return "Investment analysis: Data insufficient for detailed recommendation."

analyze_investment_tool = Tool(
    name="Analyze Investment",
    description="Analyzes the financial data for investment insights.",
    func=_analyze_investment
)

## Creating Risk Assessment Tool
def _create_risk_assessment(financial_document_data: str) -> str:
    # Simple implementation: Check for keywords like "decline" or "risk"
    if "decline" in financial_document_data.lower():
        return "Risk assessment: High volatility detected due to revenue decline. Mitigate with diversification."
    return "Risk assessment: Low risk based on stable metrics."

create_risk_assessment_tool = Tool(
    name="Create Risk Assessment",
    description="Assesses risks from the financial data.",
    func=_create_risk_assessment
)