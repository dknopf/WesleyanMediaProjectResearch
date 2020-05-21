# WesleyanMediaProjectResearch
Google Ad Data Creatives Webscraper

In order to run the AdCreativeWebscraper.py you must install the selenium python package. This also relies upon the CSV package and the itertools islice package. You MUST also install the correct chromedriver from https://chromedriver.chromium.org/downloads based on your Chrome browser version. This can be found at https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have.

The webscraper takes in a CSV and outputs a new CSV. The filterAds.py function takes a CSV in the form of the google-political-ads-creative-stats file from the political ads transparency report found at https://transparencyreport.google.com/political-ads/region/US?hl=en. filterAds filters the ads so that only the US ads beginning on a specific date are included.

The webscraper opens a headless (no visible window) version of chrome that goes to the URL of the ad creative given in the original google CSV and scrapes for the text of the ad, adding that text to the end of the CSV. The webscraper waits 0.75 seconds for the page to be loaded, and if it cannot find the XPATH of the ad it assumes that the ad has violated Google's ad terms, which makes it inaccessible. The webscraper takes about 14 hours to run on a year's worth of ads.
