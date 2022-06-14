import json

# This uses a json string as an input 

json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr",
        "Required": true
        }
    ]
}
"""

#def main():
#    json_input = json.loads(json_string)
#    print(json_input)

def main():
    json_input = json.loads(json_string)
    indented_format = json.dumps(json_input, indent=2)
    print(indented_format)
    
if __name__=="__main__":
    main()
