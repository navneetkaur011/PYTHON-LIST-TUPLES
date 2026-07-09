print("--- Basic List Methods ---")
List = ["Banana" ,"Litchi", "A"]

# 1. append(): Adds an element at the end
List.append("b")
print("After append(b):", List) 

# 2. sort(): Sorts the list in ascending order
List.sort() # NOTE:We cannot directly sort a list that contains both strings and integers
print("\nAfter sort():", List) 

# Sort in descending order
List.sort(reverse=True)
print("\nAfter sort(reverse=True):", List)

# 3. reverse(): Reverses the elements of the list
List.reverse()
print("\nAfter reverse():", List)

# 4. insert(): Inserts element at a specific index -> insert(idx, element)
List.insert(2, "$")
print("\nAfter insert(2, $):", List)

# 5. remove(): Removes the first occurrence of an element
List.remove("Litchi")
print("\nAfter remove(Litchi):", List)

# 6. pop(): Removes element at a specific index
List.pop(2)
print("\nAfter pop(2):", List)