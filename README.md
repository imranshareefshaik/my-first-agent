# 🤖 Autonomous AI Agent

A lightweight, fully functional autonomous AI agent built in Python using the Google Gemini API. This project demonstrates the core concepts of agentic workflows, including autonomous decision-making, tool-calling, and reasoning loops.

## ✨ Features
* **Autonomy:** Unlike reactive chatbots, this agent takes a goal, determines the necessary steps, and acts on them.
* **Tool Integration:** Equipped with custom Python functions that the AI can trigger on its own:
  * 🧮 **Calculator:** Evaluates mathematical expressions accurately.
  * 🌐 **Web Search:** Simulates retrieving real-time data from the web.
* **Continuous Loop:** Utilizes an agentic loop to assess if a goal is met or if further tool execution is required.

## 🚀 How It Works
1. The user provides a natural language prompt or goal.
2. The agent's "brain" (Gemini 2.5 Flash) processes the request.
3. If the agent realizes it needs outside information or calculations, it autonomously selects the correct tool from its toolkit.
4. The Python script executes the tool and feeds the result back to the agent.
5. The agent synthesizes the tool outputs into a final, intelligent response.

## 💻 Installation & Setup

**1. Clone the repository:**
```bash
git clone https://github.com/imranshareefshaik/my-first-agent.git
cd my-first-agent
