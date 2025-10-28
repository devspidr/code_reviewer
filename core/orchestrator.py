import os
import json
import datetime
from core.reviewer_agent import ReviewerAgent  # Make sure this file exists


class Orchestrator:
    """Coordinates the full code review workflow."""

    def __init__(self, code_path):
        self.code_path = code_path
        self.report_dir = "reports"
        os.makedirs(self.report_dir, exist_ok=True)

    def run(self):
        """Runs the complete AI Code Review process."""
        # Step 1: Run the reviewer agent
        agent = ReviewerAgent(self.code_path)
        review_results = agent.run_review()

        # Step 2: Generate refactored code file
        refactored_path = self._generate_refactored_code(review_results)

        # Step 3: Save the final report
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = os.path.join(self.report_dir, f"report_{timestamp}.json")

        report_data = {
            "timestamp": timestamp,
            "file": self.code_path,
            "issues_found": review_results.get("issues_found", []),
            "quality_score": review_results.get("quality_score", 0),
            "summary": review_results.get("summary", ""),
            "refactor_suggestions": refactored_path,
        }

        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=4)

        print(f"✅ Review complete — Report saved at {report_path}")
        return report_path

    def _generate_refactored_code(self, review_results):
        """Saves the corrected/refactored code to a file."""
        refactored_dir = "temp_refactored"
        os.makedirs(refactored_dir, exist_ok=True)

        refactored_path = os.path.join(
            refactored_dir,
            os.path.basename(self.code_path).replace(".py", "_refactored.py")
        )

        # If a corrected version is available
        if "refactored_code" in review_results and review_results["refactored_code"]:
            corrected_code = review_results["refactored_code"]
        else:
            # Fall back to original code
            with open(self.code_path, "r", encoding="utf-8") as f:
                corrected_code = f.read()

        with open(refactored_path, "w", encoding="utf-8") as f:
            f.write(corrected_code)

        return refactored_path
