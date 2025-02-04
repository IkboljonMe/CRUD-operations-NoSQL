from mongodb_connection import execute_query

query = {"name": "John Doe", "age": 30}

result = execute_query("create", query=query)
print("Document Created:", result)
