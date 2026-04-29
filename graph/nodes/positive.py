from graph.state import ReviewInputState
from core.llm import llm

def positive_response(state: ReviewInputState):
    prompt = f"""
    You are a friendly and professional customer support assistant.

    Task:
    Write a warm and genuine thank-you response to a positive customer review.

    Review:
    \"\"\"{state["review_text"]}\"\"\"

    Instructions:
    - Express sincere appreciation
    - Acknowledge the positive experience briefly
    - Keep tone warm, natural, and human
    - Keep it concise (1–2 sentences)

    Constraints:
    - Do NOT sound robotic or overly formal
    - Do NOT repeat the review word-for-word
    - Do NOT include explanations or extra text

    """
    response = llm.invoke(prompt)
    return {'response': response}