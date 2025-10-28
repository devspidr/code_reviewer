# app.py
from agents.parser_agent import ParserAgent
from core.orchestrator import Orchestrator

if __name__ == "__main__":
    # Initialize agents
    parser_agent = ParserAgent()
    agents = [parser_agent]

    # Create orchestrator
    orchestrator = Orchestrator(agents)

    # Sample code input
    input_data = {
        "code": """
def hello():
    print("Hello, world!")

class MyClass:
    pass
"""
    }

    # Run the pipeline
    orchestrator.run(input_data)
