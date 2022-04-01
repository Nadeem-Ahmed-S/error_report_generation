import re
import sys
import os

#Used to store an argument passed from the makefile
cmd_arg = sys.argv[1];

#Variable : Pattern
#Pattern that you want to search for
if(cmd_arg == 'simulate'):
  pattern = '^\#\ \*\* Error';
elif(cmd_arg == 'compile'):
  pattern = '^\*\* Error';

#Variable : command
#Command that you want to run on the terminal
command = 'make ' + cmd_arg 

#The fubction that runs the command on the terminal
os.system(command);

def line_loop(arg,log_file,file_name):
  for line in log_file:
    match = re.search(arg,line);
    if(match):
      print("**-------------------------Error Report-------------------------**")
      print(line)
      print("**--------------------------------------------------------------**")
      count = count + 1;
      with open(cmd_arg+"_error_log.log",'a') as file_name:
        file_name.write(line)
        file_name.close()


log_file = open(cmd_arg+"_log.log",'r');

file_name = cmd_arg + "_error_log"

count = 0;

line_loop(pattern,log_file,file_name);
log_file.close();

if(count != 0):
  log_file = open(cmd_arg+"_log.log",'r');
  line_loop("Errors",log_file,file_name);
  log_file.close();

