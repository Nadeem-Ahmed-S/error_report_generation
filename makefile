#.IGNORE:
#	compile
#	simulate

.SILENT:
	compile
	simulate
	usage

usage:
	echo "";
	echo "--------------------------------------------";
	echo "           Error File Generation            ";
	echo "--------------------------------------------";
	echo "";
	echo "Use the below command for compilation:";
	echo "make compile";
	echo "";
	echo "Use the below command for compilation and to generate the error_log_file:";
	echo "make run type="compile"";
	echo "";
	echo "Use the below command for simulation:";
	echo "make simulate";
	echo "";
	echo "Use the below command for compilation and to generate the error_log_file:";
	echo "make run type="simulate"";
	echo "";

#compile
compile:
	make clean_compile;
	make clean_simulate;
	vlib work;
	vlog -sv \
	+acc     \
	+cover   \
	+fcover  \
	-l compile_log.log \
	top.sv;  
	#-f file.f

	#make compile_py;

simulate:
	#mkdir $(test_folder)

	# Use -novopt for no optimization - Makes the simulation slower
	# vsim -pli finesim.so -coverage top
	vsim -vopt \
	work.top \
	-voptargs=+acc=npr \
	-assertdebug \
	+UVM_VERBOSITY=$(uvm_verbosity) \
	-l simulate_log.log \
	-sva \
  -coverage \
	-c -do " run -all; exit"


clean_compile:
	rm -rf work/ compile_log.log compile_error_log.log

clean_simulate:
	rm -rf work/ simulate_log.log vsim.wlf vish_stacktrace.vstf simulate_error_log.log

clean:
	make clean_compile;
	make clean_simulate;

run:
	python error_report_generation.py $(type)

#simulate_py:
#	python error_report_generation.py $(type)

