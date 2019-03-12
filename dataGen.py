import random
import csv

####################nodes######################

#Paper CSV generation

paperCount = 20000
paperList =  []
paperList.append(["paperID","paperTitle"])
#Indicates how many papers will be generated.
topPaper = 2000
for c in range(1,topPaper + 1):
    count = paperCount + c
    paperList.append([str(count),"Paper #" + str(count)])
f = open("./data/paper.csv","w")
writer = csv.writer(f)
for row in paperList:
    writer.writerow(row)


#Organization CSV generation

orgCount = 30000
orgList =  []
orgList.append(["ordID","orgName"])
topOrg = 15
for c in range(1,topOrg + 1):
    count = orgCount + c
    orgList.append([str(count),"Organization #" + str(count)])

f = open("./data/organization.csv","w")
writer = csv.writer(f)
for row in orgList:
    writer.writerow(row)


#Author CSV generation

authorCount = 10000
authorList =  []
authorList.append(["authorID","authorName"])
topAuthor = 150
for pc in range(1,topAuthor + 1):
    count = authorCount + pc
    authorList.append([str(count),"Author #" + str(count)])

f = open("./data/author.csv","w")
writer = csv.writer(f)
for row in authorList:
    writer.writerow(row)

#Journal CSV

journalCount = 60000
journalList =  []
journalList.append(["journalID","journalName"])
topJournal = 25
for pc in range(1,topJournal + 1):
    count = journalCount + pc
    journalList.append([str(count),"Journal #" + str(count)])

f = open("./data/journals.csv","w")
writer = csv.writer(f)
for row in journalList:
    writer.writerow(row)


#Proceeding CSV

proceedingCount = 50000
proceedingList =  []
proceedingList.append(["proceedingID","proceedingName"])
topProceeding = 25

for pc in range(1,topProceeding + 1):
    count = proceedingCount + pc
    proceedingList.append([str(count),"Proceeding #" + str(count)])

f = open("./data/proceedings.csv","w")
writer = csv.writer(f)
for row in proceedingList:
    writer.writerow(row)


#Keyword CSV

keywordCount = 40000
keywordList =  []
keywordList.append(["keywordID","keyword"])
topKeyword = 50

keywords = ["data management", "indexing", "data modeling", "big data", "data processing", "data storage","data querying"
    ,"health informatics","HL7", "FHIR", "OPENEHR","interoperability","cloud computing","saas", "IA", "machine learning", "visual analytics"
    ,"data warehouse","sql","mongoDB"]

for pc in range(1,topKeyword + 1):
    count = keywordCount + pc
    if (pc <= 20):
        keywordList.append([str(count), keywords[pc-1]])
    else:
        keywordList.append([str(count), "Keyword #" + str(count)])


f = open("./data/keywords.csv","w")
writer = csv.writer(f)
for row in keywordList:
    writer.writerow(row)

####################relations######################

#CitedBy csv

citedList =  []
citedList.append(["paperID","citedBy"])
topCited = topPaper * 7
alreadyCited = {}
for c in range(1,topCited + 1):
    '''paper = c %  topPaper
    if paper == 0:
        paper = topPaper
    paper = paper + paperCount
'''
    paper = random.randint(paperCount+1, paperCount + topPaper)

    if not paper in alreadyCited.keys():
        alreadyCited[paper]=[]

    cited = paper
    already = True
    '''
    Control that a paper is not cited twice in the same paper and the cited paper is different than the citing paper
    '''
    while (paper == cited or already):
        cited = random.randint(paperCount+1,paperCount+topPaper)
        if cited in alreadyCited[paper]:
            already = True
        else:
            already = False
            alreadyCited[paper].append(cited)

    citedList.append([str(paper),str(cited)])


f = open("./data/citedBy_relation.csv","w")
writer = csv.writer(f)
for row in citedList:
    writer.writerow(row)


#writes csv

writtenList =  []
writtenList.append(["paperID","authorID","main"])
topWrites = topPaper * 3
dicMain = []
authorWrites = {}
for c in range(1,topWrites+1):
    paper = c %  topPaper
    if paper == 0:
        paper = topPaper
    if paper not in dicMain:
        main = "Yes"
        dicMain.append(paper)
    else:
        main = "No"
    paper = paper + paperCount
    if paper not in authorWrites.keys():
        authorWrites[paper]=[]

    '''
    Control that a author does not appear more than once as a writer of a paper
    '''
    already = True
    while already:
        writer = random.randint(authorCount+1,authorCount+topAuthor)
        if writer in authorWrites[paper]:
            already=True
        else:
            already=False
            authorWrites[paper].append(writer)

    writtenList.append([str(paper),str(writer),main])


