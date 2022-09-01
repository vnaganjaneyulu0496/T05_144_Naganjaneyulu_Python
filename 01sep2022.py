                        1) Introduction to Python3:

    Python is a general-purpose interpreted, interactive, object-oriented, and high-level programming
    language.It was created by Guido van Rossum during 1985- 1990.
    ->Python can be used on a server to create web applications.
    ->Python can be used alongside software to create workflows.
    ->Python can connect to database systems. It can also read and modify files.
    ->Python can be used to handle big data and perform complex mathematics.
    ->Python can be used for rapid prototyping, or for production-ready software development.
*Features of Python3:
    ->Interpreted
    ->Platform Independent
    ->Free and Open Source; Redistributable
    ->High-level Language
    ->Robust
    ->Rich Library Support

*Advantages:
    ->Extensive support libraries
    ->Open source and community development
    ->User-friendly data structures
    ->Dynamically typed language
    ->Object-oriented language
    ->Interpreted Language

*Disadvantages:
    ->1.	Slow speed of execution compared to C,C++
    ->2.	Absence from mobile computing and browser


                            2) Variables:

    ->Variables are containers for storing data values.
*Creating Variables:
    ->x = 10
    ->Python will go to the address of x variable
    ->It will take the binary value from that address and converts to decimal format
    ->Returns value to console
    ->We are assigning the value 10 to variable 'x'
    ->Variable is a name which is used to refer memory location of value
    ->Note - Variable name should not be a keyword

                3) IDE (integrated development environment) shortcuts -

It is a software tool that use a programmer to write and test the program and software , while the IDLE is the IDE for
the python . IDE is a software environment which usually consist of a software development package containing code editor,
build automation.

Different types of IDE - PyCharm, Visual Studio Code, Jupyter, Intelli J

1) Ctrl-d - Delete next character in line
2) Ctrl-k - Cut text from cursor to end of line
3) Ctrl-u - Cut text from beginning of line to cursor
4) Ctrl-a - Move cursor to the beginning of the line
5) Ctrl-e - Move cursor to the end of the line
6) Ctrl-b - Move cursor back one character
7) Ctrl-f - Move cursor forward one character
8) Ctrl-y - Yank (i.e. paste) text that was previously cut
9) Ctrl-t - Transpose (i.e., switch) previous two characters
10) Ctrl-p - Access previous command in history
11) Ctrl-n - Access next command in history
12) Ctrl-r - Reverse-search through command history
13) Ctrl-l - Clear terminal screen
14) Ctrl-c - Interrupt current Python command
15) Ctrl-d - Exit IPython session
16) Fn + F5 - Run Python
17) F5  - Execute active script
18) F10 - Display Python Tool Manager.
19) F1 - Trigger Python Editor context help.
20) Ctrl + Z - undo
                        4) Operators

*Python Operators:*
->	operator can be defined as a symbol which is responsible for a particular operation between two operands.
->	Python provides a variety of operators:
->	1.Arithmetic Operators               +  -  *  ** /  //  %
	2.Comparison (Relational) Operators  == != <  >  <=  >=
	3.Assignment Operators		         x = 10
	4.Logical Operators			         and or not
	5.Bitwise Operators
	6.Membership Operators		         in not in
	7.Identity Operators		         is   is not

1.Arithmetic Operators: Arithmetic operators are used to perform arithmetic operations between two operands.
	Operator	Name			Example
	+		  Addition			x + y
	-		  Subtraction		x - y
	*		  Multiplication	x * y
	/		  Division			x / y
	%		  Modulus			x % y
	**		  Exponentiation	x ** y
	//		  Floor division	x // y
2.Comparison (Relational) Operators: Comparison operators are used to comparing the value of the two operands and returns    	Boolean true or false accordingly.
	Operator	Name			Example
	==			Equal			x == y
	!=			Not equal		x != y
	>			Greater than	x > y
	<			Less than		x < y
	>=			Greater than or equal to	x >= y
	<=			Less than or equal to	x <= y
3.Assignment Operators: The assignment operators are used to assign the value of the right expression to the left operand.
	Operator	Example		Same As
	=			x = 5		x = 5
	+=			x += 3		x = x + 3
	-=			x -= 3		x = x - 3
	*=			x *= 3		x = x * 3
	/=			x /= 3		x = x / 3
	%=			x %= 3		x = x % 3
	//=			x //= 3		x = x // 3
	**=			x **= 3		x = x ** 3
	&=			x &= 3		x = x & 3
	|=			x |= 3		x = x | 3
	^=			x ^= 3		x = x ^ 3
	>>=			x >>= 3		x = x >> 3
	<<=			x <<= 3		x = x << 3
4.Logical Operators: The logical operators are used primarily in the expression evaluation to make a decision.
	Operator	Description										Example	Try it
	and 		Returns True if both statements are true		x < 5 and  x < 10
	or			Returns True if one of the statements is true	x < 5 or x < 4
	not			Reverse the result, returns False if the result (x < 5 and x < 10)
				is true	not
5.Membership Operators: Python membership operators are used to check the membership of value inside a Python data structure.
	Operator	Description									Example	Try it
	in 			Returns True if a sequence with the 		x in y
				specified value is present in the object
	not 		in	Returns True if a sequence with the 	x not in y
				specified value is not present in the object
6.Identity Operators: The identity operators are used to decide whether an element certain class or type.
	Operator	Description						Example	Try it
	is 			Returns True if both variables 	x is y
				are the same object
	is 			not	Returns True if both 		x is not y
				variables are not the same object

                        5) Data Types
* Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:
Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: Bool

Numbers      3     int   float   complex
Boolean        1      bool

By using the type() function:
Employee Data : empid, name, sal, address, gender, is_perm
Empid  🡪   int  🡪  101
sal    🡪  float 🡪 2400.32
is_perm ->bool     ->  True
name   -> String  -> “Madhu”
Order_Id -> String -> ”1234567890”
address -> String -> “Guntur, Bapatla”
gender -> String ->  ‘M’  ‘F’

1) Python Numbers
There are three numeric types in Python:
int
float
complex
Variables of numeric types are created:
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))
<class ‘int’>
<class ‘float’>


                        *Tokens and their types

    ->Tokens can be defined as a punctuator mark, reserved words and each individual word in a statement.
    ->Token is the smallest unit inside the given program.
    ->There are following tokens in Python:
        identifiers     operator              literals          Keywords    constant
        Identifiers         Operator        Literals
        x                      =                10

                            6) Keywords

    ->Keywords Are reserved words and has specific meaning in a language and they cannot be used as
      ordinary identifiers

    * Identifiers
    ->An identifier is a variable name. A Python identifier is a name used to identify a variable,
      function name, class name, module name or other object name.
    An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9)
    * Rules for writing Identifiers:
    There are some rules for writing Identifiers.
    But first you must know Python is case sensitive.
    That means Name and name are two different identifiers in Python.