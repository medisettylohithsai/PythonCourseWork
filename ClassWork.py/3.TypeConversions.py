# ===============================
# Python Type Conversion Program
# Made for Beginners
# ===============================

print("---- Integer Conversions ----")
num = 10
print("Original:", num, "| Type:", type(num))

print("int to float:", float(num), "| Type:", type(float(num)))
print("int to string:", str(num), "| Type:", type(str(num)))
print("int to boolean:", bool(num), "| Type:", type(bool(num)))
print("int to complex:", complex(num), "| Type:", type(complex(num)))
print()


print("---- Float Conversions ----")
pi = 3.14
print("Original:", pi, "| Type:", type(pi))

print("float to int:", int(pi), "| Type:", type(int(pi)))
print("float to string:", str(pi), "| Type:", type(str(pi)))
print("float to boolean:", bool(pi), "| Type:", type(bool(pi)))
print("float to complex:", complex(pi), "| Type:", type(complex(pi)))
print()


print("---- String Conversions ----")
"""the character string cannot be converted into the int,float.. so i take numeric string here....."""
text = "25"   # numeric string 
print("Original:", text, "| Type:", type(text))

print("string to int:", int(text), "| Type:", type(int(text)))
print("string to float:", float(text), "| Type:", type(float(text)))
print("string to boolean:", bool(text), "| Type:", type(bool(text)))
print("string to complex:", complex(text), "| Type:", type(complex(text)))
print()


print("---- Boolean Conversions ----")
flag = True
print("Original:", flag, "| Type:", type(flag))

print("bool to int:", int(flag), "| Type:", type(int(flag)))
print("bool to float:", float(flag), "| Type:", type(float(flag)))
print("bool to string:", str(flag), "| Type:", type(str(flag)))
print("bool to complex:", complex(flag), "| Type:", type(complex(flag)))
print()


print("---- Complex Conversions ----")
c = 5 + 2j
print("Original:", c, "| Type:", type(c))

# NOTE: complex → int/float is not allowed directly
print("complex to string:", str(c), "| Type:", type(str(c)))
print("complex to boolean:", bool(c), "| Type:", type(bool(c)))
print()


print("---- List Conversion ----")
list_data = [1, 2, 3]
print("Original:", list_data, "| Type:", type(list_data))

print("list to tuple:", tuple(list_data), "| Type:", type(tuple(list_data)))
print("list to string:", str(list_data), "| Type:", type(str(list_data)))
print("list to set:", set(list_data), "| Type:", type(set(list_data)))
print("list to set:", set(list_data), "| Type:", type(bool(list_data)))
print()


print("---- Tuple Conversion ----")
tuple_data = (10, 20, 30)
print("Original:", tuple_data, "| Type:", type(tuple_data))

print("tuple to list:", list(tuple_data), "| Type:", type(list(tuple_data)))
print("tuple to string:", str(tuple_data), "| Type:", type(str(tuple_data)))
print("tuple to set:", set(tuple_data), "| Type:", type(set(tuple_data)))
print("tuple to set:", set(tuple_data), "| Type:", type(bool(tuple_data)))
print()


print("---- Set Conversion ----")
set_data = {5, 6, 7}
print("Original:", set_data, "| Type:", type(set_data))

print("set to list:", list(set_data), "| Type:", type(list(set_data)))
print("set to tuple:", tuple(set_data), "| Type:", type(tuple(set_data)))
print("set to string:", str(set_data), "| Type:", type(str(set_data)))
print("set to string:", str(set_data), "| Type:", type(bool(set_data)))
print()


print("---- Dictionary Conversion ----")
data = {"name": "Lohith", "age": 20}
print("Original:", data, "| Type:", type(data))

print("dict to string:", str(data), "| Type:", type(str(data)))
print("dict to list (keys):", list(data), "| Type:", type(list(data)))
print("dict to tuple (keys):", tuple(data), "| Type:", type(tuple(data)))
print("dict to list (keys):", list(data), "| Type:", type(set(data)))
print("dict to list (keys):", list(data), "| Type:", type(bool(data)))
print()
