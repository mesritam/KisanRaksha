from dataclasses import dataclass
import re

@dataclass
class AutomationResult:
    intent: str
    action: str
    response: str

def automate(task: str) -> AutomationResult:
    text = task.strip()
    lower = text.lower()
    if not text:
        return AutomationResult("unknown", "ask", "Please provide a task.")
    if any(word in lower for word in ["summarize", "summary", "shorten"]):
        cleaned = re.sub(r"\s+", " ", text)
        summary = cleaned[:240] + ("..." if len(cleaned) > 240 else "")
        return AutomationResult("summarize", "generate_summary", summary)
    if any(word in lower for word in ["email", "mail", "message"]):
        return AutomationResult("communication", "draft_message", f"Draft a professional message for: {text}")
    if any(word in lower for word in ["remind", "reminder", "schedule"]):
        return AutomationResult("productivity", "create_reminder", f"Reminder requested: {text}")
    return AutomationResult("general", "analyze", f"Automation received: {text}")
