
FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

already = []

for i in FLAVORS:
    for g in FLAVORS:
        if g==i or g in already:
            continue
        else:
            print(f"{i}, {g}")
        already.append(i)