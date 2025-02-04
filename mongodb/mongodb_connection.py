from pymongo import MongoClient
import time

# MongoDB Atlas Connection URI
MONGO_URI = "mongodb+srv://ikboljonme:FcP2smDgn2tmrx4j@cluster0.gjqry.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "test_db"
COLLECTION_NAME = "test_collection"

try:
    # Connect to MongoDB
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    
    # Get collection reference (MongoDB creates it on first insert)
    collection = db[COLLECTION_NAME]

    print("MongoDB connected successfully!")

except Exception as e:
    print("Error connecting to MongoDB:", e)

# Function to execute MongoDB queries
def execute_query(operation, query=None, update=None):
    start_time = time.time()
    
    try:
        if operation == "create":
            result = collection.insert_one(query)
            output = {"Inserted_ID": str(result.inserted_id)}

        elif operation == "read":
            result = collection.find_one(query)
            output = result if result else "No document found."

        elif operation == "update":
            result = collection.update_one(query, {"$set": update})
            output = {"Modified Count": result.modified_count}

        elif operation == "delete":
            result = collection.delete_one(query)
            output = {"Deleted Count": result.deleted_count}

        else:
            output = "Invalid Operation"

        end_time = time.time()
        print(f"Execution Time: {end_time - start_time} seconds")
        return output

    except Exception as e:
        print("MongoDB Error:", e)
        return None
