import json
x='{"name":"Hero" , "age": 19 , "Sahar": "Kohalpur"}'
y=json.loads(x)
print(y["Sahar"])

import json
json_string='{"name":"Hero" , "age": 19 , "Sahar": "Kohalpur"}'
python_obj=json.loads(json_string)
print(python_obj)

# import JSON into python

import json

json_string = '{"name": "Hero", "age": 19, "Sahar": "Kohalpur"}'

python_obj = json.loads(json_string)
print(python_obj)


