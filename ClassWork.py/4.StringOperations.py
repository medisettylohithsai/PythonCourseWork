# ============================
# String Operations (No Methods)
# ============================

# Original string
text = "Hello Python"
print("Original String:", text)
print()

# ----- 1. Indexing -----
print("Indexing:")
print("Character at index 0:", text[0])
print("Character at index 6:", text[6])
print("Last character:", text[-1])
print()

# ----- 2. Slicing -----
print("Slicing:")
print("text[0:5] :", text[0:5])       # Hello
print("text[6:]  :", text[6:])        # Python
print("text[:5]  :", text[:5])        # Hello
print("text[2:8] :", text[2:8])       # llo Py
print()

# ----- 3. Concatenation (+) -----
print("Concatenation:")
a = "Hello"
b = "World"
print("a + b:", a + b)
print("a + ' ' + b:", a + " " + b)
print()

# ----- 4. Repetition (*) -----
print("Repetition:")
print("a * 3:", a * 3)
print("'Hi' * 5:", "Hi" * 5)
print()

# ----- 5. Membership (in / not in) -----
print("Membership:")
print("'Hello' in text:", "Hello" in text)     # True
print("'World' in text:", "World" in text)     # False
print("'Py' not in text:", "Py" not in text)   # False
print("'Java' not in text:", "Java" not in text)  # True
print()

# ----- 6. Comparison (==, !=) -----
print("Comparison:")
x = "apple"
y = "apple"
z = "banana"

print("x == y:", x == y)     # True
print("x == z:", x == z)     # False
print("x != z:", x != z)     # True
print()
