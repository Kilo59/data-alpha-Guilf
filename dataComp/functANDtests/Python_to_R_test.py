#Author:SpaceTuna8
import dataIO
<<<<<<< HEAD
import subprocess
=======

>>>>>>> refs/remotes/origin/master
# => [1, 2, 3, ... 49, 50]
data_list = [x for x in range(1,51)]

dataIO.singleCol_CSV("Py_R_test1.csv", "ColumnHeader", data_list)
<<<<<<< HEAD
str(data_list)

#define command and argument
command = 'Rsrcipt'
path2script = 'fromPython.R'

#build subprocess command
cmd = [command, path2script] + data_list

#check_output will run command and store to result
x = subprocess.check_output(cmd, univsersal_newlines=True)

print('The maximum of the numbers is:', x)
=======
>>>>>>> refs/remotes/origin/master
