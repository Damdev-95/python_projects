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
When this code is run, the interpreter will define a special variable called __name__ and assign the value of "__main__" to the code in this python file. So the code in our python file becomes __name__ == "__main__".

When we use import statements, we can import code from other files into our python program. When this happens, the imported code is set a __name__ value of the modules name.

By setting the __name__=="__main__" we can control the order in which the code in this file is executed, telling python to run the code in this file which has the name of __main__ rather than the code imported from another file. This avoids situations where your code could run an imported script, resulting in unwanted behavior.

We do this using an if statement. If statements are covered in more detail later. At this stage, all you need to understand is that it is telling the python interpreter that if the __name__ is equal to __main__ which relates to the code in this python file, then run the main() function.

The main() function therefore sets the start point for our code to control the order in which our code executes. It is conventional to include all the calls to your functions within the main() function. This will help others to read your code and understand the logic and flow

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
# OR

```
import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

### Change below this line only ###

kwargs={
    "Text":"I am learning to code in AWS",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"fr"
    }

def main():
    translate_text(**kwargs)

if __name__=="__main__":
    main()

```
# Step 1 - User input from the console
In our Amazon Translate example, we have provided the values directly in the code. What if we want to provide the values as user input at the time we run the program?

In this step, we learn how to provide user input when the program is run and pass this to the function.
# The input() function
```
import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

### Change below this line only ###

text = input("Provide the text you want translating: ")
source_language_code = input("Provide the two letter source language code: ")
target_language_code = input("Provide the two letter target language code: ") 

def main():
    translate_text(
        Text=text,
        SourceLanguageCode=source_language_code,
        TargetLanguageCode=target_language_code
        )

if __name__=="__main__":
    main()

```
# ARGUMENT PARSER

```
import argparse # argparse is a built in python package, we add it with an import statement
import boto3

# Define the parser variable to equal argparse.ArgumentParser()
parser = argparse.ArgumentParser(description="Provides translation between one source language and another of the same set of languages.")

# Add each of the arguments using the parser.add_argument() method
parser.add_argument(
    '--text',
    dest="Text",
    type=str,
    help="The text to translate. The text string can be a maximum of 5,000 bytes long. Depending on your character set, this may be fewer than 5,000 characters",
    required=True
    )

parser.add_argument(
    '--source-language-code', 
    dest="SourceLanguageCode", 
    type=str, 
    help="The language code for the language of the source text. The language must be a language supported by Amazon Translate.",
    required=True
    )

parser.add_argument(
    '--target-language-code',
    dest="TargetLanguageCode",
    type=str,
    help="The language code requested for the language of the target text. The language must be a language support by Amazon Translate.",
    required=True
    )

# This will inspect the command line, convert each argument to the appropriate type and then invoke the appropriate action.
args = parser.parse_args()

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

def main():
    # vars() is an inbuilt function which returns a dictionary object
    translate_text(**vars(args))

if __name__=="__main__":
    main()
```
* To run the program, enter the following command in the terminal:

`python lab_5_step_2_cli_arguments.py --text "we are learning python on AWS" --source-language-code en --target-language-code fr`

* We have added the parameters on the command line.

* Each parameter relates to each block for parser.add_argument

# INPUT FILE 

```
def open_input(file):
    with open(file, 'r') as f:
        text = f.read() #We use read() to read the actual contents of the file
        print(text)

def main():
    open_input("text.txt")

if __name__=="__main__":
    main()

```
# TEXT.TXT
```
"AWS Sysops Administrator Associate"
```

# What did python do?
* Python used text.txt as an input parameter for the file.
* It used with open() to open the file and r as read-only.
* It used the .read() method to read the contents of the file and assign it to the variable text.
* It printed the variable to return the sentence.

# Step 4 - JSON
JSON  stands for Javascript Object Notation and is pronounced "jason". It is a very similar structure to python dictionaries and lists, with only a few exceptions. It is a very common format for computer programs to exchange information in using Application Programming Interfaces (APIs).

![image](https://user-images.githubusercontent.com/71001536/173601807-cfc71493-534e-4c2c-abde-2c3e3410290a.png)

# json.loads() & json.dumps()
Before we use an external file it is worth spending time learning about json.loads() and json.dumps(). These two methods use JSON strings, denoted by the 's'. When learning to manipulate JSON it is easy to get confused between json.loads() and json.load() or json.dumps() and json.dump().

Here is the easy way to know which to use.

json.load() & json.dump() - Use to input and output JSON from files and into files.
json.loads() & json.dumps() - Use to input and outputting JSON from strings and into strings.
