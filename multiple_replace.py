string = "abcd"
replace_dict = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}
for k, v in replace_dict.items():
    string = string.replace(k, v)

print(string)  # output: ABCD
