from graph.state import ReviewInputState
from core.llm import sentiment_llm

def sentiment_find(state: ReviewInputState):

    review = state['review_text']
    sentiment = sentiment_llm.invoke(review).sentiment
    return {'sentiment': sentiment}