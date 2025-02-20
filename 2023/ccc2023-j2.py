total = 0

peppers = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000
}

n = int(input())
ingredients = []

for i in range(n):
    ingredients.append(input())

for i in ingredients:
    total += peppers.get(i)

print(total)