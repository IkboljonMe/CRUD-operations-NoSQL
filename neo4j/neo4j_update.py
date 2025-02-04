from neo4j_connection import execute_query
import time

query = """
MATCH (p:Person {name: 'John Doe'})
SET p.age = 35
RETURN p.name AS name, p.age AS age
"""

start_time = time.time()
result = execute_query(query)
end_time = time.time()

print("Updated Node:", result)
print("Execution Time:", end_time - start_time, "seconds")
