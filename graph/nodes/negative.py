from graph.state import ReviewInputState
from core.llm import llm

def negative_response(state: ReviewInputState):
    diagnoses = state['diagnoses']
    prompt = f"""You are a support assistant.
    The user had a '{diagnoses['issue_type']}' issue, sounded '{diagnoses['tone']}', and marked urgency as '{diagnoses['urgency']}'.
    Write an empathetic, helpful resolution message.
    STRICT FORMAT CONTROL:

- Output MUST be a single paragraph
- Do NOT use bullet points, lists, or numbering
- Do NOT use markdown formatting (**, -, etc.)
- Do NOT include greetings like "Hi [Customer Name]"
- Do NOT include signatures, names, or company titles

STRICT LENGTH:

- Maximum 80 words
- Do NOT exceed this limit

STRICT CONTENT:

- Only offer: replacement or refund
- Do NOT introduce additional options (e.g., discounts)

STRICT INTERACTION:

- Do NOT ask questions
- Do NOT request additional details from the customer

STRICT OUTPUT:

- Do NOT include line breaks or new paragraphs
- Do NOT format as an email

STRICT SENTENCE CONTROL:
- Do NOT use semicolons
- Do NOT combine multiple ideas in one sentence
- Each sentence must contain only one idea

STRICT ACTION STRUCTURE:
- Keep acknowledgment, resolution, and next step in separate sentences
- Do NOT use "and" to combine actions

STRICT SAFETY:
- Do NOT use words like:
  "immediately", "instantly", "right away"
- Replace with:
  "as quickly as possible"

  STRICT INTERACTION:
- Do NOT ask the customer to choose or respond
- Do NOT use phrases like:
  "let us know"
  "which option you prefer"
- Always provide a direct next step instead (e.g., "please contact our support team")

CHOICE CONTROL:
- Do NOT reference customer choice indirectly
- Do NOT use phrases like:
  "preferred option"
  "option you prefer"
- Always present resolution neutrally without requiring a decision\

STRICT RESOLUTION FRAMING:
- Do NOT ask or imply the customer must choose
- Do NOT use phrases like:
  "preferred option"
  "option you prefer"
  "choose"
- Present the resolution as a fixed offering without requiring a decision

NEXT STEP RULE:
- The final sentence must ONLY direct the user to contact support
- Do NOT include resolution logic in the same sentence
    """

    response = llm.invoke(prompt)
    return {'response': response}