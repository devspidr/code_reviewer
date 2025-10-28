# agents/bug_finder_agent.py
import subprocess
from core.base_agent import BaseAgent


class BugFinderAgent(BaseAgent):
    """Agent that finds bugs or code issues using pylint."""

    def run(self, code_path: str):
        """Run pylint static analysis on the given file."""
        try:
            print(f"[BugFinderAgent] Running static analysis on: {code_path}")
            # Run pylint on the target file
            result = subprocess.run(
                ["pylint", code_path, "--output-format=json"],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                print("[BugFinderAgent] No major issues found.")
                return []

            elif result.stdout.strip():
                # Try to parse JSON output if possible
                try:
                    import json
                    issues = json.loads(result.stdout)
                    print(f"[BugFinderAgent] Found {len(issues)} issues.")
                    return issues
                except json.JSONDecodeError:
                    print("[BugFinderAgent] Could not parse pylint output as JSON.")
                    print(result.stdout)
                    return []

            else:
                print("[BugFinderAgent] pylint returned no output.")
                return []

        except FileNotFoundError:
            print("Error: pylint is not installed or not found in PATH.")
            return []
        except Exception as e:
            print(f"Error in BugFinderAgent: {e}")
            return []
