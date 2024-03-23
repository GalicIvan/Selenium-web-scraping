# Bot koji web scrapingom ispisuje sve centre u BiH ligi koji su imali neku minutazu ove godine

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-notifications')
chrome_options.add_argument('disable-popup-blocking')
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.eurobasket.com/Bosnia/basketball-Players.aspx')
driver.maximize_window()

time.sleep(2)

positionCenter = driver.find_element(By.ID, 'position4')
positionCenter.click()

time.sleep(2)

statsRadio = driver.find_element(By.ID, 'viewmode2')
statsRadio.click()

time.sleep(2)

showPlayers = driver.find_element(By.ID, 'Paging')
select_element = showPlayers
select = Select(select_element)
select.select_by_value('100')

time.sleep(2)

'''playerNames = []
allPlayers = driver.find_elements(By.CLASS_NAME, 'fixedColLine')
for player in allPlayers:
    playerName = player.text
    playerNames.append(playerName)

for name in playerNames:
    print(name)'''

playerInfo = []

playersTable = driver.find_element(By.ID, 'players')
tBody = playersTable.find_element(By.TAG_NAME, 'tbody')
tRow = tBody.find_elements(By.TAG_NAME, 'tr')

time.sleep(1)

for row in tRow:
    rowText = row.text
    playerInfo.append(rowText)

for player in playerInfo:
    player = player.split(' ')
    if float(player[5]) > 0:
        print(player)

time.sleep(10000)
driver.quit()