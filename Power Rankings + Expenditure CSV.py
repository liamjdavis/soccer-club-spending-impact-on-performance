import csv

# read power rankings csv
with open('spi_global_rankings.csv', 'r') as powerRankings:
    rankingsReader = csv.reader(powerRankings)
    rankingsData = list(rankingsReader)

# read club expenditures csv
with open('club expenditures.csv', 'r') as expenditures:
    expendituresReader = csv.reader(expenditures)
    expenditureData = list(expendituresReader)
    
# put all club rankings into list
clubList = []
rankingsList = []
expenditureList = []

for row in expenditureData:
    clubList.append(row[0])
    expenditureList.append(row[1])

# find rankings for every club
for row in rankingsData:
    club = row[2]
    if club in clubList:
        rankingsList.append(row[0])

# sort rankings by order and sort clubs and expenditures with them
