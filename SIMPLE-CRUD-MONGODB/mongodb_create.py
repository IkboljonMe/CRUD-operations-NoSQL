from mongodb_connection import execute_query

# *** NEW USER DATA TO INSERT ***
user_data = {"full_name": "Alice Smith", "user_age": 28}

# *** EXECUTE INSERT OPERATION ***
insert_result = execute_query("create", query=user_data)

# *** PRINT INSERTION RESULT ***
print("NEW USER DOCUMENT INSERTED:", insert_result)
