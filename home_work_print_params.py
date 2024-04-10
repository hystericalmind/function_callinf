def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(12, 12, 12)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [99, 'banana', [900]]
values_dict = {'a': 20, 'b': 'cherry', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [90, ' [ (; pyton easy ;) ]']

print_params(*values_list_2, 42)
