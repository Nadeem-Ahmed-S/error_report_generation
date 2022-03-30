import re
import sys
import os

#f1 = open("file1.log",'w+')

#Variable : Pattern
#Pattern that you want to search for
pattern = 'Error';

cmd_arg = sys.argv[1];

#Variable : compile_command
#Command that you want to run on the terminal
compile_command = "make compile";

#Variable : simulate_command
#Command that you want to run on the terminal
simulate_command = "make simulate";

if(cmd_arg == "compile"):
  command = compile_command;
elif(cmd_arg == "simulate"):
  command = simulate_command;

#The fubction that runs the command on the terminal
os.system(command);

print("--------------Error Report-----------")

#with open("compile_log.log",'r') as compile_log:

if(cmd_arg == "compile"):
  log_file = open("compile_log.log",'r');
elif(cmd_arg == "simulate"):
  log_file = open("simulate_log.log",'r');

for line in log_file:
  match = re.search(pattern,line);
  if(match):
    print(line)
    if(cmd_arg == "compile"):
      with open("./compile_error_log.log",'a') as compile_error_log:
        compile_error_log.write(line)
        compile_error_log.close()
    elif(cmd_arg == "simulate"):
      with open("./simulate_error_log.log",'a') as simulate_error_log:
        simulate_error_log.write(line)
        simulate_error_log.close()

log_file.close()

print("--------------------------------------")

#Another way to generate the error report
#
#a = 0
#
#print("--------------Error Report-----------")
#
#with open("compile_log.log",'r') as f:
#  for line in f:
#    match = re.search(pattern,line);
#    if(match):
#      print(line)
#      if(a==0):
#        with open("./error_log_file.log",'a') as f1:
#          a = 1
#          f1.write(line)
#          f1.close()
#      else:
#        with open("./error_log_file.log",'a') as f1:
#          f1.write(line)
#          f1.close()
#    
#print("--------------------------------------")

