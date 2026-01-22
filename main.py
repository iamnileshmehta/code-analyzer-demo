# main.py
from analyzer import analyze_path
from rag_pipe import index_knowledge_objects
from translation_flow import run_translation

path = input("Enter ERPNext file or directory path: ")

knowledge_objects = analyze_path(path)

vector_store = index_knowledge_objects(knowledge_objects)

run_translation(vector_store)
