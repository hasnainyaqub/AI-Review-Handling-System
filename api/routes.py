from fastapi import APIRouter, HTTPException
from schema.agent_request_schema import AgentRequest
from services.agent_service import run_agent

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/agent")
def run_agent_api(request: AgentRequest):
    try:
        result = run_agent(request.model_dump())
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))