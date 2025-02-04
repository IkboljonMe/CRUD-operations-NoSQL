from mongodb_connection import execute_query

query = {"name": "John Doe"}
update = {"age": 35}

result = execute_query("update", query=query, update=update)
print("Updated Document:", result)
