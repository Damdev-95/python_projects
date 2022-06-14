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


# Creating a requirements.txt file
When you use pip freeze you see all the packages installed into your virtual environment. We need to be able to recreate the set of packages when the code is reused elsewhere. For example, giving the code to someone else or when running it in a different environment. To accomplish this pip uses a requirements.txt file. This file contains a list of all the packages and versions you need to install the new environment.

You can create a requirements.txt file by using the command `pip freeze > requirements.txt`

This will create the requirements.txt file in the current directory.

To install a requirements.txt file in the new virtual environment you type `pip install -r requirements.txt` in the new virtual environment to install all the same packages and dependencies from that file.

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
# Using Variables in Strings
Imagine we want to use the value of a variable in the middle of a string. This can be done a few ways in python.

# .format()
In this method you can use the {} in your string to indicate where the variable should go. Then use .format(variable_name) after the quotation marks. If you have multiple variables, for each variable you use a {}. In the .format() separate each variable with a comma. For example .format(variable_1, variable_2).

```
first_name = "Sulaiman"
surname = "Olubiyi"
print("My first name is {}. My family name is {}".format(first_name, surname))
```

# f strings
Since python version 3.6 it has been possible to use a format called f-strings to include variables in your strings. Some people find this format easier to read.

```
firstname = "Jane"
surname = "Doe"

print(f"My first name is {firstname}. My family name is {surname}")
```

# New Lines and indentation
If you want your text to go over several lines you can use \n and \t. The \ character is called an escape character.

The n tells python to put the text on the next line.
The t tells python to add a tab spacing.

```
string = "This is a string over\nthree lines\n\twith the third line indented"
print(string)

This is a string over
three lines
        with the third line indented
```
# Dictionaries
A dictionary is a way of storing related information in key-value pairs. It uses a key as an identifier and a value to store the information. For example, the key could be first_name and the value could be Ada.

A dictionary when written in python would look like {"first_name":"Ada"}. A dictionary in python is abbreviated to dict and has the following syntax {"key":"value"}. The key is a string providing an identifier and the value can be the same kind of values you would store in a variable.

Dictionaries are very common in AWS, so you will see them frequently.

* They are used to exchange information between different services and functions
* They are returned by Application Programming Interfaces (API)
* They are used as Tag values

# Create
Dictionaries can be created by assigning the key-values you want to store in the dictionary.

Using the python interactive mode, try the following:
```
>>> user = {"first_name":"Ada"}
>>> print(user)
{'first_name': 'Ada'}
```
or if you are going to be adding the contents of the dictionary later, you can declare an empty dictionary. You can create an empty dictionary in two ways:

Assigning {} to a variable, for example:

account_details = {}

or use the dict() constructor:

account_details = dict()

Read
To read the value associated with a key, you need to provide the name of the dictionary and the the value of the key inside square brackets.

Try the following:
```
>>> user = {"first_name":"Ada"}
>>> print(user["first_name"])
Ada
```
# Update
Add a key-value
Dictionaries are mutable, which means they can be changed after you create them. You can add, update or delete the key-value pairs in a dictionary.

To add an additional key-value to a dictionary, provide the dictionary name, the new key in [] and a value after an = sign.

Try the following:
```
>>>user["family_name"] = "Byron"
>>>print(user)
{'first_name': 'Ada', 'family_name': 'Byron'}
```

# Modify a value
To modify a value in a similar way to adding it. You provide the new value after the = sign.
```
user["family_name"] = "Lovelace"
print(user)
{'first_name': 'Ada', 'family_name': 'Lovelace'}
```
# Delete a Key-Value Pair
To remove a key-value pair you use the del statement with the name of the dictionary and the key you want to delete.

```
>>> del user["family_name"]
>>> print(user)
{'first_name': 'Ada'}
```
# FUCTION TO TRANSLATE USING AWS TRANSLATE

```
def translate_text(): 
    response = client.translate_text(
        Text='My name is Sulaiman,I love you Halimah', 
        SourceLanguageCode='en', 
        TargetLanguageCode='fr' 
    )
#### Add the new text below this line ####
    print(response) # this code is inside the function and will print the contents of the variable 'response' 

translate_text() # This line will call our function. Without it, python will not do anything.

```
# USING MAIN FUNCTION

```
import boto3

client = boto3.client('translate')

def translate_text():
    response = client.translate_text(
        Text='I am learning to code in AWS',
        SourceLanguageCode='en',
        TargetLanguageCode='fr'
    )
    print(response) # this code is inside the function and will print the contents of the variable 'response'

def main():
    translate_text()

if __name__=="__main__":
    main()
```
# USING POSITIONAL ARGUMENTS 

```
import boto3

def translate_text(text, source_language_code, target_language_code): # we define the positional arguments in the ()
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text, # we remove the hard coded value
        SourceLanguageCode=source_language_code, # we used the positional argument instead
        TargetLanguageCode=target_language_code
    )
    print(response) 

def main():
    translate_text('I am learning to code in AWS','en','fr') # we provide the value for the arguments when we call the function in the correct positional order.

if __name__=="__main__":
    main()
```
# KEYWORD ARGUMENT

```
import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

def main():
    translate_text(Text='I am learning to code in AWS',SourceLanguageCode='en',TargetLanguageCode='fr')

if __name__=="__main__":
    main()

```
