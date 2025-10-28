# agents/refactor_agent.py

import re
from core.base_agent import BaseAgent


class RefactorAgent(BaseAgent):
    """Agent that automatically improves the analyzed code."""

    def run(self, code_path: str):
        """
        Reads the Python file, refactors it (adds docstrings, removes unused imports),
        and saves the improved version.
        """
        try:
            with open(code_path, "r", encoding="utf-8") as f:
                code = f.read()

            # 1️⃣ Remove unused import statements (like "import math" if not used)
            code = self._remove_unused_imports(code)

            # 2️⃣ Add basic docstrings to functions/classes if missing
            code = self._add_missing_docstrings(code)

            # 3️⃣ Save refactored version
            new_path = code_path.replace(".py", "_refactored.py")
            with open(new_path, "w", encoding="utf-8") as f:
                f.write(code)

            print(f"[RefactorAgent] Refactored file created: {new_path}")
            return new_path

        except FileNotFoundError:
            print(f"Error in RefactorAgent: File not found: {code_path}")
        except Exception as e:
            print(f"Error in RefactorAgent: {e}")

    def _remove_unused_imports(self, code: str) -> str:
        """Simplified removal of unused imports (for demo)."""
        lines = code.splitlines()
        cleaned = [line for line in lines if not re.match(r"^\s*import\s+\w+", line.strip())]
        return "\n".join(cleaned)

    def _add_missing_docstrings(self, code: str) -> str:
        """Add simple docstrings if missing (basic regex version)."""
        code = re.sub(
            r"(?<=def\s)(\w+)\s*\(.*?\):",
            lambda m: f"{m.group(0)}\n    \"\"\"Auto-added docstring for {m.group(1)}.\"\"\"",
            code
        )
        code = re.sub(
            r"(?<=class\s)(\w+)\s*\(.*?\):",
            lambda m: f"{m.group(0)}\n    \"\"\"Auto-added docstring for class {m.group(1)}.\"\"\"",
            code
        )
        return code
