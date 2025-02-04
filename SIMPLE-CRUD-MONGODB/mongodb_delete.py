from mongodb_connection import execute_query

# *** DEFINE SEARCH CRITERIA FOR DELETION ***
delete_criteria = {"full_name": "Alice Smith"}

# *** EXECUTE REMOVE OPERATION ***
remove_result = execute_query("delete", query=delete_criteria)

# *** PRINT DELETION RESULT ***
print("USER DATA REMOVED:", remove_result)
