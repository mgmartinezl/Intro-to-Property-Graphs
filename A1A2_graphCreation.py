#A1-A2

from py2neo import Graph
import sys


graph = Graph()

path = "file:"+sys.argv[1]

file1 = 'paper.csv'
file2 = 'author.csv'
file3 = 'proceedings.csv'
file4 = 'journalsdummy.csv'
file5 = 'keywords.csv'
file6 = 'writes_relation.csv'
file7 = 'reviewedBy_relation.csv'
file8 = 'contains_relation.csv'
file9 = 'publishes_relation.csv'
file10 = 'includes_relation.csv'
file11 = 'citedBy_relation.csv'

print("Connection established to server 7474")

#Clean database to insert graph and instances

restartNeo4j = '''
MATCH (n)
OPTIONAL MATCH (n)-[r]-()
DELETE n,r
'''
graph.cypher.execute(restartNeo4j)

print("Database successfully dropped")

#Nodes creation

print("Nodes will start being created")


paper = '''USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM ''' + '''"{0}{1}"'''.format(path, file1) + ''' AS row CREATE (:Paper{paperID:row.paperID, paperTitle:row.paperTitle, citedBy:row.citedBy, abstract:row.abstract,citations: 0});'''


author = '''USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM ''' + '''"{0}{1}"'''.format(path, file2) + ''' AS row CREATE (:Author {authorID: row.authorID, authorName: row.authorName});'''


proc = '''USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM ''' + '''"{0}{1}"'''.format(path, file3) + ''' AS row CREATE (:Proceeding {proceedingID: row.proceedingID, proceedingName: row.proceedingName});'''

journal = '''USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM ''' + '''"{0}{1}"'''.format(path, file4) + ''' AS row CREATE (:Journal {journalID: row.journalID, journalName: row.journalName});'''


keyword = '''USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM ''' + '''"{0}{1}"'''.format(path, file5) + ''' AS row CREATE (:Keyword {keywordID: row.keywordID, keyword: row.keyword});'''

graph.cypher.execute(paper)

graph.cypher.execute(author)

graph.cypher.execute(proc)

graph.cypher.execute(journal)

graph.cypher.execute(keyword)

print("Nodes successfully created")

#Create indexes to accelerate lookups

print("Indexes being created...")

i1 = '''CREATE INDEX ON :Paper(paperID);'''
graph.cypher.execute(i1)

i2 = '''CREATE INDEX ON :Author(authorID);'''
graph.cypher.execute(i2)

i3 = '''CREATE INDEX ON :Keyword(keywordID);'''
graph.cypher.execute(i3)

i4 = '''CREATE INDEX ON :Journal(journalID);'''
graph.cypher.execute(i4)

i5 = '''CREATE INDEX ON :Proceeding(proceedingID);'''
graph.cypher.execute(i5)

print("Indexes successfully created")

#Create relationships between nodes

print("Relatioships will start being created")

writes = '''USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM ''' + '''"{0}{1}"'''.format(path, file6) + ''' AS row MATCH (paper:Paper {paperID: row.paperID}) MATCH (author:Author {authorID: row.authorID}) MERGE (paper)<-[:WRITES {main_author: row.main}]-(author);'''

reviews = '''USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM ''' + '''"{0}{1}"'''.format(path, file7) + ''' AS row MATCH (paper:Paper {paperID: row.paperID}) MATCH (author:Author {authorID: row.authorID}) MERGE (paper)<-[:REVIEWS]-(author);'''

contains = '''USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM ''' + '''"{0}{1}"'''.format(path, file8) + ''' AS row MATCH (paper:Paper {paperID: row.paperID}) MATCH (kw:Keyword {keywordID: row.keywordID}) MERGE (paper)-[:CONTAINS]->(kw);'''

publishes = '''USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM ''' + '''"{0}{1}"'''.format(path, file9) + ''' AS row MATCH (paper:Paper {paperID: row.paperID}) MATCH (journal:Journal {journalID: row.journalID}) MERGE (paper)<-[:PUBLISHES {volume: row.volume, year: row.year}]-(journal);'''

includes = '''USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM ''' + '''"{0}{1}"'''.format(path, file10) + ''' AS row MATCH (paper:Paper {paperID: row.paperID}) MATCH (proceeding:Proceeding {proceedingID: row.proceedingID}) MERGE (paper)<-[:INCLUDES {edition: row.edition, venue: row.venue, year: row.year, month: row.month, day: row.day}]-(proceeding);'''

cited_by = '''USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM ''' + '''"{0}{1}"'''.format(path, file11) + ''' AS row MATCH (paper:Paper {paperID: row.paperID}) MATCH (paper_citation:Paper {paperID: row.citedBy}) SET paper.citations = paper.citations + 1 MERGE (paper)-[:CITED_BY]->(paper_citation);'''

graph.cypher.execute(writes)

graph.cypher.execute(reviews)

graph.cypher.execute(contains)

graph.cypher.execute(publishes)

graph.cypher.execute(includes)

graph.cypher.execute(cited_by)

print("Relationships succesfully created")
print("You are now ready to start querying your database. ENJOY!")













