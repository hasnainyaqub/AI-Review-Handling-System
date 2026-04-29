from langchain_groq import ChatGroq

from core.config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE
from schema.agent_schema import SentimentSchema

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=MODEL_NAME,
    temperature=TEMPERATURE
)

sentiment_llm = llm.with_structured_output(SentimentSchema)
