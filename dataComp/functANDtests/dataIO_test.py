import dataIO
import dataCowboy
import RunTime
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials #to authorize GAPP access


#Working Sheet Name
google_sheet_name = 'plate_wells'
#Setup GoogleApp Authrization/Credentials
auth_filename = 'Authorization.json'
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_filename, scope)
gc = gspread.authorize(credentials)
##open spreadsheet by 'title'
g_sheet = gc.open(google_sheet_name)
#setup worksheet variables
well_labels = g_sheet.worksheet('well_labels')

#count columns
number_of_cols = well_labels.col_count

####Get All Data####
get_all_start = RunTime.currentTime()#start-time
#parse data as lists
#each row = list
list_of_lists = well_labels.get_all_values()
column_list = dataCowboy.pl_rdr_labels(list_of_lists)

get_all_end = RunTime.currentTime()#Store script process_end_time
get_all_runTime = RunTime.calc_runTime(get_all_start, get_all_end)
####END Get All####

####Get-By-Column####
by_col_start = RunTime.currentTime()#start-time
col_list = []
for number in range(1,number_of_cols+1):
    col_list.append(well_labels.col_values(number))

by_col_end = RunTime.currentTime()#Store script process_end_time
by_col_runTime = RunTime.calc_runTime(by_col_start, by_col_end)
####END Get-By-Column####

print(get_all_runTime)

print(column_list)
print(list_of_lists)

print(by_col_runTime)
print(col_list)

print(len(column_list))
print(column_list)
print(number_of_cols)

'''
col1 = []
col2 = []
header_list = ['Alpha', 'Bravo']


for i in range(50):
    col1.append(1+i)
    col2.append(random.randrange(1,25))

print(header_list[0],len(col1), col1)
print(header_list[1],len(col2), col2)

col_list = [col1, col2]
unequal_list = [col1, header_list]

print(col_list)

dataIO.singleCol_CSV('test1.csv', header_list[0], col1)
dataIO.doubleCol_CSV('test2.csv', header_list, col_list)
#dataIO.doubleCol_CSV('errorTest.csv', header_list, unequal_list)
'''

for number in range(1,5):
    print(number)


dataIO.csv_dialect()

skiped_row = dataIO.skipRows_CSV_reader("raw_plate_reader.csv", 2)
col_header = dataIO.firstRow_CSV_reader("raw_plate_reader.csv")
csv_list = dataIO.readAll_CSV_reader("raw_plate_reader.csv")
