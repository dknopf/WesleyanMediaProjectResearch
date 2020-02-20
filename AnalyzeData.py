import csv

def count_text(csv_in):
    with open(csv_in, 'r', newline='', encoding="utf-8") as csvFile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='"')
        counter_text = 0
        counter_violated = 0
        for row in reader:
            if row[2] == 'Text' and row[3] == 'US':
                counter_text += 1
                if row[39] == 'Ad violated Google policy':
                    counter_violated += 1
        return (counter_text, counter_violated)




ad_text_stats = count_text('googleAdCreatives.csv')
print("The number of valid text ads is", ad_text_stats[0] - ad_text_stats[1], "and the number of text ads that violated Google's ad policy is", ad_text_stats[1])
