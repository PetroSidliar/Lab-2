a_list = ["a", "", "c", "", "e"]

empty_strings = []
for string in a_list:
    if (string != ""):
        empty_strings.append(string)

print(empty_strings)
