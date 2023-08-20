
Description:
	MEG is a programming language created to provide simpler connotations and syntax for
	several commonly seen concepts in programming languages and programs as a whole. Once a
	file is written in this language it is then translated to Python through a translator.
	

Requirements:
	Python3 Must be installed on your machine!!!
	
	A machine capable of running creating and saving text files is also required.
	Additionally, certain permissions could stop the creation of files ( This should really not Happen).


Language:
	int declarations:
		<var_name> must start with a character. A variable cannot be named
		true, false, or, and, while, if. These are reserved keywords.
		You can also have operators in this
			_int_ <var_name> -> <integer_val>.
			_int_ test -> 10.
			_int_ test2 -> 10 + 2 / 2.
	string declarations:
			_string_ <var_name> -> (<string_val>).
			_string_ test3 -> (Hello World!).
	boolean declarations:
		You can also have boolean logic in this
			_bool_ <var_name> -> <boolean_value>.
			_bool_ test4 -> true.
			_bool_ test5 -> ! true | test4 & true.
	for loop:
		<var_name> must start with a character
		<val> can be either a number or an already initialized int
		Nested loops work
			for <var_name> -> <val> <val> <val>. [
				*stuff*
			]
	if statement:
		6 different statements possible
		<if> can be ifneq, ifgt, iflt, ifgteq, iflteq, ifeq
			<if> <var_name> <integer_val>. [
				*stuff*
			]
			ifeq x 10. [
				*stuff*
			]
	print:
		Can only display one variable at a time, has to be assigned
			show <var_name>.

Command line arguments:
	-h flag will display the usages, if a test file is given it will run
	-run will run the output.py file so you don't have to type python3 output.py
	without -run, you will have to type python3 output.py to get the output
		python3 meg.py *test text file name*
		python3 meg.py -h
        	python3 meg.py *test text file name* -h
		python3 meg.py *test text file name* -run

Command line variable assignment:
	You would assign ints, strings, and bools like you normally would,
	but there must be '' around the -> in the command line. You also
	need quotes around the strings like shown below.
		python3 meg.py *test text file name* *variables*
		python3 meg.py valid1.txt _int_ x -> 1.
		python3 meg.py valid1.txt _int_ y -> 2. _string_ z -> '(good).'

Example of Complete Program:
	_int_ x -> 0.
	_int_ y -> 50.
	_bool_ z -> false.
	for i -> 0 100 1. [
		for j -> 10 0 -1. [
			ifgteq i y. [
				_int_ x -> x + 1.
			]
		]
	]
	ifeq x 500. [
		_bool_ z -> ! z.
	]
	show x.
	show z.
