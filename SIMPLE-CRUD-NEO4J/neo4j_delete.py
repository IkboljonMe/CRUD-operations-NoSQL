from neo4j_connector import execute_query
import time

# *** DEFINE QUERY TO REMOVE USER NODE ***
remove_user_query = """
MATCH (u:User {full_name: 'Alice Smith'})
DELETE u
"""

# *** MEASURE EXECUTION TIME ***
start_time = time.time()
execute_query(remove_user_query)
end_time = time.time()

# *** PRINT DELETION RESULT ***
print("USER NODE REMOVED.")
print("EXECUTION TIME:", end_time - start_time, "SECONDS")
