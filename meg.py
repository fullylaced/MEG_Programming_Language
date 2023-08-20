import sys
import subprocess

# Make output.py as the output file, does not use pipping.
testFile = open('output.py','w')
tab = 0
keywords = ['TRUE', 'FALSE', 'OR', 'AND', 'WHILE', 'IF']
ints = []
strings = []
bools = []

# Checks to make sure variable name isn't a keyword and that it starts with
# a letter of the alphabet.
def valid_var_name(var):
    if not var[0].isalpha():
        return False
    if var.upper() in keywords:
        return False
    else:
        return True


# Different error cases that make sure to print out the error in console and
# in the output.py file. This is because we would not want the code to continue
# if there were any errors, since if the error was in a loop or condition we would
# want to stop the code and display the error instead of trying to write it into the
# code and continuing.
def error(val):
    global tab
    testFile.close()
    testFile1 = open('output.py','w')
    if val == 0:
        testFile1.write('print(\'Error: Must have a valid file name or cli as argument\')\n')
    elif val == 1:
        testFile1.write('print(\'Error: Illegal variable name\')\n')
    elif val == 2:
        testFile1.write('print(\'Error: Illegal for loop arguments\')\n')
    elif val == 3:
        testFile1.write('print(\'Error: There must be a . at the end of the line\')\n')
    elif val == 4:
        testFile1.write('print(\'Error: Conditional operator not valid\')\n')
    elif val == 5:
        testFile1.write('print(\'Error: Only allowed to print one variable at once\')\n')
    elif val == 6:
        testFile1.write('print(\'Error: Cannot use same variable name for different variable type\')\n')
    elif val == 7:
        testFile1.write('print(\'Error: Expecting a number or int variable\')\n')
    elif val == 8:
        testFile1.write('print(\'Error: Expecting an operator\')\n')
    elif val == 9:
        testFile1.write('print(\'Error: Cannot end bool expression with operator\')\n')
    elif val == 10:
        testFile1.write('print(\'Error: Must have a valid file name or cli as argument\')\n')
    elif val == 11:
        testFile1.write('print(\'Error: No keyword or oprator found\')\n')
    elif val == 12:
        testFile1.write('print(\'Error: Need more arguments for var assignment\')\n')
    elif val == 13:
        testFile1.write('print(\'Error: Variable has not been declared yet\')\n')
    testFile1.close()
    subprocess.run('python3 output.py',shell=True)
    exit(0)


# Checks for any command line arguments and runs accordingly
def cli(args, args_size):
    if(args_size == 2):
       if('-h' in args[1]):
          print("USAGE HELP:")
          print("python3 meg.py *test text file name* -> output in output.py")
          print("python3 meg.py -h -> shows help")
          print("python3 meg.py *test text file name* -h -> output in output.py and shows help")
          print("python3 meg.py *test text file name* -run -> output in output.py and runs it")
          print("python3 meg.py *test text file name* *variables*")
          print("Use the README for more information")
          exit(0)

    if(args_size == 3):
       if('-h' in args[2]):
          print("USAGE HELP:")
          print("python3 meg.py *test text file name* -> output in output.py")
          print("python3 meg.py -h -> shows help")
          print("python3 meg.py *test text file name* -h -> output in output.py and shows help")
          print("python3 meg.py *test text file name* -run -> output in output.py and runs it")
          print("python3 meg.py *test text file name* *variables*")
          print("Use the README for more information")


# This is our variation of a for loop. It takes in a starting value,
# a destination value, and an increment value then runs through until
# the end.
def for_loop(line):
    global tab
    line = line.replace('.', '')
    temp = line.strip().split()
    if len(temp) != 7 or '[' not in temp:
        error(2)
    testFile.write('\t' * tab + 'for ' + temp[1] + ' in range(' + temp[3] + ', ' + temp[4] + ', ' + temp[5] + '):\n')
    tab += 1


# End for loop, makes sure tabs are correct for python
def end_for_loop(line):
    global tab
    tab -= 1


# This is our if conditions. We have 6 different if conditions:
# if equal to, if not equal to, if greater than, if less than,
# if less than equal to, and if greater than equal to. This is used
# to compare ints.
def if_condition(line):
    global tab
    line = line.replace('.', '')
    temp = line.strip().split()
    if temp[0] == 'ifeq':
        testFile.write('\t' * tab + 'if ' + temp[1] + ' == ' + temp[2] + ':\n')
    elif temp[0] == 'ifneq':
        testFile.write('\t' * tab + 'if not ' + temp[1] + ' == ' + temp[2] + ':\n')
    elif temp[0] == 'ifgt':
        testFile.write('\t' * tab + 'if ' + temp[1] + ' > ' + temp[2] + ':\n')
    elif temp[0] == 'iflt':
        testFile.write('\t' * tab + 'if ' + temp[1] + ' < ' + temp[2] + ':\n')
    elif temp[0] == 'iflteq':
        testFile.write('\t' * tab + 'if ' + temp[1] + ' <= ' + temp[2] + ':\n')
    elif temp[0] == 'ifgteq':
        testFile.write('\t' * tab + 'if ' + temp[1] + ' >= ' + temp[2] + ':\n')
    else:
        error(4)
    tab += 1


