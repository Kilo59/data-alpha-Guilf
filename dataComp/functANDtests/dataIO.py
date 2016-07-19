#dataIO
import csv
from configparser import SafeConfigParser

#############Local Input/Output######

###reading from Config file
parser = SafeConfigParser()
parser.read('config.ini')
def get_tolerance(req_name):
    tolerance = parser.getfloat('tolerance', req_name)
    return tolerance
def get_start_cond(condition_name):
    condition = parser.getboolean('start_conditions', condition_name)
    return condition
###CSV info gathering

#modified from jamylak @StackOverflow
def count_rows_CSV(string_filename):
    with open(string_filename,"r") as f:
        reader = csv.reader(f,delimiter = ",")
        data = list(reader)
        row_count = len(data)
    return row_count

#modified from mgilson @StackOverflow
def count_columns_CSV(string_filename):
    d = ','
    f=open(string_filename,'r')

    reader0=csv.reader(f,delimiter=d)
    ncol=len(next(reader0)) # Read first line and count columns
    return ncol

def count_rowsXcols(string_filename):
    result = count_columns_CSV(string_filename) * count_rows_CSV(string_filename)
    return result

####CSV input
def firstRow_CSV_reader(string_filename):
    with open(string_filename, newline='') as csvfile:
        reader1 = csv.reader(csvfile, delimiter=',', quotechar='|')
        row_1_list = reader1.__next__()
    return row_1_list

def skipRows_CSV_reader(string_filename, num_skiped_rows):
    csv_as_list = []
    with open(string_filename, newline='') as csvfile:
        reader1 = csv.reader(csvfile, delimiter=',', quotechar='|')
        for number in range(1, num_skiped_rows + 1):
            next(reader1)
        for i in reader1:
            csv_as_list.append(i)
    return csv_as_list

def readAll_CSV_reader(string_filename):
    csv_as_list = []
    with open(string_filename, newline='') as csvfile:
        reader1 = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i in reader1:
            csv_as_list.append(i)
    return csv_as_list

def csv_list_of_lists(string_filename):
    headers = firstRow_CSV_reader(string_filename)
    with open(string_filename) as csvfile:
        reader3 = csv.DictReader(csvfile)
        list1 = [[] for x in range(len(headers))]
        for ls, header in zip(list1, headers):
            ls.append(header)
        for row in reader3:
            #print(row['Time'], row['Well 101'], row['Well 300'])
            for col_list in list1:
                col_list.append(row[col_list[0]])
    return list1

########|CSV Output|########

'''
#length of each list must be the same
def colList_to_rowList(list_of_columns):
    #lists should have the same length
    list_of_rows = list_n( len(list_of_columns[0]) )

    list_of_rows[0].append(list_of_columns[0][0])
    list_of_rows[0].append(list_of_columns[1][0])
    list_of_rows[0].append(list_of_columns[2][0])

    list_of_rows[1].append(list_of_columns[0][1])
    list_of_rows[1].append(list_of_columns[1][1])
    list_of_rows[1].append(list_of_columns[2][1])

    list_of_rows[2].append(list_of_columns[0][2])
    list_of_rows[2].append(list_of_columns[1][2])
    list_of_rows[2].append(list_of_columns[2][2])

    list_of_rows[3].append(list_of_columns[0][3])
    list_of_rows[3].append(list_of_columns[1][3])
    list_of_rows[3].append(list_of_columns[2][3])

    return list_of_rows
'''
#**used in multiCol_CSV function**
#takes a list of lists (where each list repesents a column of data)
#sorts it into to a list of list where each list represents a row
#Example input:     [ [header1, 0.1, 0.10], [header2, 0.2, 0.20] ]
#Example output:    [ [header1, header2], [0.1, 0.2], [0.10, 0.20] ]
def cols_to_rows_list(list_of_columns):
    #lists should have the same length
    list_of_rows = list_n( len(list_of_columns[0]) )
    for index, row in enumerate(list_of_rows):
        for ls_index in range( len(list_of_columns) ):
            #print(index, ls_index)
            row.append(list_of_columns[ls_index][index])
    return list_of_rows

def multiCol_CSV(filename, list_of_columns):
    row_list = cols_to_rows_list(list_of_columns)
    print("***Written to CSV file***")
    with open(filename, 'w', newline='') as csvfile:
        writer1 = csv.writer(csvfile, delimiter=',')
        for index, ls in enumerate(row_list):
            #print(ls)
            writer1.writerow(ls)
    return

def singleCol_CSV(string_filename, string_header, item_list):
    with open(string_filename, 'w', newline='') as csvfile:
        writer1 = csv.writer(csvfile, delimiter= ',')
        writer1.writerow([string_header])
        for i in range(len(item_list)):
            writer1.writerow([item_list[i]])
    return


#Columns must be past be passed in as a list of lists, each with the same length
def doubleCol_CSV(filename, header_list, list_of_columns):
    with open(filename, 'w', newline='') as csvfile:
        writer2 = csv.writer(csvfile, delimiter=',')
        if len(list_of_columns[0]) != len(list_of_columns[1]):
            print("ERROR: Columns must have the same number of items")
            writer2.writerow( ['ERROR: Columns must have the same number of items'] )
        else:
            writer2.writerow([header_list[0], header_list[1]])
            for i in range(len(list_of_columns[0])):
                writer2.writerow([ list_of_columns[0][i],list_of_columns[1][i] ])
    return

##########|Misc|#################

#return an empty list of lists of size variable size
def list_n(size_of_list):
    ls = [[] for i in range(size_of_list)]
    return ls

def csv_dialect():
    print(csv.list_dialects)
    return

def print_data_lists(list_of_lists):
    for i in range(len(list_of_lists)):
        print(list_of_lists[i][0], list_of_lists[i][1:])
    return
