from mongodb_connection import execute_query

query = {"name": "John Doe"}

result = execute_query("read", query=query)
print("Retrieved Document:", result)
