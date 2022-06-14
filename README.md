#  Python_projects
python development for network engineers

## Create a Virtual Environment
A virtual environment in python is a container in which all your code and other python packages reside. It allows you to keep your python configuration separate from other versions on your system. It is a good idea to always use a virtual environment when developing python code.

You can choose a name for your virtual environment such as my_environment, but often you see a virtual environment called venv.

To create a virtual environment we will use the command:

`python -m venv my_venv`

Once the virtual environment has been created, you need to activate it. Once activated, your code runs inside the environment, including any packages you install. To activate the environment use one of the following commands:

# Linux/macOS

`source my_venv/bin/activate`

# Windows (Git-Bash)

`source my_venv/Scripts/activate`

# Windows (PowerShell)

`.\my_venv\Scripts\Activate.ps1`

* To know you are inside the virtual environment your command prompt will have the prefix (my_venv). Now any packages you use will be stored in a folder structure inside your virtual environment.

* To exit from the virtual environment, you type `deactivate` and the command prompt will no longer be prefixed by (my_venv).

```
a_str = "This is an example of a string in quotes" # In python the word string is abbreviated to str
my_float = 5.5
an_integer = 5 # integer is abbreviated to int
shopping_list = ["apples", "oranges", "pears"]
a_dict = {"userId": "JBloggs"} # dictionary is abbreviated to dict
my_var = another_variable # variable is abbreviated to var
test_function = my_function() #function is abbreviated to func
example_tuple = ("apple", "orange", "pear")
boolean_values = True # boolean is abbreviated to bool
```
