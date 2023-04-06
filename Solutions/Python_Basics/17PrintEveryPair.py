import string
strings = string.ascii_lowercase

for i in strings:
    for g in strings:
        print(f"{i}{g}")