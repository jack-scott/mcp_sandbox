from fastmcp import FastMCP
import random

# Create an MCP server
mcp = FastMCP("Random_greeting")

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    greetings = [
        "Hello",
        "Hi",
        "Hey",
        "Greetings",
        "Salutations",
        "Howdy",
        "Welcome",
        "What's up",
        "Good to see you",
    ]
    greeting = random.choice(greetings)
    if name:
        greeting += f", {name}!"
    else:
        greeting += "!"
    return greeting

if __name__ == "__main__":
    # Start the server
    mcp.run()
