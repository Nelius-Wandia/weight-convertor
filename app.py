weight = int(input('What is your weight? '))
unit = input('(K)kgs or (G)grams: ')

if unit.upper() == 'K':
    final_weight = weight * 1000
    print(f"You are {final_weight} grams")
else:
    final_weight = weight * 0.001
    print(f"You are {final_weight} kgs")