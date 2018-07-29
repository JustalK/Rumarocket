import csv

CSV_CITY_FILENAME = './2.csv';
CSV_CITY_PRIMARY_KEY = 'BUSINESS CENTER LOCATION';
CSV_CITY_PRIMARY_KEY_INDEX = 3;
CSV_ALL_FILENAME = './1.csv';
CSV_ALL_BUSINESS_CENTER_LOCATION_INDEX = 8;
CSV_ALL_CITY_INDEX = 10;
CSV_ALL_DATE_OPENED_INDEX = 3;
CSV_ALL_CLOSED_INDEX = 4;
CSV_ALL_ASSIGNED_1_INDEX = 13;
CSV_ALL_ASSIGNED_2_INDEX = 14;
CSV_RESULT_FILENAME = './3.csv'
csv_result = ['"BUSINESS CENTER LOCATION","city/municipality","DATE OPENED","closed","ASSIGNED MANAGEMENT TRAINEE 1","ASSIGNED MANAGEMENT TRAINEE 2"'];

all_city = [];


def sanitize(data):
    return data.strip(' ').upper()

# Reading the first csv for getting all the cities inside of it
with open(CSV_CITY_FILENAME, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar="'")
    for row in csvreader:
	    if sanitize(row[CSV_CITY_PRIMARY_KEY_INDEX]) not in all_city and sanitize(row[CSV_CITY_PRIMARY_KEY_INDEX])!='' and sanitize(row[CSV_CITY_PRIMARY_KEY_INDEX])!=CSV_CITY_PRIMARY_KEY:
             all_city.append(sanitize(row[CSV_CITY_PRIMARY_KEY_INDEX]))			 	 
			
# Reading the big file for getting only the row with the cities inside the first file			
with open(CSV_ALL_FILENAME, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvreader:
	    if sanitize(row[CSV_ALL_BUSINESS_CENTER_LOCATION_INDEX]) in all_city:
		    csv_result.append('"'+row[CSV_ALL_BUSINESS_CENTER_LOCATION_INDEX]+'","'+row[CSV_ALL_CITY_INDEX]+'","'+row[CSV_ALL_DATE_OPENED_INDEX]+'","'+row[CSV_ALL_CLOSED_INDEX]+'","'+row[CSV_ALL_ASSIGNED_1_INDEX]+'","'+row[CSV_ALL_ASSIGNED_2_INDEX]+'"')

# Creating a csv and filling it with the result
with open(CSV_RESULT_FILENAME, "w") as output:
    for line in csv_result:
        output.write(line + '\n')