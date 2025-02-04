from pymongo import MongoClient
import time

# *** MONGODB CONNECTION CONFIGURATION ***
# THIS SCRIPT CONNECTS TO MONGODB RUNNING ON macOS

# MONGODB ATLAS CONNECTION URI
MONGO_URI = "mongodb+srv://tansu:3ooEl8Njhhk1ynR9@cluster0.8hfbl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "test"
COLLECTION_NAME = "simple_crud"

try:
    # *** CONNECT TO MONGODB SERVER ***
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]

    # *** GET COLLECTION REFERENCE ***
    # MONGODB AUTOMATICALLY CREATES COLLECTION ON FIRST INSERT
    collection = db[COLLECTION_NAME]

    print("MONGODB CONNECTED SUCCESSFULLY!")

except Exception as e:
    print("ERROR CONNECTING TO MONGODB:", e)

# *** FUNCTION TO EXECUTE CRUD OPERATIONS ***
def execute_query(operation, query=None, update=None):
    start_time = time.time()
    
    try:
        if operation == "create":
            result = collection.insert_one(query)
            output = {"INSERTED_ID": str(result.inserted_id)}

        elif operation == "read":
            result = collection.find_one(query)
            output = result if result else "NO DOCUMENT FOUND."

        elif operation == "update":
            result = collection.update_one(query, {"$set": update})
            output = {"MODIFIED_COUNT": result.modified_count}

        elif operation == "delete":
            result = collection.delete_one(query)
            output = {"DELETED_COUNT": result.deleted_count}

        else:
            output = "INVALID OPERATION"

        end_time = time.time()
        print(f"EXECUTION TIME: {end_time - start_time} SECONDS")
        return output

    except Exception as e:
        print("MONGODB ERROR:", e)
        return None
