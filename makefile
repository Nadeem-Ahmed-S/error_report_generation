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

clean_compile:
	rm -rf work/ error_log_file.log

compile_py:
	python error_report_generation.py

#compile_err
#compile_err:
#	grep ^**Error
