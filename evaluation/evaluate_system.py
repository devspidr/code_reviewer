import os
import json
from datetime import datetime
from core.orchestrator import Orchestrator

def evaluate_all_tests():
    """Run orchestrator on multiple test files and summarize results."""
    test_dir = "test_files"
    files = [f for f in os.listdir(test_dir) if f.endswith(".py")]
    results = []

    if not files:
        print("❌ No test files found in test_files/ directory.")
        return

    print(f"🧪 Running evaluation on {len(files)} test files...\n")

    for file in files:
        file_path = os.path.join(test_dir, file)
        print(f"⚙️  Evaluating {file} ...")

        orchestrator = Orchestrator(file_path)
        report = orchestrator.run()
        results.append({
            "file": file,
            "issues_found": len(report["issues"]) if report["issues"] else 0
        })

    summary_path = f"reports/eval_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    print("\n✅ Evaluation Complete!")
    print(f"📄 Summary saved at: {summary_path}")
    print(json.dumps(results, indent=4))


if __name__ == "__main__":
    evaluate_all_tests()
