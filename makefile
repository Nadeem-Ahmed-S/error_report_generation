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
	echo "make compile_py";
	echo "";

#compile
compile:
	make clean_compile;
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


clean:
	rm -rf work/ error_log_file.log compile_log.log simulate_log.log vsim.wlf vish_stacktrace.vstf simulate_error_log.log

py:
	python error_report_generation.py $(type)

#simulate_py:
#	python error_report_generation.py $(type)

