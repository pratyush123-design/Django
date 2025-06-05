import json

def txt_to_json(txt_file, json_file):
    data = {}
    with open(txt_file) as f:
        for line in f:
            if ': ' in line:
                parts = line.strip().split(': ', 1)
                data[parts[0]] = parts[1]
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=2)

def json_to_txt(json_file, txt_file):
    with open(json_file) as f:
        data = json.load(f)
    with open(txt_file, 'w') as f:
        for key in data:
            f.write(f"{key}: {data[key]}\n")
