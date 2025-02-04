from neo4j_connector import execute_query
import time

# *** DEFINE QUERY TO ADD A NEW PERSON NODE ***
add_person_query = """
CREATE (u:User {full_name: 'Alice Smith', user_age: 28})
RETURN u.full_name AS name, u.user_age AS age
"""

# *** MEASURE EXECUTION TIME ***
start_time = time.time()
add_result = execute_query(add_person_query)
end_time = time.time()

# *** PRINT CREATION RESULT ***
print("USER NODE ADDED:", add_result)
print("EXECUTION TIME:", end_time - start_time, "SECONDS")
