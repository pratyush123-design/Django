import json

json_string = '{"name": "Hero", "age": 19, "Sahar": "Kohalpur"}'

python_obj = json.loads(json_string)
print(python_obj)
