from neo4j import GraphDatabase

# Connection details
URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "1221qwwq"

# Create a Neo4j driver instance
driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

# Function to execute queries
def execute_query(query, parameters=None):
    with driver.session() as session:
        result = session.run(query, parameters)
        return [record for record in result]

# Test connection
if __name__ == "__main__":
    try:
        print("Testing Neo4j connection...")
        test_query = "RETURN 'Hello, Neo4j!' AS message"
        response = execute_query(test_query)
        print(response[0]["message"])  # Output: Hello, Neo4j!
    except Exception as e:
        print("Connection failed:", e)
