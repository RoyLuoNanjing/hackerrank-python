s = input()

lower = sorted([c for c in s if c.islower()])
upper = sorted([c for c in s if c.isupper()])
odd_digits = sorted([c for c in s if c.isdigit() and int(c) % 2 != 0])
even_digits = sorted([c for c in s if c.isdigit() and int(c) % 2 == 0])

result = ''.join(lower + upper + odd_digits + even_digits)
print(result)