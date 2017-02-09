"""
    changes the datase and time stamp of the servers
    you can use any command to change as we are using 
    ssh -t to force a sudo tty at the client end
#   Force pseudo-terminal allocation. This can be used to execute arbitrary screen-based programs on a remote machine, which can be very useful, e.g. when implementing menu services. Multiple -t options force tty allocation, even if ssh has no local tty.
"""


import os,sys

user="nchawla@"
ip=raw_input("enter the ip")
l=ip.split('.')
# take the input from command line

first_octet=l[0]
second_octet=l[1]
third_octet=l[2]
fourth_octet=l[3]
command='date'

for fourth_octet in range(81,90):
	command="date"
	os.system("ssh -t "+user+
          	first_octet+'.'+
          	second_octet+'.'+
          	third_octet+'.'+
          	str(fourth_octet)+" "+command)


