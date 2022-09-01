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