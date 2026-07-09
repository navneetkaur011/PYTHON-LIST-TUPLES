print("--- Part 1: Lists in Python ---")
# Lists are built-in data types that store a sequence of values.
# They are mutable (can be changed after creation).

marks = [94.4, 85.2, 67.5, 45.1, 99.0]
print("Original List:", marks)
print("Type:", type(marks))
print("Length of List:", len(marks))

# Accessing elements via indexing
print("First element:", marks[0]) # 94.4
print("Last element using negative indexing:", marks[-1]) # 99.0

# Lists can store different data types together
student_info = ["Rahul", 21, "Delhi", 91.5]
print("Mixed Data Type List:", student_info)

# Mutability: Changing elements
student_info[0] = "Rohit"
print("Modified List :", student_info) # ['Rohit', 21, 'Delhi', 91.5]

# List Slicing: list_name[starting_idx : ending_idx] 
print("Sliced Marks (index 1 to 3):", marks[1:4]) # [94.4, 85.2, 67.5, 45.1]
print("Sliced Marks (index 0 to 3):", marks[:4]) # [94.4, 85.2, 67.5, 45.1]
print("Sliced Marks (index 1 to len(marks)):", marks[1:]) # [85.2, 67.5, 45.1, 99.0]
print("Sliced Marks (negative index):", marks[-3:-1]) # [67.5, 45.1] 