from mongodb_connection import execute_query

query = {"name": "John Doe"}

result = execute_query("delete", query=query)
print("Deleted Document:", result)
