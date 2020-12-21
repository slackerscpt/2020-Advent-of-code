import re

allergen_dict = dict()
food_set = set()
food_list = []

for line in [line.strip() for line in open('input.txt')]:
    ingredients, allergens = line.split(' (contains ')
    foods = ingredients.split()
    food_set = set.union(food_set, set(foods))
    food_list.extend(foods)
    allergens = re.split(r', | |\)', allergens)[:-1]
    for allergen in allergens:
        allergen_dict[allergen] = set.intersection(allergen_dict[allergen], set(foods)) if allergen in allergen_dict else set(foods)

while sum([len(c) for c in allergen_dict.values()]) != len(allergen_dict):
    uniques = [list(s)[0] for s in allergen_dict.values() if len(s) == 1]
    for unique in uniques:
        for candidates in allergen_dict.values():
            if unique in candidates and len(candidates) != 1:
                candidates.remove(unique)

safe_foods = set.union(*allergen_dict.values()) ^ food_set
count = sum([food_list.count(food) for food in safe_foods])
print(f'Part 1 Answer: {count}')

allergen_foods = ','.join([list(allergen_dict[key])[0] for key in sorted(allergen_dict)])
print(f"Part 2 Answer: {allergen_foods}")