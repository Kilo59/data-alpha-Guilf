#config_wr_test.py
#test reading and writing to config file
from functANDtests import dataIO
from functANDtests import dataCowboy
from functANDtests import RunTime
from configparser import SafeConfigParser
import sys

print(dataIO.get_start_cond('run'))

dataIO.change_config('start_conditions', 'run', 'False')
