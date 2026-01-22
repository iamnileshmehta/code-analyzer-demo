# main.py
from analyzer import analyze_path
from rag_pipe import index_knowledge_objects
from translation_flow import run_translation
from rag.summarizer import summarize_function

path = input("Enter ERPNext file or directory path: ")

# print("1. Get code entities \n" \
# "2. Get Code Explanation\n" \
# "3. Get translated code")

# choose = input("Choose the options: ")



knowledge_objects = analyze_path(path)


vector_store = index_knowledge_objects(knowledge_objects)


run_translation(vector_store)
