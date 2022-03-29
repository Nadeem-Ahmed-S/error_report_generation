import re
import sys
import os

pattern = 'Error'
a = 0

#f1 = open("file1.log",'w+')

line1 = "make compile"
os.system(line1);

print("--------------Error Report-----------")

with open("compile_log.log",'r') as f:
  for line in f:
    match = re.search(pattern,line);
    if(match):
      print(line)
      if(a==0):
        with open("./error_log_file.log",'w+') as f1:
          a = 1
          f1.write(line)
          f1.close()
      else:
        with open("./error_log_file.log",'a') as f1:
          f1.write(line)
          f1.close()
    
print("--------------------------------------")

