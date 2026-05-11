# PYTHON OPERATORS

a = 10
b = 3

# 1. Arithmetic Operators
print("Arithmetic Operators")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print("a // b =", a // b)

# 2. Assignment Operators
print("\nAssignment Operators")
x = 5
print("x =", x)
x += 2
print("x += 2 ->", x)
x -= 1
print("x -= 1 ->", x)
x *= 3
print("x *= 3 ->", x)
x /= 2
print("x /= 2 ->", x)
x %= 2
print("x %= 2 ->", x)

# 3. Comparison Operators
print("\nComparison Operators")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# 4. Logical Operators
print("\nLogical Operators")
p = True
q = False
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

# 5. Identity Operators
print("\nIdentity Operators")
m = [1, 2, 3]
n = m
o = [1, 2, 3]
print("m is n:", m is n)
print("m is o:", m is o)
print("m is not o:", m is not o)

# 6. Membership Operators
print("\nMembership Operators")
fruits = ["apple", "banana", "mango"]
print("'apple' in fruits:", "apple" in fruits)
print("'grape' in fruits:", "grape" in fruits)
print("'grape' not in fruits:", "grape" not in fruits)

# 7. Bitwise Operators
print("\nBitwise Operators")
x = 5   # 0101
y = 3   # 0011
print("x & y =", x & y)
print("x | y =", x | y)
print("x ^ y =", x ^ y)
print("~x =", ~x)
print("x << 1 =", x << 1)
print("x >> 1 =", x >> 1)