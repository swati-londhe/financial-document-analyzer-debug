## Importing libraries and files
from crewai import Task

from agents import verifier, financial_analyst, investment_advisor, risk_assessor
from tools import read_data_tool, search_tool

## Creating a verification task
verification = Task(
    description="Verify if the document at {file_path} is a valid financial report. If yes, summarize key sections. Query: {query}",
    expected_output="Verification result and summary of key financial sections in bullet points.",
    agent=verifier,
    tools=[read_data_tool],
    async_execution=False,
)

## Creating an analysis task
analyze_financial_document = Task(
    description="Analyze the financial document at {file_path} for key metrics, trends, and insights related to the query: {query}. Use search if needed for market context.",
    expected_output="Detailed analysis report with financial metrics, trends, and insights in structured format (e.g., bullet points or table).",
    agent=financial_analyst,
    tools=[read_data_tool, search_tool],
    async_execution=False,
)

## Creating an investment analysis task
investment_analysis = Task(
    description="Based on the financial analysis, provide investment recommendations for the query: {query}. Use tools to analyze data.",
    expected_output="Investment recommendations with pros, cons, and suggested strategies in bullet points.",
    agent=investment_advisor,
    tools=[read_data_tool, search_tool],
    async_execution=False,
)

## Creating a risk assessment task
risk_assessment = Task(
    description="Assess risks from the financial document and external factors for the query: {query}. Provide mitigation strategies.",
    expected_output="Risk assessment report with identified risks and mitigation plans in bullet points.",
    agent=risk_assessor,
    tools=[read_data_tool, search_tool],
    async_execution=False,
)