income = {'Alice': 90000,
          'Bob': 100000,
          'Jeff': 120000,
          'Apiwat': 99999,
          'Stark': 999999}

lowest = min(income, key=income.get)
print("The person with the lowest income:", end=' ')
print(lowest + ' with $' + str(income[lowest]))