strings = ["a", "b", "c", "d"]

# LookUp O(1)
# Get an element
print(strings[2])

# Push O(1) Can be O(n) if array need to be relocated
# Add element at the end
strings.append("e")
print(strings)

# Pop O(1)
# Delete last element
strings.pop()
print(strings)

# Insert O(n)
# Add an element in any position
strings.insert(0, "x")
strings.insert(3, "y")
print(strings)

# Delete O(n)
# Delete an element in any position
strings.remove("x")
print(strings)
