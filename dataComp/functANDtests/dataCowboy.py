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
    column_list = [colA, colB, colC, colD, colE, colF, colG, colH, colH, colI, colJ, colK, colL, colM, colN, colO, colP, colQ, colR, colS, colT]
    for row in list_of_columns:
        for cell, index in zip(row, range(len(column_list))):
            column_list[index].append(cell)

    return column_list
