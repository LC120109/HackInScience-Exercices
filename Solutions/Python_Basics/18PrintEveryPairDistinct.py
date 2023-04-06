import string
strings = string.ascii_lowercase

for i in strings:
    for g in strings:
        if i == g:
            continue
        else:
            print(f"{i}{g}")