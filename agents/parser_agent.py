# agents/parser_agent.py
import ast
from core.base_agent import BaseAgent


class ParserAgent(BaseAgent):
    """Agent that parses a Python file into an AST."""

    def run(self, code_path: str):
        """Parse the given Python file and print its structure."""
        try:
            with open(code_path, "r", encoding="utf-8") as f:
                code = f.read()

            tree = ast.parse(code)
            print(f"[ParserAgent] Successfully parsed: {code_path}")
            print(ast.dump(tree, indent=4))

        except FileNotFoundError:
            print(f"Error in ParserAgent: File not found: {code_path}")
        except SyntaxError as e:
            print(f"Error in ParserAgent: Syntax error - {e}")
        except Exception as e:
            print(f"Error in ParserAgent: {e}")
