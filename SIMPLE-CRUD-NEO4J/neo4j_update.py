from neo4j_connector import execute_query
import time

# *** DEFINE QUERY TO MODIFY USER NODE ***
modify_user_query = """
MATCH (u:User {full_name: 'Alice Smith'})
SET u.user_age = 32
RETURN u.full_name AS name, u.user_age AS age
"""

# *** MEASURE EXECUTION TIME ***
start_time = time.time()
modify_result = execute_query(modify_user_query)
end_time = time.time()

# *** PRINT UPDATE RESULT ***
print("USER NODE MODIFIED:", modify_result)
print("EXECUTION TIME:", end_time - start_time, "SECONDS")
