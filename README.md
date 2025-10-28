# 🤖 Agentic Code Reviewer

An **AI-powered Agentic Code Review System** that automatically analyzes Python code, detects issues, suggests improvements, and even generates refactored (corrected) code.  
Built using **Python, Streamlit**, and an **Agent-Orchestrated AI pipeline**.

---

## 🚀 Features

- 📂 Upload Python files through a Streamlit interface  
- 🧠 Agentic orchestration to parse, analyze, and refactor code  
- 🔍 AI-based review to detect syntax, logic, and style issues  
- 🪄 Automatic code refactoring with improved readability and structure  
- 📊 Quality dashboard (issues, quality scores, improvement trends)  
- 💾 Saves results in structured JSON reports inside `/reports`

---

## 🧩 Project Architecture

User → Streamlit UI → Orchestrator → ParserAgent → ReviewerAgent → RefactorAgent → Report Generator → Streamlit Display


Each agent performs a specific role:
- **ParserAgent** → Understands and structures the uploaded code  
- **ReviewerAgent** → Analyzes issues, lint errors, and code quality  
- **RefactorAgent** → Suggests or auto-generates improved code  
- **Orchestrator** → Manages communication between all agents  

---

## 🖥️ Tech Stack

- **Python 3.10+**
- **Streamlit** — User interface  
- **Plotly / Altair** — Data visualization  
- **JSON / Logging / OS** — Data handling  
- **Static analysis tools or LLMs** — AI-based review logic  

---

🧠 How It Works

Upload your .py file

The Orchestrator triggers all agents

Agents parse, analyze, and refactor your code

A detailed report is generated and saved under /reports

The Streamlit app displays:

🧾 Original code

🪄 Refactored code

📊 Review summary and quality score

