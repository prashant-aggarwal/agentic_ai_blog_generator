# Agentic Blog Creator

This is a modular Python project that uses [CrewAI](https://docs.crewai.com/) and Amazon Bedrock via environment-based configuration to generate AI-powered blog posts. It applies agent-based reasoning for task-specific responsibilities such as research, summarization, and blog writing.

---

## 🚀 Features

- **Agent-based architecture** using CrewAI
- **LLM-powered pipeline** via Amazon Bedrock models (e.g., Amazon Nova, Claude v2)
- **Modular & OOP structure**
- **YAML-driven configuration** for agents and tasks
- Outputs blog content in Markdown format

---

## 📁 Project Structure

```
agentic_ai_blog_generator/
├── crew_config/
│   ├── agents.yaml        # Defines agent roles and goals
│   └── tasks.yaml         # Defines tasks linked to agents
├── modules/
│   ├── agent_task_builder.py  # Loads agents/tasks from YAML
│   ├── crew_executor.py       # Orchestrates CrewAI workflow
│   └── llm_initializer.py     # Initializes Bedrock LLM
├── main.py              # Main execution file
├── .env                 # Environment configuration (MODEL_ID, REGION)
├── requirements.txt     # Python dependencies
└── blog_output.md       # Output blog file (generated)
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/prashant-aggarwal/agentic_ai_blog_generator.git
cd agentic_ai_blog_generator
```

### 2. Create `.env` file in the root directory

```env
MODEL_ID=<Desired model id> e.g. anthropic.claude-v2
AWS_REGION_NAME=<Desired region> e.g. us-east-1
AWS_ACCESS_KEY_ID=<AWS access key of your AWS account with necessary permissions>
AWS_SECRET_ACCESS_KEY=<AWS secret ccess Key Id your AWS account with necessary permissions>
```

> ⚠️ Make sure the selected model is available in your AWS Bedrock account.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python main.py
```

The result will be saved to `blog_output.md`.

---

## 📦 Requirements

- Python 3.10+
- AWS credentials with access to Amazon Bedrock
- Bedrock model (Amazon Nova, Claude, LLaMA2, etc.) enabled
- Internet access (for API calls)

---
