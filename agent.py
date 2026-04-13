import google.generativeai as genai
import os

# ==========================================
# 1. DEFINE THE TOOLS
# ==========================================

def calculator(math_expression: str) -> str:
    """A simple calculator tool. Pass a math expression like '15 * 847 / 100'."""
    print(f"\n   [🛠️  Executing Tool] Calculator")
    print(f"   [📥 Input] {math_expression}")
    try:
        result = str(eval(math_expression))
        print(f"   [✅ Result] {result}")
        return result
    except Exception as e:
        return f"Error calculating: {e}"

def web_search(query: str) -> str:
    """A mock web search tool to find information."""
    print(f"\n   [🛠️  Executing Tool] Web Search")
    print(f"   [📥 Input] {query}")
    # This simulates a real API call
    mock_result = f"Search results for '{query}': 15% is a standard, albeit slightly low, tip amount for good service."
    print(f"   [✅ Result] {mock_result}")
    return mock_result

# ==========================================
# 2. CONFIGURE THE AGENT
# ==========================================

# Pulls the API key you set in your terminal
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY environment variable not found. Please set it in your terminal before running.")
    exit()

genai.configure(api_key=api_key)

# We initialize the model and hand it the tools it is allowed to use
agent = genai.GenerativeModel(
    model_name='gemini-2.5-flash',
    tools=[calculator, web_search]
)

# ==========================================
# 3. THE AGENTIC LOOP
# ==========================================

def run_agent():
    print("🤖 Agent initialized. Type 'exit' to quit.\n")
    
    # enable_automatic_function_calling handles the loop of sending 
    # the tool result back to the AI automatically!
    chat = agent.start_chat(enable_automatic_function_calling=True)
    
    while True:
        goal = input("\nYou: ")
        if goal.lower() == 'exit':
            break
            
        print("🤔 Agent is thinking and planning its steps...")
        
        # This single line triggers the autonomy. The model decides what to do.
        response = chat.send_message(goal)
        
        print(f"\n🎯 Final Answer:\n{response.text}")
        print("-" * 50)

if __name__ == "__main__":
    run_agent()