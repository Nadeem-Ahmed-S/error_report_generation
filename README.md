# error_report_generation
A Python script to create a log file to capture the errors in compilation and simulation

# To compile and genrate a log file for compilation:
make compile

# To compile and genrate a separate log for compilation errrors:
make run type="compile"

# To simulate and genrate a log file for simulation:
make simulate

# To simulate and genrate a separate log for simulation errrors:
make run type="simulate"

# Python commands to execute the compileation and simulation
# To compile and genrate a separate log for compilation errrors:
python error_report_generation compile

# To simulate and genrate a separate log for simulation errrors:
python error_report_generation compile
