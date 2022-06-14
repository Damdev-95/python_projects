#first_name = "Sulaiman"
#surname = "Olubiyi"
#print("My first name is {}. My family name is {}".format(first_name, surname))

#my_int = 50
#sentence = "The total comes to: "

#print(sentence + (my_int)()

# TypeError: can only concatenate str (not "int") to str

#string = "This is a string over\nthree lines\n\n\twith the third line indented"
#print(string)

persons = [{"name": "halimah", "location": "Ilorin", "Gender": "Female", "occupation": "Fashionist"},
        {"name": "abike", "location": "Abuja", "Gender": "Female", "occupation": "Pharmacist"},
        {"name": "sulaiman", "location": "Ibadan", "Gender": "Male", "occupation": "Teacher"},
        {"name": "damilare", "location": "Lagos", "Gender": "Male", "occupation": "Cloud Engineer"}]

for person in persons:
    print("My profile is", person)