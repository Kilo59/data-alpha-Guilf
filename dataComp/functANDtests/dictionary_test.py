import gspread
from oauth2client.service_account import ServiceAccountCredentials #to authorize GAPP access

#####|Google Sheet Setup|#####
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
print("****************************")
#setup well_data worksheet & well_grouping worksheet objects
well_data = g_sheet.worksheet('well_data')
well_grouping = g_sheet.worksheet('well_grouping')
###############################

####|Grouping Begin|##
#######TESTING DICTIONARY STRUCTURE
group_dict = well_grouping.get_all_records(empty2zero = False, head = 1)

group_list = []

#loop through dictionary of well_grouping worksheet values
#ignore empty groups, append group names of the rest to a list
for d in group_dict:
    for group_name in d:
        print(group_name, d[group_name])
        if d[group_name] == '':
            print("None")
        else:
            if group_name not in group_list:
                group_list.append(group_name)

print("**********")
print(group_list)



'''
print(group_dict)
print(group_dict[0])
print(group_dict[1])
print(group_dict[2])
print(group_dict[0]['Group_16'])
print(group_dict[1]['Group_16'])

for i in range(len(group_dict)):
    print(len(group_dict[i]))
    if group_dict[i]['Group_16'] != '':  # if not empty
        print(group_dict[i]['Group_16'])

for i in range(len(group_dict)):
    print(len(group_dict[i]))
    if group_dict[i]['Group_4'] != '':
        print(group_dict[i]['Group_4'])
'''
####|Grouping End|##