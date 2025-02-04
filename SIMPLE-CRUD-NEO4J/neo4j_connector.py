from neo4j import GraphDatabase

# *** NEO4J CONNECTION CONFIGURATION ***
# THIS SCRIPT CONNECTS TO NEO4J RUNNING ON WINDOWS

# CONNECTION DETAILS
URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "1221qwwq"

# CREATE A NEO4J DRIVER INSTANCE
driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

# *** FUNCTION TO EXECUTE QUERIES ***
def execute_query(query, parameters=None):
    with driver.session() as session:
        result = session.run(query, parameters)
        return [record for record in result]

# *** TEST CONNECTION TO NEO4J ***
if __name__ == "__main__":
    try:
        print("TESTING NEO4J CONNECTION...")
        test_query = "RETURN 'Hello, Neo4j!' AS message"
        response = execute_query(test_query)
        print(response[0]["message"])  # EXPECTED OUTPUT: Hello, Neo4j!
    except Exception as e:
        print("CONNECTION FAILED:", e)
