# core/orchestrator.py
import json
from agents.parser_agent import ParserAgent
from agents.bug_finder_agent import BugFinderAgent

class Orchestrator:
    """Coordinates multiple agents to perform sequential analysis."""

    def __init__(self, code_path):
        self.code_path = code_path
        self.parser_agent = ParserAgent()
        self.bug_finder_agent = BugFinderAgent()

    def run(self):
        print("🚀 Starting multi-agent code review workflow...\n")

        # Step 1: Parse the code
        structure = self.parser_agent.run(self.code_path)

        # Step 2: Run bug analysis
        bug_report = self.bug_finder_agent.run(self.code_path)

        # Step 3: Combine both results
        combined_report = {
            "file": self.code_path,
            "structure": structure,
            "issues": bug_report
        }

        # Step 4: Pretty print result
        print("\n✅ Final Combined Report:")
        print(json.dumps(combined_report, indent=4))

        return combined_report


if __name__ == "__main__":
    code_file = "test_files/test_code.py"
    orchestrator = Orchestrator(code_file)
    orchestrator.run()
