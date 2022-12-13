from neo4j import GraphDatabase

#  Conexão com o Neo4j
# uri = "neo4j+s://c87d723c.databases.neo4j.io"
# user = "neo4j"
# password = "6Q0Ytiw6C-bSjOWFVYv1weh0isXgKRqB6Bxj8G8IHrY"

try:
    driver = GraphDatabase.driver(uri, auth=(user, password))
    session = driver.session()
    print("Conexão com Neo4j estabelecida com sucesso!")
except Exception as erro:
    print("Ih rapaz...deu erro", erro)
