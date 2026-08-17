# TaskFlow AI Product Manager

TaskFlow AI Product Manager is a multi-agent AI system developed for the Summer School '26 OpenAI Agents SDK Capstone Project.

The system assists with product management activities including customer feedback analysis, product analytics, competitor research, feature prioritisation, PRD generation and sprint planning.

## Key Features

- Multi-agent product management architecture
- Central Product Orchestrator Agent
- Six specialised AI agents
- Agent handoffs
- Customer feedback analysis
- Product analytics
- Competitor and market research
- RICE-based feature prioritisation
- Human-in-the-loop approval
- Automated PRD generation
- Capacity-aware sprint planning
- Persistent SQLite conversation memory
- Internal knowledge retrieval
- Structured Pydantic outputs
- Error handling and logging

## Multi-Agent Architecture

The system contains seven agents:

1. Product Orchestrator Agent
2. Feedback Analysis Agent
3. Product Analytics Agent
4. Competitor Research Agent
5. Feature Prioritisation Agent
6. PRD Writer Agent
7. Sprint Planner Agent

The Product Orchestrator receives user requests and hands them off to the appropriate specialist.

## End-to-End Workflow

```text
Customer Feedback
       ↓
Product Analytics
       ↓
Competitor Research
       ↓
Feature Prioritisation
       ↓
Human Approval
       ↓
PRD Generation
       ↓
Sprint Planning
       ↓
Final Product Plan
```

## Technology Stack

- Python
- OpenAI Agents SDK
- Gemini 3.5 Flash Lite
- LiteLLM
- Pydantic
- Pandas
- Tavily Search API
- SQLite
- Python Logging

## Installation

Clone the repository:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd TaskFlow-AI-Product-Manager
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
OPENAI_AGENTS_DISABLE_TRACING=1
```

Do not commit the `.env` file to GitHub.

## Running the Application

For the conversational AI Product Manager:

```bash
python app.py
```

For the complete end-to-end workflow:

```bash
python end_to_end_demo.py
```

## Human-in-the-Loop Approval

Important product roadmap decisions require Product Manager approval.

The workflow pauses after feature prioritisation and allows the Product Manager to approve or reject the recommendation before downstream planning continues.

## Persistent Memory

SQLite session storage allows TaskFlow to maintain conversational context across interactions and application restarts.

## Knowledge Retrieval

The internal knowledge base contains information about:

- Product strategy
- Customer personas
- Company goals
- Engineering architecture
- Product policies

Relevant agents can retrieve this information when making product recommendations.

## Example Result

During the end-to-end demonstration, TaskFlow identified onboarding and workspace setup as a major product issue.

The Feature Prioritisation Agent selected **Improve Onboarding** as the highest-priority initiative.

Following human approval, the system generated a PRD and converted it into a two-sprint development plan containing 15 total story points.

## Project Structure

```text
agent_modules/       AI agent definitions
config/              Application/model configuration
data/                TaskFlow product datasets
knowledge_base/      Internal product knowledge
models/              Pydantic structured-output models
tools/               Agent tools and API integrations
workflows/           End-to-end workflow
utils/               Logging and output utilities
tests/               Application tests
app.py               Conversational application
end_to_end_demo.py   Complete workflow demonstration
```

## Security

API credentials are stored using environment variables and are excluded from version control through `.gitignore`.

## Capstone Requirements

| Requirement | Implementation |
|---|---|
| 5+ specialised agents | 7 agents |
| 5+ tools/APIs | Implemented |
| Agent handoffs | Implemented |
| Memory/context management | SQLite sessions |
| Structured outputs | Pydantic |
| Human approval | Implemented |
| RAG / knowledge retrieval | Implemented |
| Session persistence | Implemented |
| Error handling/logging | Implemented |

## Disclaimer

TaskFlow is a demonstration product environment created for this capstone project. AI-generated recommendations are intended to support product decision-making and remain subject to human review.
