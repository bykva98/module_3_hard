def calculate_structure_sum (*args):
    final_sum = 0
    for element in args:
        if type(element) == (int or float):
            final_sum += element
        elif type(element) == str:
            final_sum += len(element)
        elif isinstance(element, (list, set, tuple)):
            final_sum += calculate_structure_sum(*element)
        elif isinstance(element, dict):
            for i, k in element.items():
                final_sum += calculate_structure_sum(i) + calculate_structure_sum(k)
    return final_sum


data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)