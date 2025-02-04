from mongodb_connection import execute_query

# *** DEFINE SEARCH CRITERIA FOR UPDATE ***
update_criteria = {"full_name": "Alice Smith"}

# *** DEFINE UPDATED VALUES ***
new_values = {"user_age": 32}

# *** EXECUTE MODIFY OPERATION ***
modify_result = execute_query("update", query=update_criteria, update=new_values)

# *** PRINT UPDATE RESULT ***
print("USER DATA MODIFIED:", modify_result)
