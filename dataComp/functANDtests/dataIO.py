#dataIO
import csv

#Input/Output

####CSV input
def firstRow_CSV_reader(string_filename):
    with open(string_filename, newline='') as csvfile:
        reader1 = csv.reader(csvfile, delimiter=',', quotechar='|')
        row_1_list = reader1.__next__()
    return row_1_list

#not fucntional
def singleCol_CSV_reader(string_filename):
    csv_as_list = []
    with open(string_filename, newline='') as csvfile:
        reader1 = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i in reader1:
            csv_as_list.append(i)
    return csv_as_list

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

####CSV Output
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

#misc
def csv_dialect():
    print(csv.list_dialects)
    return