f = open("./data/writes_relation.csv","w")
writer = csv.writer(f)
for row in writtenList:
    writer.writerow(row)


#reviews

reviewList =  []
reviewList.append(["paperID","authorID","review","decision"])
topReview = topPaper * 3
dicReview = {}

for c in range(1,topReview + 1):
    paper = c %  topPaper
    if paper == 0:
        paper = topPaper

    paper = paper + paperCount
    decisionProb = random.randint(0, 6)
    if decisionProb > 2:
        decision = "Approved"
        review = "Nice Nice..."
    else:
        decision = "Denied"
        review = "Bad bad..."

    if paper not in dicReview.keys():
        dicReview[paper]=[]

    reviewer = random.randint(authorCount+1,authorCount+topAuthor)
    #A reviewer should not be the author of the paper nor is already a reviewer of the paper
    while reviewer in authorWrites[paper] or reviewer in dicReview[paper]:
        reviewer = random.randint(authorCount+1, authorCount + topAuthor)
    dicReview[paper].append(reviewer)
    reviewList.append([str(paper),str(reviewer),review,decision])


f = open("./data/reviews_relation.csv","w")
writer = csv.writer(f)
for row in reviewList:
    writer.writerow(row)


#containsKeyword

containList =  []
containList.append(["paperID","keywordID"])
topContain = topPaper * 4
dicContain = {}

for c in range(1,topContain + 1):
    paper = c %  topPaper
    if paper == 0:
        paper = topPaper
    paper = paper + paperCount

    if paper not in dicContain.keys():
        dicContain[paper]= []

    keyword = keywordCount + random.randint(1, 8)
    while keyword in dicContain:
        keyword = keywordCount + random.randint(1, 8)
    dicContain[paper].append(keyword)
    '''
    probKeyword = random.randint(0, 10)
    if (probKeyword < 8):
        keyword = probKeyword
    else:
        keyword = random.randint(keywordCount,keywordCount+topKeyword+1)
    '''
    containList.append([str(paper),str(keyword)])


f = open("./data/contains_relation.csv","w")
writer = csv.writer(f)
for row in containList:
    writer.writerow(row)


#published_in

publishedList =  []
publishedList.append(["paperID","journalID", "volume", "year"])
topPublished = int(topPaper / 2)
dicPublished = {}

for c in range(1,topPublished + 1):

    paper = c %  topPublished
    if paper == 0:
        paper = topPublished
    paper = paper + paperCount

    journal = c % topJournal
    if journal == 0:
        journal = topJournal
    journal = journal + journalCount

    volume = random.randint(1,21)
    year = random.randint(2010,2021)
    publishedList.append([str(paper),str(journal),volume,year])


f = open("./data/publishes_relation.csv","w")
writer = csv.writer(f)
for row in publishedList:
    writer.writerow(row)


#includes_relation

submittedList =  []
submittedList.append(["paperID","proceedingID", "edition", "venue", "year", "month", "day"])
baseSubmitted = int(topPaper / 2)
dicSubmitted = {}

for c in range(baseSubmitted + 1,topPaper + 1):

    paper = c%topPaper
    if paper == 0:
        paper = topPaper
    paper = paper + paperCount

    proceeding = c %  topProceeding
    if proceeding == 0:
        proceeding = topProceeding
    proceeding = proceeding + proceedingCount

    edition = random.randint(1,21)
    year = random.randint(2010,2021)
    month = random.randint(1, 12)
    day = random.randint(1, 31)
    venue = "City ###"
    submittedList.append([str(paper),str(proceeding),edition,venue,year,month,day])


f = open("./data/includes_relation.csv","w")
writer = csv.writer(f)
for row in submittedList:
    writer.writerow(row)

#affiliation

affiliationList =  []
affiliationList.append(["orgID","authorID"])
dicAffiliation = {}

for c in range(1,topAuthor + 1):
    author = c % topAuthor
    if author == 0:
        author = topAuthor
    author = author + topAuthor

    org = c %  topOrg
    if org == 0:
        org = topOrg
    org = org + orgCount

    affiliationList.append([str(org),str(author)])


f = open("./data/host_relation.csv","w")
writer = csv.writer(f)
for row in affiliationList:
    writer.writerow(row)

