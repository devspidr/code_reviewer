class ReviewerAgent:
    """A mock reviewer that simulates static analysis."""

    def __init__(self, code_path):
        self.code_path = code_path

    def run_review(self):
        with open(self.code_path, "r", encoding="utf-8") as f:
            code = f.read()

        # Simulated issues (in a real app, you'd integrate pylint or GPT model)
        issues = [
            {"type": "convention", "message": "Missing module docstring"},
            {"type": "warning", "message": "Unused import detected"},
        ]

        # Fake refactor: adds a docstring at the top
        refactored_code = '"""\nAuto-refactored version\n"""\n\n' + code

        return {
            "issues_found": issues,
            "quality_score": 90,
            "summary": "Code analyzed successfully with minor issues fixed.",
            "refactored_code": refactored_code
        }
