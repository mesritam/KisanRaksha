# AI Automation API

Portfolio project using Python, FastAPI, Docker, GitHub Actions, and Jenkins.

## Features

- REST API for natural-language automation tasks
- Task intent classification
- Automation action routing
- Automated tests
- Docker containerization
- GitHub Actions CI
- Jenkins pipeline

## API

POST /automate

Request:
{
  "task": "summarize this project for me"
}

Response:
{
  "intent": "summarize",
  "action": "generate_summary",
  "response": "summarize this project for me"
}

## Run locally

python -m venv .venv
pip install -r requirements.txt
uvicorn backend.main:app --reload

Open http://127.0.0.1:8000/docs

## Tests

pytest -q

## Docker

docker build -t ai-automation-api .
docker run -p 8000:8000 ai-automation-api

## CI/CD

GitHub Actions runs dependency installation, tests, and Docker build on pushes and pull requests to main. Jenkins provides an alternative pipeline.

## Production roadmap

- LLM provider integration
- PostgreSQL
- Authentication
- Redis/Celery background jobs
- Logging and monitoring
- Google Cloud deployment
