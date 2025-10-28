# core/base_agent.py
import abc

class BaseAgent(abc.ABC):
    """Abstract base class for all AI agents."""

    @abc.abstractmethod
    def run(self, code_path: str):
        """Execute the agent’s main task."""
        pass
