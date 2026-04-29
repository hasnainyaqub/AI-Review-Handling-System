from typing import TypedDict, Literal

class ReviewInputState(TypedDict):
    review_text: str
    sentiment: Literal['postive', 'negative']
    diagnoses: dict
    response: str