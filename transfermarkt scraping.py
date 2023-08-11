import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (replace 'chrome' with 'firefox' if using Firefox)
driver = webdriver.Chrome()

# Open the URL
url = "https://www.transfermarkt.com/transfers/einnahmenausgaben/statistik/a/ids/a/sa//saison_id/2017/saison_id_bis/2022/land_id/0/nat/0/kontinent_id/0/pos//w_s//intern/0"
driver.get(url)

# Wait for the table to load
wait = WebDriverWait(driver, 10)
time.sleep(10)
table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".responsive-table")))

# Find all rows in the table
rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")

# Create a list to store club expenditures data
clubExpenditures_data = []

# Iterate through each row and extract data
for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")
    if len(columns) >= 3:
        clubName = columns[2].text
        expenditure = columns[3].text
        clubExpenditures_data.append([clubName, expenditure])

# Write the data to the CSV file (append to existing data)
csvFile = "club expenditures.csv"
with open(csvFile, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for row in clubExpenditures_data:
        writer.writerow(row)  # Write each row separately

# Close the WebDriver
driver.quit()

print(f"Data appended to {csvFile}")
