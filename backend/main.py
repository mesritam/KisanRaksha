from fastapi import FastAPI
from pydantic import BaseModel, Field
from backend.automation import automate

app = FastAPI(title="AI Automation API", version="1.0.0", description="Task classification and automation workflow API.")

class AutomationRequest(BaseModel):
    task: str = Field(..., min_length=1, max_length=2000)

@app.get("/")
def root():
    return {"name": "AI Automation API", "version": "1.0.0", "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/automate")
def run_automation(request: AutomationRequest):
    result = automate(request.task)
    return {"intent": result.intent, "action": result.action, "response": result.response}
