import json
import os
import sys


def python_file_to_json(py_file_path, output_json):
    if not py_file_path.endswith(".py"):
        raise ValueError("Only Python files are supported")

    with open(py_file_path, "r", encoding="utf-8") as f:
        code = f.read()

    data = {
        "file_name": os.path.basename(py_file_path),
        "file_path": os.path.abspath(py_file_path),
        "language": "python",
        "code": code
    }

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Code converted to JSON: {output_json}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python code_to_json.py <file.py> <output.json>")
        sys.exit(1)

    python_file = sys.argv[1]
    output_json = sys.argv[2]

    python_file_to_json(python_file, output_json)
