import json
import os
from datetime import datetime
from agents.parser_agent import ParserAgent
from agents.bug_finder_agent import BugFinderAgent
from agents.refactor_agent import RefactorAgent


class Orchestrator:
    """Coordinates multiple agents to perform a complete, multi-step review."""

    def __init__(self, code_path):
        self.code_path = code_path
        self.parser_agent = ParserAgent()
        self.bug_finder_agent = BugFinderAgent()
        self.refactor_agent = RefactorAgent()

    def run(self):
        print("🚀 Starting enhanced code review workflow...\n")

        # Step 1: Parse the code
        print("🔹 Step 1: Parsing the code...")
        structure = self.parser_agent.run(self.code_path)

        # Step 2: Bug analysis
        print("\n🔹 Step 2: Running bug finder...")
        bug_report = self.bug_finder_agent.run(self.code_path)

        # Step 3: Refactor the code
        print("\n🔹 Step 3: Auto-refactoring...")
        refactored_path = self.refactor_agent.run(self.code_path)

        # Combine everything
        report = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "file_analyzed": self.code_path,
            "parsed_structure": str(structure),
            "issues_found": bug_report,
            "refactored_file": refactored_path
        }

        # Step 4: Save structured JSON report
        os.makedirs("reports", exist_ok=True)
        report_file = f"reports/review_report_{datetime.now().strftime('%H%M%S')}.json"
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)
        print(f"\n📄 JSON report saved to: {report_file}")

        # Step 5: Also save a readable Markdown summary
        md_file = report_file.replace(".json", ".md")
        with open(md_file, "w", encoding="utf-8") as f:
            f.write("# 🧠 Code Review Summary\n\n")
            f.write(f"**File analyzed:** `{self.code_path}`\n")
            f.write(f"**Refactored output:** `{refactored_path}`\n")
            f.write(f"**Timestamp:** {report['timestamp']}\n\n")
            f.write("## 🪲 Issues Found:\n")
            for issue in bug_report:
                f.write(f"- **{issue['symbol']}** (line {issue['line']}): {issue['message']}\n")
            f.write("\n✅ Refactored file created successfully.\n")

        print(f"📝 Markdown summary saved to: {md_file}")
        print("\n🎉 All steps completed successfully!")

        return report


if __name__ == "__main__":
    code_file = "test_files/test_code.py"
    orchestrator = Orchestrator(code_file)
    orchestrator.run()
