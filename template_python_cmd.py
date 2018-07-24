#1
import os

cmd = "git --version"

returned_value = os.system(cmd)  # returns the exit code in unix
print('returned value:', returned_value)

#2
import subprocess

cmd = "git --version"

returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
print('returned value:', returned_value)

#3
import subprocess

cmd = "date"

# returns output as byte string
returned_output = subprocess.check_output(cmd)

# using decode() function to convert byte string to string
print('Current date is:', returned_output.decode("utf-8"))
