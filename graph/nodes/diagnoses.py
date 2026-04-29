from graph.state import ReviewInputState
from core.llm import llm
from schema.diagnoses_schema import RunDiagnosesSchema

def run_diagnoses(state: ReviewInputState):
    prompt = f"""
    You are an AI assistant specialized in analyzing negative customer reviews.

    Review:
    \"\"\"{state['review_text']}\"\"\"

    Task:
    Extract a structured diagnosis of the review.

    Instructions:
    - Identify the SINGLE most dominant issue
    - Do NOT invent issues not mentioned
    - Be concise and accurate
    - If the review is vague, choose the closest matching category

    Allowed values:

    issue_type:
    Product Quality, Delivery/Shipping, Customer Service, Pricing, Usability, Other

    tone:
    angry, frustrated, disappointed, neutral

    urgency:
    high → strong anger or demand for action
    medium → clear dissatisfaction
    low → mild or vague complaint

    Output Rules:
    - Return ONLY structured output matching the schema
    - Do NOT include explanations or extra text
    """
    run_diagnoses_llm = llm.with_structured_output(RunDiagnosesSchema)
    diagnoses = run_diagnoses_llm.invoke(prompt)
    return {'diagnoses': diagnoses.model_dump()}