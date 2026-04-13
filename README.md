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
## THIS IS THE 2ND PROCESS YOU CAN DO THIS ALSO


# 🤖 Autonomous AI Agent (Free Gemini Edition)

A lightweight, fully functional autonomous AI agent built in Python. This project demonstrates the core concepts of agentic workflows, including autonomous decision-making, tool-calling, and reasoning loops.

**Note:** This repository follows an alternative process utilizing the **Google Gemini API**, which is incredibly fast and completely free to set up!

## ✨ Features
* **Autonomy:** Unlike reactive chatbots, this agent takes a goal, determines the necessary steps, and acts on them.
* **Tool Integration:** Equipped with custom Python functions that the AI can trigger on its own:
  * 🧮 **Calculator:** Evaluates mathematical expressions accurately.
  * 🌐 **Web Search:** Simulates retrieving real-time data from the web.
* **Continuous Loop:** Utilizes an agentic loop to assess if a goal is met or if further tool execution is required.

---

## 🚀 The Setup Process

Follow these steps to get your own version of this agent running locally in minutes.

### Step 1: Get Your Free Gemini API Key
1. Go directly to [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Sign in with your standard Google/Gmail account.
3. Click the **Create API key** button at the top left.
4. Click the blue button that says **Create API key in new project**.
5. Copy the generated long string of letters and numbers. That is your API key!

### Step 2: Install the SDK
Open your terminal and install the Google Generative AI Python library:
```bash
pip install google-generativeai
```

### Step 3: Set Your Environment Variable
Tell your terminal what your API key is so the code can use it securely. Replace `"your-copied-key-goes-here"` with the key you copied in Step 1.
* **Windows (PowerShell):** `$env:GEMINI_API_KEY="your-copied-key-goes-here"`
* **Windows (Command Prompt):** `set GEMINI_API_KEY="your-copied-key-goes-here"`
* **Mac/Linux:** `export GEMINI_API_KEY="your-copied-key-goes-here"`

### Step 4: Grab the Code
You do not need to write the brain from scratch. Simply download or clone the **`agent.py`** file directly from this repository. It contains the fully configured agent loop, the tool definitions, and the model configuration.

### Step 5: Run It
In the same terminal where you set your API key, run the script:
```bash
python agent.py
```
Wait for the initialization message, then give it a goal like: *"What is 15 percent of 847 and is that a normal tip amount?"* Watch the terminal to see the agent think, execute tools autonomously, and deliver a final synthesized answer!

## 👨‍💻 Author
Built by Imran.
```
