from pydantic import BaseModel

class AgentRequest(BaseModel):
    review_text: str