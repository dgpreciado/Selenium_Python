def missing_char(str, n):
    if n == str[-1]:
        return str.split(0, n - 1)

    return


print(missing_char("kitten", 4))

print()
