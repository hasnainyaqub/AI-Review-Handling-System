from pydantic import BaseModel, Field
from typing import Literal

class SentimentSchema(BaseModel):
    sentiment : Literal['positive', 'negative'] = Field(description='The sentiment of the revie')
