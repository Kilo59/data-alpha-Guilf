#init_reader.py
#Author: SpaceTuna8
#Purpose:Read 256x301 CSV file
from functANDtests import RunTime #to calculate script run-time
from functANDtests import demoFunc #various computational functions
from functANDtests import dataIO #for data input/Output

start_time = RunTime.currentTime()#Store script start-time

#read and store column headers from csvfile
colHeaders = dataIO.singleRow_CSVreader("raw_plate_reader.csv")
print(colHeaders)


proccess_end_time = RunTime.currentTime()#Store script process_end_time
process_runTime = RunTime.calc_runTime(start_time, proccess_end_time)
