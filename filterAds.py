import csv


"""
Takes a CSV in the form of the google political ads creative stats csv and creates a new csv
filteredAds.csv containing only the entries in the original CSV which have region (row[3]) as US and take place after january 1 2019
(dates in US format)
"""
def filterAdCreatives(csv_in):
    with open(csv_in, 'r', newline = '', encoding = "utf-8") as csvFile:
        with open("filteredAds.csv", 'w', newline = '', encoding = "utf-8") as csvWriter:
            writer = csv.writer(csvWriter, delimiter=',', quotechar='"')
            reader = csv.reader(csvFile, delimiter=',', quotechar='"')
            # writer.writerow(['Ad_ID', 'Ad_URL', 'Ad_Type', 'Regions', 'Advertiser_ID', 'Advertiser_Name', 'Ad_Campaigns_List', 'Date_Range_Start', 'Date_Range_End', 'Num_of_Days', 'Impressions', 'Spend_USD', 'Spend_Range_Min_USD', 'Spend_Range_Max_USD', 'Spend_Range_Min_EUR', 'Spend_Range_Max_EUR', 'Spend_Range_Min_INR', 'Spend_Range_Max_INR', 'Spend_Range_Min_BGN', 'Spend_Range_Max_BGN', 'Spend_Range_Min_HRK', 'Spend_Range_Max_HRK', 'Spend_Range_Min_CZK', 'Spend_Range_Max_CZK', 'Spend_Range_Min_DKK', 'Spend_Range_Max_DKK', 'Spend_Range_Min_HUF', 'Spend_Range_Max_HUF', 'Spend_Range_Min_PLN', 'Spend_Range_Max_PLN', 'Spend_Range_Min_RON', 'Spend_Range_Max_RON', 'Spend_Range_Min_SEK', 'Spend_Range_Max_SEK', 'Spend_Range_Min_GBP', 'Spend_Range_Max_GBP'])
            i = 0
            for row in reader:
                if i == 0:
                    writer.writerow(row)
                    i += 1
                elif row[3] == "US" and row[7] > "2019-01-01":
                    writer.writerow(row)
    csvFile.close()
    csvWriter.close()


filterAdCreatives("google-political-ads-creative-stats.csv")
