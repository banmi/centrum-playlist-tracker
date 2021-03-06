from selenium import webdriver
import csv
import time
from collections import defaultdict
from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)
browser.get("https://centrum.fm/")

# get last position
with open('beta.csv', 'r', newline='', encoding='utf-8-sig') as file:
    lines = file.readlines()
    last_row = lines[-1]
    print(last_row)
    num = int(last_row[0])

columns = defaultdict(list)  # each value in each column is appended to a list

with open('beta.csv', encoding="utf-8-sig") as f:
    reader = csv.DictReader(f, delimiter=";") # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

print(columns['Artist'][-1] + ' last writen artist')



# get actual song
locator = browser.find_element_by_xpath("//div[@id='container']/div[@id='header']/div[@id='antena-header']/div[@class='playing']/div[@class='antena-header2']")

last_artist = columns['Artist'][-1]
artist = locator.find_element_by_xpath("//span[@class='artist']").get_attribute("innerHTML")
title = locator.find_element_by_xpath("//span[@class='title']").get_attribute("innerHTML")

def update_csv():
    with open('beta.csv', 'a', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([num+1, time.strftime('%d-%m-%Y %H:%M:%S'), artist, title])
        browser.close()


print(artist + ' actual artist')
print(title + ' actual title')


if last_artist == artist:
    print("duplicate skipping")
    time.sleep(15)
else:
    update_csv()
    last_artist = artist
    print(last_artist + ' updated artist')


    print("updating")


