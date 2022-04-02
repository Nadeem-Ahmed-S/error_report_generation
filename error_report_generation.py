import re
import sys
import os

#Used to store an argument passed from the makefile
cmd_arg = sys.argv[1];

#The below variable is protocol specific
prot_name = ""

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

#This function is used to print error-lines in terminal and
#to add the errors into the error_log file
def write_into_error_file(pattern_arg,log_file,error_file):
  for line in log_file:
    match = re.search(pattern_arg,line);
    if(match):
      print(line)
      #if(os.path.exists(cmd_arg+"_error.log")):
      with open(error_file,'a') as error_file_local:
        error_file_local.write(line)
        error_file_local.close()


print("**-------------------------Error Report-------------------------**")

error_file = cmd_arg+"_error.log";

#Opening the log file and passing it to the frunction and closing it.
log_file = open(prot_name+cmd_arg+".log",'r');
write_into_error_file(pattern,log_file,error_file);
log_file.close();

#Opening the log file and passing it to the frunction and closing it.
log_file = open(prot_name+cmd_arg+".log",'r');
if(os.path.exists(cmd_arg+"_error.log")):
  write_into_error_file("Errors",log_file,error_file);
log_file.close();

print("Log file path : "+prot_name+cmd_arg+".log");
if(os.path.exists(cmd_arg+"_error.log")):
  print("Error log file :" + error_file)

print("**--------------------------------------------------------------**")



