import csv

# read power rankings csv
with open('spi_global_rankings.csv', 'r') as powerRankings:
    rankingsReader = csv.reader(powerRankings)
    rankingsData = list(rankingsReader)

# read club expenditures csv
with open('club expenditures.csv', 'r') as expenditures:
    expendituresReader = csv.reader(expenditures)
    expenditureData = list(expendituresReader)
    
# put all club rankings and expenditures
clubList = []
rankingsList = []
expenditureList = []

for row in rankingsData:
    club = row[2]
    ranking = row[0]

    for row1 in expenditureData:
        if club in row1[0]:
            clubList.append(club)
            rankingsList.append(ranking)
            expenditureList.append(row1[1])

# put all lists in Power Rankings + Expenditure csv
with open('Power Rankings + Expenditure.csv', 'a', newline='') as csvfile:
    writer  = csv.writer(csvfile)

    for i in range (len(clubList)):
        row_toWrite = [clubList[i], rankingsList[i], expenditureList[i]]
        writer.writerow(row_toWrite)