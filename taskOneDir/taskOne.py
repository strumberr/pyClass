input_array = [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]

result_dict = {}

for el in input_array:
    if el not in result_dict:
        result_dict[el] = 1
    else:
        result_dict[el] += 1

print(max(result_dict.values()))