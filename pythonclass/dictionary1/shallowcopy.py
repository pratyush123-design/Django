origina_dict={"name":"Pratyush","Age":21,"Skills":["Python","Dance"]}
not_perfect_cloning=origina_dict.copy()
not_perfect_cloning["name"]="Alice"
not_perfect_cloning["Skills"].append("javascript")
print("Original dict is: ", origina_dict)
print("shallow copy is: ", not_perfect_cloning)

origina_dict={"name":"Pratyush","Age":21,"Skills":["Python","Dance"]}
not_perfect_cloning=dict(origina_dict)
not_perfect_cloning["name"]="Hari"
not_perfect_cloning["Skills"].append("JS") #append accepts only one argument
print("original dict is:",origina_dict)
print("shallow copy", not_perfect_cloning)

