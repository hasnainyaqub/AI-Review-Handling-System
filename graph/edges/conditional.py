from typing_extensions import Literal

from graph.state import ReviewInputState

def sentiment_router(state: ReviewInputState) -> Literal['positive_response', "run_diagnoses"]:
    sentiment = state['sentiment']
    if sentiment == 'positive':
        return 'positive_response'
    else: 
        return 'run_diagnoses'