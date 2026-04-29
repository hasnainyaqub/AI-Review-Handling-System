# 🤖 AI Review Handling System

A production-grade, multi-agent AI system built with **FastAPI**, **LangGraph**, and **Groq LLM** that intelligently handles customer reviews. The system classifies review sentiment, diagnoses issues in negative reviews, and generates tailored, empathetic responses — all powered by a structured LangGraph state machine.

---

## 🧠 How It Works

```
Customer Review (POST /agent)
        │
        ▼
┌───────────────────┐
│  sentiment_find   │  ← Classify: positive / negative
└───────────────────┘
        │
   ┌────┴────┐
   ▼         ▼
positive   negative
   │         │
   ▼         ▼
┌──────┐  ┌──────────────┐
│ warm │  │ run_diagnoses│ ← Extract issue_type, tone, urgency
│ thank│  └──────────────┘
│ -you │         │
└──────┘         ▼
            ┌─────────────────┐
            │ negative_response│ ← Generate empathetic resolution
            └─────────────────┘
```

---

## 🚀 Features

- **Sentiment Analysis** — Automatically detects positive or negative customer sentiment
- **Issue Diagnosis** — Extracts issue type (Product Quality, Shipping, etc.), tone, and urgency for negative reviews
- **Response Generation** — Generates context-aware, empathetic response messages following strict content policies
- **REST API** — Clean FastAPI endpoints, ready for integration
- **LangGraph Workflow** — Fully modular, stateful multi-agent pipeline

---

## 📁 Project Structure

```
AI_Review_Handling_System/
├── main.py                        # FastAPI app entry point
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker image definition
├── docker-compose.yml             # Multi-container orchestration
├── .env                           # Environment variables (not committed)
│
├── api/
│   └── routes.py                  # API route definitions
│
├── core/
│   ├── config.py                  # App configuration (API keys, model name)
│   └── llm.py                     # Groq LLM + structured output initialization
│
├── graph/
│   ├── builder.py                 # LangGraph state machine builder
│   ├── executor.py                # Graph invocation entry point
│   ├── state.py                   # ReviewInputState TypedDict
│   ├── nodes/
│   │   ├── sentiment.py           # Node: classify sentiment
│   │   ├── diagnoses.py           # Node: diagnose issue from negative review
│   │   ├── positive.py            # Node: generate positive response
│   │   └── negative.py            # Node: generate negative/empathetic response
│   └── edges/
│       └── conditional.py         # Conditional edge: route by sentiment
│
├── schema/
│   ├── agent_request_schema.py    # Pydantic model for incoming API request
│   ├── agent_schema.py            # Pydantic model for sentiment output
│   └── diagnoses_schema.py        # Pydantic model for diagnoses output
│
└── services/
    └── agent_service.py           # Service layer bridging API and graph
```

---

## ⚙️ Prerequisites

- Python 3.11+
- A [Groq API Key](https://console.groq.com/)
- Docker & Docker Compose (for containerized deployment)

---

## 🛠️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/hasnainyaqub/AI-Review-Handling-System.git
cd AI_Review_Handling_System
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
# venv\Scripts\activate       # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the application

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at **http://localhost:8000**.

---

## 🐳 Docker Deployment

### Using Docker Compose (Recommended)

```bash
# Build and start
docker compose up --build

# Run in background
docker compose up --build -d

# Stop
docker compose down
```

### Using Docker directly

```bash
# Build image
docker build -t ai-review-system .

# Run container
docker run -p 8000:8000 --env-file .env ai-review-system
```

---

## 📡 API Reference

### `GET /`
Health check — confirms the API is running.

**Response:**
```json
{ "message": "Welcome to the Review Handling System API!" }
```

---

### `GET /health`
Service health check.

**Response:**
```json
{ "status": "ok" }
```

---

### `POST /agent`
Submit a customer review and receive an AI-generated response.

**Request Body:**
```json
{
  "review_text": "The product stopped working after two days. Very disappointed."
}
```

**Response (Negative Review):**
```json
{
  "result": {
    "response": "We sincerely apologize for the inconvenience you experienced. We understand how frustrating it is when a product does not meet expectations. Please contact our support team as quickly as possible so we can arrange a replacement or refund for you."
  }
}
```

**Response (Positive Review):**
```json
{
  "result": {
    "response": "Thank you so much for your kind words! We're thrilled to hear you had a great experience and truly appreciate your support."
  }
}
```

---

## 🔍 Interactive API Docs

Once running, visit:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🧩 Tech Stack

| Component | Technology |
|-----------|-----------|
| Web Framework | FastAPI |
| ASGI Server | Uvicorn |
| LLM Provider | Groq (via `langchain-groq`) |
| Agent Workflow | LangGraph |
| Schema Validation | Pydantic v2 |
| Config Management | python-dotenv |
| Containerization | Docker + Docker Compose |

---

## 👨‍💻 Developer

**Hasnain Yaqoob**  
[hasnainyaqoob.site](https://hasnainyaqoob.site)
