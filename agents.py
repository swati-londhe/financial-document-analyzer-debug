## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from langchain_community.llms import HuggingFaceHub

from tools import search_tool, read_data_tool, analyze_investment_tool, create_risk_assessment_tool

### Loading LLM from Hugging Face
llm = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    model_kwargs={"temperature": 0.5, "max_length": 512}
)

# Creating an Experienced Financial Analyst agent
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze the financial document and provide data-driven insights for the query: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You are an experienced financial analyst with expertise in market trends, financial ratios, and investment strategies. "
        "You carefully read financial reports and use data to provide accurate analysis."
    ),
    tools=[read_data_tool, search_tool],
    llm=llm,
    max_iter=5,
    max_rpm=10,
    allow_delegation=True
)

# Creating a document verifier agent
verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify that the uploaded document is a valid financial report and extract key sections.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a specialist in verifying financial documents. You check for authenticity and relevance to ensure accurate analysis."
    ),
    llm=llm,
    max_iter=5,
    max_rpm=10,
    allow_delegation=False,
    tools=[read_data_tool]
)


investment_advisor = Agent(
    role="Investment Advisor",
    goal="Provide investment recommendations based on the financial analysis for the query: {query}",
    verbose=True,
    backstory=(
        "You are a certified investment advisor with years of experience. You use financial data to recommend balanced strategies."
    ),
    llm=llm,
    max_iter=5,
    max_rpm=10,
    allow_delegation=False,
    tools=[analyze_investment_tool, search_tool]
)


risk_assessor = Agent(
    role="Risk Assessor",
    goal="Assess risks based on the financial document and market conditions for the query: {query}",
    verbose=True,
    backstory=(
        "You specialize in risk management, identifying potential volatilities and mitigation strategies from financial data."
    ),
    llm=llm,
    max_iter=5,
    max_rpm=10,
    allow_delegation=False,
    tools=[create_risk_assessment_tool, search_tool]
)