#DataCowboy.py
#SpaceTuna8

def pl_rdr_labels(list_of_columns):
    colA = []
    colB = []
    colC = []
    colD = []
    colE = []
    colF = []
    colG = []
    colH = []
    colI = []
    colJ = []
    colK = []
    colL = []
    colM = []
    colN = []
    colO = []
    colP = []
    colQ = []
    colR = []
    colS = []
    colT = []
    column_list = [colA, colB, colC, colD, colE, colF, colG, colH, colI, colJ, colK, colL, colM, colN, colO, colP, colQ, colR, colS, colT]
    for row in list_of_columns:
        for cell, index in zip(row, range(len(column_list))):
            column_list[index].append(cell)
    return column_list

#Merge a list of lists into a single list
def pl_rdr_single_list(list_of_columns):
    single_list = []
    list_of_list = pl_rdr_labels(list_of_columns)
    for a_list in list_of_list:
        for item in a_list:
            single_list.append(item)
    return single_list

'''
####Accept a single list (from CSV) stored row by row
##Example [A1, B1, C1, A2, B2, C2, A3, B3, C3
def single_list_to_grouped_list(single_list):
    list_of_list = []
    for i in single_list:

    return list_of_list
'''