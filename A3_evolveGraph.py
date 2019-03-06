#A3

from py2neo import Graph
import sys

graph = Graph()

path = "file:"+sys.argv[1]

file1 = 'organization.csv'
file2 = 'affiliation_relation.csv'
file3 = 'reviewedBy_relation.csv'

print("Connection established to server 7474")

#Additional nodes creation

print("New nodes will start being created")

organizations = '''USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM ''' + '''"{0}{1}"'''.format(path, file1) + ''' AS row CREATE (:Organization {orgID: row.ordID, orgName: row.orgName});'''

#graph.cypher.execute(organizations)
graph.run(organizations)

print("Node organization was successfully created")

#Add affiliation relationship

hosts = '''USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM ''' + '''"{0}{1}"'''.format(path, file2) + ''' AS row MATCH (author:Author {authorID: row.authorID}) MATCH (organization:Organization {orgID: row.orgID}) MERGE (author)<-[:HOSTS]-(organization)'''

#graph.cypher.execute(hosts)
graph.run(hosts)

print("Relationship affiliated_to was created successfully")

#Delete reviewing relationship and create it again with new attributes

delete_rel = '''MATCH ()-[r:REVIEWS]-() DELETE r'''
#graph.cypher.execute(delete_rel)
graph.run(delete_rel)

reviews = '''USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM ''' + '''"{0}{1}"'''.format(path, file3) + ''' AS row MATCH (paper:Paper {paperID: row.paperID}) MATCH (author:Author {authorID: row.authorID}) MERGE (paper)<-[:REVIEWS {review: row.review, decision: row.decision}]-(author);'''

graph.run(reviews)

print("Relationship reviewed_by was updated and created successfully")
print("You are now ready to start querying your database. ENJOY!")


