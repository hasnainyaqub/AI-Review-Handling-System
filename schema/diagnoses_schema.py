from typing_extensions import Literal
from pydantic import BaseModel, Field


class RunDiagnosesSchema(BaseModel):
    issue_type: Literal[
        "Product Quality",
        "Delivery/Shipping",
        "Customer Service",
        "Pricing",
        "Usability",
        "Other"
    ] = Field(description="""
    Classify the main problem into ONE of these categories:
    - Product Quality
    - Delivery/Shipping
    - Customer Service
    - Pricing
    - Usability
    - Other
    """)

    tone: Literal["angry", "frustrated", "disappointed", "neutral"] = Field(description= """
    Detect the emotional tone of the customer:
    - angry
    - frustrated
    - disappointed
    - neutral"""
    )
    urgency: Literal["high", "medium", "low"] = Field(description="""
    Estimate how urgent the issue is:
    - high (customer demands immediate action / very angry)
    - medium (clear dissatisfaction but not extreme)
    - low (mild complaint or vague issue)""")
