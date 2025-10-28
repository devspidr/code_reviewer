# small helper to run pylint programmatically if needed
import subprocess, sys

def run_pylint(path):
    result = subprocess.run([sys.executable, "-m", "pylint", path], capture_output=True, text=True)
    return result.stdout
import subprocess
import json
from pathlib import Path

def analyze_code_with_pylint(file_path: str):
    """
    Run Pylint on the given Python file and return structured JSON results.
    """
    try:
        # Run pylint as a subprocess to analyze the file
        result = subprocess.run(
            ["pylint", file_path, "-f", "json"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Parse pylint’s JSON output
        if result.stdout.strip():
            pylint_output = json.loads(result.stdout)
        else:
            pylint_output = []

        # Simplify and structure the output
        issues = []
        for item in pylint_output:
            issues.append({
                "type": item.get("type"),      # error, warning, convention, etc.
                "message": item.get("message"), # description of the problem
                "symbol": item.get("symbol"),   # short name of the rule violated
                "line": item.get("line"),       # line number where it occurred
                "path": item.get("path")        # file name
            })

        return issues

    except Exception as e:
        return [{"error": str(e)}]


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m static_analysis.run_pylint <path_to_python_file>")
    else:
        file_path = sys.argv[1]
        issues = analyze_code_with_pylint(file_path)
        print(issues)
