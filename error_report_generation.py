import re
import sys
import os

#Used to store command argument passed from the makefile
cmd_arg = sys.argv[1];

if(cmd_arg == "simulate"):
  #Used to store testname argument passed from the makefile
  test_name = sys.argv[2];
  #Used to store verbosity argument passed from the makefile
  verbosity = sys.argv[3];

#The below variable is protocol specific
prot_name = "axi4_"

#Variable : Pattern
#Pattern that you want to search for
if(cmd_arg == 'simulate'):
  pattern = '^\#\ \*\* Error';
elif(cmd_arg == 'compile'):
  pattern = '^\*\* Error';

#Variable : command
#Command that you want to run on the terminal
if(cmd_arg == 'compile'):
  command = 'make ' + cmd_arg  
elif(cmd_arg == 'simulate'):
  command = 'make' + ' ' + cmd_arg + ' ' +'test=' + test_name + ' ' + 'uvm_verbosity=' + verbosity 

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

#Assigning error file name to error_file variable
if(cmd_arg == "compile"):
  error_file = prot_name+cmd_arg+"_error.log";
elif(cmd_arg == "simulate"):
  error_file = test_name+"/"+test_name+"_error.log";

#Opening the log file and passing it to the frunction and closing it.
if(cmd_arg == "compile"):
  log_file = open(prot_name+cmd_arg+".log",'r');
elif(cmd_arg == "simulate"):
  log_file = open(test_name+"/"+test_name+".log",'r');

write_into_error_file(pattern,log_file,error_file);
log_file.close();

#Opening the log file and passing it to the frunction and closing it.
if(cmd_arg == "compile"):
  log_file = open(prot_name+cmd_arg+".log",'r');
elif(cmd_arg == "simulate"):
  log_file = open(test_name+"/"+test_name+".log",'r');

if(os.path.exists(cmd_arg+"_error.log")):
  write_into_error_file("Errors",log_file,error_file);
else:
  for line in log_file:
    match = re.search("Errors",line);
    if(match):
      print(line)
log_file.close();

print("Log file path : "+prot_name+cmd_arg+".log");
if(os.path.exists(cmd_arg+"_error.log")):
  print("Error log file :" + error_file)

print("**--------------------------------------------------------------**")

