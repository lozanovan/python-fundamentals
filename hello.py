
counter=0

for c in range(1, 48):
    for b in range(1, c):
        for a in range(1, b):
            if a**2  + b**2 == c ** 2:
                print('{}, {}, {}'.format(a, b, c))
                counter += 1
print(f"The number of the Pythagorean triples is: {counter}")