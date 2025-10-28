# core/orchestrator.py
from typing import List, Dict

class BaseAgent:
    """Base class for all agents."""
    def __init__(self, name: str):
        self.name = name

    def process(self, data: Dict) -> Dict:
        """Override in child classes."""
        raise NotImplementedError(f"{self.name} must implement process() method.")


class Orchestrator:
    """Main controller to coordinate agent interactions."""
    def __init__(self, agents: List[BaseAgent]):
        self.agents = agents

    def run(self, input_data: Dict) -> Dict:
        """Run all agents sequentially and pass data through the pipeline."""
        data = input_data
        print("\n🚀 Starting Orchestration Pipeline...\n")

        for agent in self.agents:
            print(f"🤖 Running agent: {agent.name}")
            try:
                data = agent.process(data)
            except Exception as e:
                print(f"⚠️ Error in {agent.name}: {e}")
            print(f"✅ Finished: {agent.name}\n")

        print("🎯 Pipeline complete!")
        return data
