from neo4j_connection import execute_query
import time

query = """
MATCH (p:Person {name: 'John Doe'})
DELETE p
"""

start_time = time.time()
execute_query(query)
end_time = time.time()

print("Node deleted.")
print("Execution Time:", end_time - start_time, "seconds")
