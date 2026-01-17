## Code intelligence and modernization platform (Python AST + RAG)
<br>
<hr>

# Overview

<br>
This project is a static Python code analyzer and modernization assistant built using Python’s built-in AST (Abstract Syntax Tree) module.
<br>
It analyzes Python source code without executing it, extracts structural knowledge, builds call relationships, and enables:
<hr>

# Code understanding

- Call graph extraction<br>
- Knowledge indexing (RAG)<br>
- Legacy code translation to modern languages (TypeScript, Java, C++, etc.)<br>

The system is designed with clean modular architecture, inspired by real-world static analysis and compiler pipelines.
<hr>

# Core Capabilities

🔍 Static Code Analysis (AST-based)
<br>
The analyzer extracts:
<br>
✅ Functions (name, signature, source code)<br>
✅ Classes<br>
✅ Imports<br>
✅ Function call relationships (who calls whom)<br>
✅ File-level metadata<br>

This enables:
- Dependency understanding
- Impact analysis
- Visualization (Mermaid-ready)
- 🧠 Knowledge Layer (RAG-ready)

Extracted entities are converted into Knowledge Objects containing:
- Name
- Type (function / class)
- Source code
- Summary
- Relationships
- File path

These objects are:
- Embedded
- Stored in a vector store
- Retrieved via semantic queries

<hr>

# 🔁 Legacy Code Translation (LLM-powered)

The system supports language translation of legacy Python code, using retrieved context.

Example:

- Python → TypeScript
- Python → Java
- Python → C++
  
<hr>

# Design goals:

- Preserve business logic exactly
- Context-aware translation via RAG
- Each layer has single responsibility and can be extended independently.
 
<hr>

# Why AST (Not Regex or Execution)?

<br>Using Python AST allows the analyzer to:

✔ Reliably inspect real code structure

✔ Understand function boundaries and calls

✔ Avoid running untrusted or unsafe code

✔ Scale to large codebases (ERPNext, Django, etc.)

<hr>

# Usage

Analyze a single file
```
python analyzer.py sample.py
```
Analyze a real codebase (example: ERPNext)
```
git clone https://github.com/frappe/erpnext
python analyzer.py erpnext/accounts/doctype/sales_invoice
```
<hr>

# Extensibility Ideas

📈 Mermaid call graph visualization

🧾 Docstring-based business logic extraction

🧠 Cross-file dependency resolution

🔍 Dead code detection

🏗️ Large-scale monorepo indexing

🔁 Multi-language reverse translation
<hr>

# Disclaimer
<br>
This project focuses on structural analysis, not runtime behavior.

Dynamic features (reflection, monkey-patching) are not evaluated.


