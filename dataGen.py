import random
import csv


#Paper CSV generation
paperCount = 20000
paperList =  []
paperList.append(["paperID","paperTitle","citedBy","abstract"])
topPaper = 500
for pc in range(1,topPaper + 1):
    count = paperCount + pc
    citedBy = count
    while (citedBy == count):
        citedBy = random.randint(paperCount,paperCount+topPaper)
    paperList.append([str(count),"Paper #" + str(count), str(citedBy),"Abstract #" +str(count)])

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
keywordCount = 50000
keywordList =  []
keywordList.append(["keywordID","keyword"])
topKeyword = 50

for pc in range(1,topKeyword + 1):
    count = keywordCount + pc
    keywordList.append([str(count),"Keyword #" + str(count)])

f = open("./data/keywords.csv","w")
writer = csv.writer(f)
for row in keywordList:
    writer.writerow(row)

#CitedBy csv
citedList =  []
citedList.append(["paperID","citedBy"])
topCited = 3501

for c in range(1,topCited):
    paper = c %  topPaper
    if paper == 0:
        paper = 500
    paper = paper + paperCount
    cited = paper
    while (paper == cited):
        cited = random.randint(paperCount,paperCount+topPaper+1)

    citedList.append([str(paper),str(cited)])

'''
TODO: control that a paper is not cited more than once in the same paper
'''

f = open("./data/citedBy_relation.csv","w")
writer = csv.writer(f)
for row in citedList:
    writer.writerow(row)

#written_by csv

writtenList =  []
writtenList.append(["paperID","authorID","main"])
topCited = 2000
dicMain = {}

for c in range(1,topCited+1):
    paper = c %  topPaper
    if paper == 0:
        paper = 500
    if str(paper) not in dicMain:
        main = "Yes"
        dicMain[str(paper)] = "Yes"
    else:
        main = "No"
    paper = paper + paperCount
    written = random.randint(authorCount,authorCount+topAuthor+1)

    writtenList.append([str(paper),str(written),main])

'''
TODO: control that a author does not appear more than once as a writer of a paper
'''

f = open("./data/writes_relation.csv","w")
writer = csv.writer(f)
for row in writtenList:
    writer.writerow(row)

#reviwed_by

reviewList =  []
reviewList.append(["paperID","authorID","review","decision"])
topReview = 1500
dicReview = {}

for c in range(1,topReview + 1):
    paper = c %  topPaper
    if paper == 0:
        paper = 500

    paper = paper + paperCount
    decisionProb = random.randint(0, 6)
    if decisionProb > 2:
        decision = "Approved"
        review = "Nice Nice..."
    else:
        decision = "Denied"
        review = "Bad bad..."

    reviewer = random.randint(authorCount,authorCount+topAuthor+1)

    reviewList.append([str(paper),str(reviewer),review,decision])

'''
TODO:   control that an author does not review more than once the same paper
        control that an author is not the reviewer of his own paper        
'''

f = open("./data/reviewedBy_relation.csv","w")
writer = csv.writer(f)
for row in reviewList:
    writer.writerow(row)


#containsKeyword

containList =  []
containList.append(["paperID","keywordID"])
topContain = 2000
dicContain = {}

for c in range(1,topContain + 1):
    paper = c %  topPaper
    if paper == 0:
        paper = 500
    paper = paper + paperCount

    keyword = random.randint(keywordCount,keywordCount+topKeyword+1)

    containList.append([str(paper),str(keyword)])

'''
TODO:   control that a paper does not contain the same keyword more than once
'''

f = open("./data/contains_relation.csv","w")
writer = csv.writer(f)
for row in containList:
    writer.writerow(row)


#published_in
publishedList =  []
publishedList.append(["paperID","journalID", "volume", "year"])
topPublished = 500
dicPublished = {}

for c in range(1,topPublished + 1):
    journal = c %  topJournal
    if journal == 0:
        journal = 25
    journal = journal + journalCount

    paper = random.randint(paperCount,paperCount+topPaper+1)
    volume = random.randint(1,21)
    year = random.randint(2010,2021)
    publishedList.append([str(paper),str(journal),volume,year])

'''
TODO:   control that a journal does not contain the same paper more than once
        control that a paper is not orfan (has either a journal or proceeding associated)
        control that a paper is not present in a journal and in a proceeding at the same time
'''

f = open("./data/publishes_relation.csv","w")
writer = csv.writer(f)
for row in publishedList:
    writer.writerow(row)


#submitted_to
submittedList =  []
submittedList.append(["paperID","proceedingID", "edition", "venue", "year", "month", "day"])
topSubmitted = 500
dicSubmitted = {}

for c in range(1,topSubmitted + 1):
    proceeding = c %  topProceeding
    if proceeding == 0:
        proceeding = 25
    proceeding = proceeding + proceedingCount

    paper = random.randint(paperCount,paperCount+topPaper+1)
    edition = random.randint(1,21)
    year = random.randint(2010,2021)
    month = random.randint(1, 12)
    day = random.randint(1, 31)
    venue = "City ###"
    submittedList.append([str(paper),str(proceeding),edition,venue,year,month,day])

'''
TODO:   control that a proceeding does not contain the same paper more than once
        control that a paper is not orfan (has either a journal or proceeding associated)
        control that a paper is not present in a journal and in a proceeding at the same time
        control that day is in the limits of days within the corresponding month (febreaury < 29 for ins)
'''

f = open("./data/includes_relation.csv","w")
writer = csv.writer(f)
for row in submittedList:
    writer.writerow(row)

#affiliation
affiliationList =  []
affiliationList.append(["authorID","orgID"])
topAffiliation = 150
dicAffiliation = {}

for c in range(1,topAffiliation + 1):
    org = c %  topOrg
    if org == 0:
        org = 15
    org = org + orgCount

    author = random.randint(authorCount,authorCount+topAuthor+1)
    affiliationList.append([str(org),str(author)])

'''
TODO:   control that a journal does not contain the same paper more than once
        control that a paper is not orfan (has either a journal or proceeding associated)
        control that a paper is not present in a journal and in a proceeding at the same time
'''

f = open("./data/host_relation.csv","w")
writer = csv.writer(f)
for row in affiliationList:
    writer.writerow(row)

