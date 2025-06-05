import copy
origina_dict={"name":"Pratyush","Age":21,"Skills":["Python","Dance"]}
not_perfect_cloning=copy.deepcopy(origina_dict)
not_perfect_cloning["name"]="Alice"
not_perfect_cloning["Skills"].append("javascript")
print("Original dict is: ", origina_dict)
print("deep copy is: ", not_perfect_cloning)
