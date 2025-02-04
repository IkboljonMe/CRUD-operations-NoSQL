from mongodb_connection import execute_query

# *** QUERY TO RETRIEVE USER DATA ***
search_criteria = {"full_name": "Alice Smith"}

# *** EXECUTE FETCH OPERATION ***
fetch_result = execute_query("read", query=search_criteria)

# *** PRINT RETRIEVED DATA ***
print("USER DATA RETRIEVED:", fetch_result)
