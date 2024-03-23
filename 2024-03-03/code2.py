import json

my_dict = {
    "name":"hong",
    "job":"student",
    "age":"23"
}

my_json = json.dumps(my_dict, indent=3)
print(my_json, type(my_json))