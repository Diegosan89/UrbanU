# Введение в функциональное программирование

def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        results.update({function.__name__: function(int_list)})
    return results
    pass


list_ = [16, 48, 0, 9, 78.5, 22, -5]
miracle = apply_all_func(list_, min, max, len, sum, sorted)
print(miracle)