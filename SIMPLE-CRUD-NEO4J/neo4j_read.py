from neo4j_connector import execute_query
import time

# *** DEFINE QUERY TO RETRIEVE USER NODES ***
retrieve_users_query = """
MATCH (u:User) RETURN u.full_name AS name, u.user_age AS age
"""

# *** MEASURE EXECUTION TIME ***
start_time = time.time()
retrieve_result = execute_query(retrieve_users_query)
end_time = time.time()

# *** PRINT RETRIEVED DATA ***
print("USER NODES RETRIEVED:", retrieve_result)
print("EXECUTION TIME:", end_time - start_time, "SECONDS")
