#.IGNORE:
#	compile
#	simulate

.SILENT:
	compile
	simulate
	usage

usage:
	echo "";
	echo "-------------------------------------------------------------------------------------";
	echo "           								Error File Generation Commands   													 ";
	echo "-------------------------------------------------------------------------------------";
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
	echo "-------------------------------------------------------------------------------------";
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
	-l compile.log \
	-f file.f 

	#make compile_py;

simulate:
	#mkdir $(test_folder)

	# Use -novopt for no optimization - Makes the simulation slower
	# vsim -pli finesim.so -coverage top
	vsim -vopt \
	work.hvl_top \
	work.hdl_top \
	work.tb_master_assertions \
	-voptargs=+acc=npr \
	-assertdebug \
	+UVM_TESTNAME=$(test) \
	+UVM_VERBOSITY=$(uvm_verbosity) \
	-l $(test_folder)/$(test).log \
	-sva \
  -coverage \
	-c -do "log -r /*; add wave -r /*; coverage save -onexit -assert -directive -cvg -codeAll $(test_folder)/$(test)_coverage.ucdb; run -all; exit" \
	-wlf $(test_folder)/waveform.wlf




clean_compile:
	rm -rf work/ compile.log compile_error.log

clean_simulate:
	rm -rf work/ simulate.log vsim.wlf vish_stacktrace.vstf simulate_error.log

clean:
	make clean_compile;
	make clean_simulate;

run:
	python error_report_generation.py $(type)

#simulate_py:
#	python error_report_generation.py $(type)

