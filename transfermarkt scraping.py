import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.transfermarkt.com/transfers/einnahmenausgaben/statistik/plus/1?ids=a&sa=&saison_id=2017&saison_id_bis=2022&land_id=&nat=&kontinent_id=&pos=&altersklasse=&w_s=&leihe=&intern=0&plus=1'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
expenditureTable = soup.find(class_ = 'responsive-table')

if expenditureTable:
    clubs = []
    expenditures = []

    for row in expenditureTable.find_all('tr')[1:]:
        columns = row.find_all('td')
        clubName = columns[2].text.strip()
        clubExpenditure = columns[4].text.strip()
        clubs.append(clubName)
        expenditures.append(clubExpenditure)

    data = {'Club': clubs, 'Expenditure': expenditures}
    df = pd.DataFrame(data)

    df.to_csv('club expenditures.csv', index=False)
else: 
    print("expenditure table not found")