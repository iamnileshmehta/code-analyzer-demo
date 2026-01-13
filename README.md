# code-analyzer

# Code Analyzer (Python AST)

## Overview
This project is a **simple Python code analyzer** built using Python’s built-in `ast` (Abstract Syntax Tree) module.  
The goal of this project is to **understand and analyze Python code structure programmatically**, rather than executing it.

The analyzer identifies:
- Functions
- Classes
- Imports
- Basic function call relationships

This project focuses on **clarity, explainability, and clean design**, making it easy to understand and extend.

---

## Why AST?
Instead of parsing code as plain text, this project uses Python’s AST to:
- Reliably inspect code structure
- Understand functions and calls safely
- Avoid execution of untrusted code

AST allows us to reason about *what the code contains*, not *what it does at runtime*.

---

## Project Structure

```
code-analyzer-demo/
│
├── analyze.py # Entry point that coordinates analysis
├── extractor.py # Extracts functions, classes, and imports
├── relationships.py # Analyzes function call relationships
├── output.py # Formats and prints results
├── example-output/ # Sample outputs
└── README.md
```

```bash
python analyze.py
```
