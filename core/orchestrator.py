import os
import logging
from datetime import datetime
from agents.parser_agent import ParserAgent
from agents.bug_finder_agent import BugFinderAgent
from agents.refactor_agent import RefactorAgent
from agents.reviewer_agent import ReviewerAgent

# === Setup Logging ===
os.makedirs("logs", exist_ok=True)
log_file = os.path.join("logs", "run_log.txt")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# Optional: also print logs to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)


class Orchestrator:
    """Coordinates multiple agents to perform sequential code analysis and review."""

    def __init__(self, code_path):
        self.code_path = code_path
        self.parser_agent = ParserAgent()
        self.bug_finder_agent = BugFinderAgent()
        self.refactor_agent = RefactorAgent()
        self.reviewer_agent = ReviewerAgent()

    def run(self):
        run_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"===== Code Review Run Started at {run_time} =====")

        print("🚀 Starting multi-agent code review workflow...\n")

        try:
            # Step 1: Parsing
            print("🔹 Step 1: Parsing code...")
            structure = self.parser_agent.run(self.code_path)
            logging.info("ParserAgent completed successfully.")

            # Step 2: Bug analysis
            print("\n🔹 Step 2: Running bug analysis...")
            bug_report = self.bug_finder_agent.run(self.code_path)
            logging.info(f"BugFinderAgent found {len(bug_report)} issues.")

            # Step 3: Refactor suggestions
            print("\n🔹 Step 3: Refactoring suggestions...")
            refactor_suggestions = self.refactor_agent.run(self.code_path)
            logging.info("RefactorAgent generated suggestions.")

            # Step 4: Combine & save report
            combined_report = {
                "timestamp": run_time,
                "file": self.code_path,
                "structure": structure,
                "issues": bug_report,
                "refactor_suggestions": refactor_suggestions,
            }

            report_path = f"reports/final_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(report_path, "w", encoding="utf-8") as f:
                json.dump(combined_report, f, indent=4)
            logging.info(f"Saved report: {report_path}")

            # Step 5: Final Review
            print("\n🔹 Step 4: Running final code review...")
            final_review = self.reviewer_agent.run(report_path)
            logging.info("ReviewerAgent completed successfully.")

            print("\n✅ Final Code Review Summary:")
            print(json.dumps(final_review, indent=4))

            logging.info("===== Code Review Run Completed Successfully =====\n")

        except Exception as e:
            logging.error(f"Error occurred: {e}")
            print(f"❌ An error occurred during execution: {e}")

if __name__ == "__main__":
    logging.info("===== Code Review Run Started =====")

    parser = ParserAgent()
logging.info("ParserAgent started.")
structure = parser.run("test_files/test_code.py")
logging.info("ParserAgent completed successfully.")

bugfinder = BugFinderAgent()
logging.info("BugFinderAgent started.")
issues = bugfinder.run("test_files/test_code.py")
logging.info(f"BugFinderAgent found {len(issues)} issues.")

refactor = RefactorAgent()
logging.info("RefactorAgent started.")
suggestions = refactor.run("test_files/test_code.py")
logging.info("RefactorAgent completed successfully.")

reviewer = ReviewerAgent()
logging.info("ReviewerAgent started.")
final_report = reviewer.run("test_files/test_code.py")
logging.info("ReviewerAgent completed successfully.")
