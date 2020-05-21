
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options  # for suppressing the browser head
import re
import csv
import time
from itertools import islice


"""
Creates a webdriver to run the scraping in
"""
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('log-level=3') # Suppresses error messages

# Creates a Google Chrome webDriver object

# Put the path of the chromedriver.exe here
path = 'C:/Users/daniel/Downloads/chromedriver_win32_81/chromedriver.exe'
driver = webdriver.Chrome(path, options=options)

# FOR GOOGLE CLOUD SSH
# driver = webdriver.Chrome('/home/mimring131/chromedriver', options=options)
"""
Takes a csv of creatives and scrapes the creative from the url of each text creative. Writes a new csv containing
all of the information from csv_in plus a new column with the text creative, or '.' if there is no text creative.

csv_in: str, a csv where row[1] is a url and row[2] is a type.
csv_out: str, a csv name
returns: None, modifies csv_out
"""

def scrapeGoogleAdCreative(csv_in, csv_out):

    with open(csv_in, 'r', newline='', encoding="utf-8") as csvFile:
        with open(csv_out, 'a', newline='', encoding="utf-8") as csvWriter:
            writer = csv.writer(csvWriter, delimiter=',', quotechar='"')
            reader = csv.reader(csvFile, delimiter=',', quotechar='"')
            i = 0

            # Allows the program to be started at a chosen row of csv_in
            iterable = islice(reader, i, None)
            for row in iterable:
                # Prints to the console to keep track of status
                print("ROW NUMBER IS ", i)
                # Adds the header row, with additional fields for new information
                if i == 0:
                    row.extend(['Top_Line', 'URL_Contained', 'Ad_Creative'])
                    writer.writerow(row)
                    i + 1
                    pass
                elif row[3] != 'US': #Region
                    i + 1
                    pass
                elif row[2] != 'Text': #Type of ad
                    fields_to_add = ['.', '.', '.']
                    row.extend(fields_to_add)
                    writer.writerow(row)
                else:
                    try:
                        driver.get(row[1]) # row[1] is the url of the ad in Google's transparency report

                        #TEST WITH A WORKING TEXT AD:
                        # driver.get("https://transparencyreport.google.com/political-ads/library/advertiser/AR100838960162406400/creative/CR264597198346387456")
                        #print("worked for test")
                        # if row[2] == 'Text':
                        """
                        Tries to find the XPATH of the ad creative. If nothing comes up within 0.75 second it moves on since the page has loaded by then
                        """
                        content = WebDriverWait(driver, 0.75).until(
                            EC.presence_of_element_located((By.XPATH, "/html/body/app/site-layout/mat-sidenav-container/mat-sidenav-content/ads-report/ng-component/fetched-content/report-section/section/div/creative-rendering/div/visualization-container/div[1]/text-ad/div"))
                        ).text
                        print(content)

                        """
                        Creates a list of three elements, where the first one is the blue header text of the ad,
                        the second one is the link in the line underneath that, and the third one is the text creative
                        """
                        row.extend(re.findall(re.compile(r'(?<=Ad\s).+(?=\n)|^.+(?=\n)|(?<=\n).*\Z'), content))

                        """
                        Tentative code for scraping img sources. Difficult because there is no universal
                        Tag for img, it differs by ad and img style
                        """
                        # else:
                        #     content=WebDriverWait(driver, 1.2).until(
                        #         EC.presence_of_element_located((By.TAG_NAME, "img.img_ad"))
                        #     ).get_attribute("src")
                        #     row.extend(['.', '.', content])

                        writer.writerow(row)


                    # Allows the program to be ended
                    except KeyboardInterrupt:
                        break
                    # If no tag is found within one second
                    except TimeoutException:
                        fields_to_add = ['Ad violated Google policy', 'Ad violated Google policy', 'Ad violated Google policy']
                        row.extend(fields_to_add)
                        writer.writerow(row)
                i +=1
    csvFile.close()
    csvWriter.close()


# scrapeGoogleAdCreative("google-political-ads-creative-stats.csv", "test_google_ads.csv")
scrapeGoogleAdCreative("filteredAds.csv", "testAdCreatives.csv")
