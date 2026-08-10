d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Start with the first dictionary.
result = d1.copy()

# Add values from the second dictionary.
for key, value in d2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print(result)