# This assgins ints to variables. It works to assign an int to a
# value or to another int already declared. It ensures that it is
# an integer value, as well as the variable has already been declared
# in that instance.
def int_assign(line):
    global tab
    line2 = line.strip()
    if not line2[-1] == '.':
        error(3)
    temp = line2.strip().strip('.').split()
    if not valid_var_name(temp[1]):
        error(1)
    if temp[1] in bools or temp[1] in strings:
        error(6)
    if len(temp) < 4:
        error(12)
    if len(temp) == 4:
        if temp[3].strip('-').isnumeric() or temp[3] in ints:
            testFile.write('\t' * tab + temp[1] + ' = ' + temp[3]+'\n')
        else:
            error(7)
    else:
        check = 0
        final = ''
        for i in range(3, len(temp)):
            if check == 0:
                if temp[i].strip('-').isnumeric() or temp[i] in ints:
                    check = 1
                    final += temp[i]
                else:
                    error(7)
            else:
                if temp[i] in '+-*/%':
                    check = 0
                    if temp[i] == '/':
                        final += '/'
                    final += temp[i]
                else:
                    error(8)
        if temp[-1] in '+-*/%':
            error(7)
        testFile.write('\t' * tab + temp[1] + ' = ' + final+'\n')
    ints.append(temp[1])


# This assigns a variable to a string. This only works for strings,
# not already declared strings, such as x = y where y is a string would
# not work. This also makes sure that the spaces are preserved.
def string_assign(line):
    global tab
    line2 = line.strip()
    if not line2[-1] == '.':
        error(3)
    temp = line2.strip().strip('.').split()
    final = ' '.join(temp[3:])[1:-1]
    if not valid_var_name(temp[1]):
        error(1)
    if temp[1] in ints or temp[1] in bools:
        error(6)
    if len(temp) < 4:
        error(12)
    word = '"' + final + '"'
    if temp[1] in strings:
    	testFile.write('\t' * tab + temp[1] + ' += ' + word + '\n')
    else:
    	testFile.write('\t' * tab + temp[1] + ' = ' + word + '\n')
    	strings.append(temp[1])


# This assigns a bool to a variable. This allows for boolean
# expressions as well as just true or false. It also allows
# for boolean logic with other already declared booleans.
def bool_assign(line):
    global tab
    line2 = line.strip()
    if not line2[-1] == '.':
        error(3)
    temp = line2.strip('.').split()
    if not valid_var_name(temp[1]):
        error(1)
    if temp[1] in ints or temp[1] in strings:
        error(6)
    if len(temp) < 4:
        error(12)
    if len(temp) == 4:
        if temp[3] == 'true':
            testFile.write('\t' * tab + temp[1] + ' = True\n')
        elif temp[3] == 'false':
            testFile.write('\t' * tab + temp[1] + ' = False\n')
    else:
        final = ''
        for i in range(3, len(temp)):
            if temp[i] == '&':
                final += 'and '
            elif temp[i] == '|':
                final += 'or '
            elif temp[i] == '!':
                final += 'not '
            elif temp[i] in bools:
                final += temp[i]
                final += ' '
            elif temp[i] == 'true':
                final += 'True '
            elif temp[i] == 'false':
                final += 'False '
            else:
                error(9)
        if temp[-1] in '&|!':
            error(10)
        testFile.write('\t' * tab + temp[1] + ' = ' + final.strip()+'\n')
    bools.append(temp[1])


# This is used to print out the variable. It only works with single
# variables, not equations.
def print_val(line):
    global tab
    line2 = line.strip()
    if not line2[-1] == '.':
        error(3)
    temp = line2.strip('.').split()
    if not temp[1] in bools and not temp[1] in strings and not temp[1] in ints:
        error(13)
    if len(temp) == 2:
        testFile.write('\t' * tab + 'print(' + temp[1] + ')\n')
    else:
        error(5)


# This is used for taking in specific variables in the command line.
# It will assign them properly to ensure that they are initialized
# in the output.py.
def commands(args):
	for i in range(1, len(args)):
		if args[i] == '_int_':
			j = 1
			line = args[i]
			while '.' not in args[i+j]:
				line += ' '
				if '->' in args[i+j]:
					line += '->'
				else:
					line += args[i+j]
				j += 1
			line += ' '
			line += args[i+j]
			int_assign(line)
		elif args[i] == '_string_':
			j = 1
			line = args[i]
			while '.' not in args[i+j]:
				line += ' '
				if '->' in args[i+j]:
					line += '->'
				else:
					line += args[i+j]
				j += 1
			line += ' '
			line += args[i+j]
			string_assign(line)
		elif args[i] == '_bool_':
			j = 1
			line = args[i]
			while '.' not in args[i+j]:
				line += ' '
				if '->' in args[i+j]:
					line += '->'
				else:
					line += args[i+j]
				j += 1
			line += ' '
			line += args[i+j]
			bool_assign(line)



# This runs through each line in the txt file passed and
# converts it to something that python would understand. 
def file(filename, args):
    global tab
    file = open(filename, 'r')
    if '_int_' in args or '_string_' in args or '_bool_' in args:
    	commands(args)
    for line in file:
        if 'for' in line:
            for_loop(line)
        elif '_int_' in line:
            int_assign(line)
        elif '_string_' in line:
            string_assign(line)
        elif '_bool_' in line:
            bool_assign(line)
        elif 'if' in line:
            if_condition(line)
        elif ']' in line and len(line.strip()) == 1:
            end_for_loop(line)
        elif 'show' in line:
            print_val(line)
        else:
            error(11)


def main():
    arg_list = ['-h','-r']
    args = sys.argv
    args_size = len(sys.argv)
    cli(args, args_size)

    filename = args[1]
    if '.txt' in filename:
        file(filename, args)
        testFile.close()
        if args_size == 3:
            if '-run' in args[2]:
                subprocess.run('python3 output.py',shell=True)
    else:
        error(0)


# Starts code
if __name__ == "__main__":
    main()
