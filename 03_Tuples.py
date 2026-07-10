print("--- TUPLES IN PYTHON\n ---")
# 1. Initialization and Syntax Nuances
print("--- 1. Initialization & Type Verification ---")
# Tuples are ordered, indexable, and structurally immutable sequences.
empty_tup = ()
print(f"Empty Tuple: {empty_tup} | Type: {type(empty_tup)}")

# CRITICAL NUANCE: A single-element tuple requires a trailing comma.
# Without the comma, Python evaluates it as a standard integer/string expression.
invalid_single = (5)   # Interpreted as integer <int>
valid_single = (5,)    # Correctly interpreted as tuple <tuple>

print(f"Without Comma: {invalid_single} | Type: {type(invalid_single)}")
print(f"With Trailing Comma: {valid_single} | Type: {type(valid_single)}")

# Multi-element tuple containing homogeneous or heterogeneous data
standard_tup = (87, 93, 45, 93, "Python", True)
print(f"Standard Tuple: {standard_tup}\n")


# 2. Immutability Demonstration
print("--- 2. The Core Rule: Immutability ---")
# Tuples cannot be modified after creation. Attempting to assign a new value 
# to a specific index will raise a TypeError.

print("Example: standard_tup[0] = 99 will crash the program with a TypeError.")
# Uncommenting the line below will trigger: TypeError: 'tuple' object does not support item assignment
# standard_tup[0] = 99 

print("Status: Tuple immutability securely verified.\n")


# 3. Accessing Elements (Indexing & Advanced Slicing)
print("--- 3. Indexing & Slicing Operations ---")
sample_tup = (10, 20, 30, 40, 50, 60)
print(f"Target Tuple: {sample_tup}")

# Positional and Negative Indexing
print(f"Element at Index 1: {sample_tup[1]}")
print(f"Element at Index -1: {sample_tup[-1]}")

# Slicing syntax -> tuple[start : stop : step]
print(f"Slice [1:4]: {sample_tup[1:4]}")
print(f"Slice [:3]: {sample_tup[:3]}")
print(f"Slice [2:]: {sample_tup[2:]}")
print(f"Slice with Step [::2]: {sample_tup[::2]}")
print(f"Reversed Tuple using Slicing [::-1]: {sample_tup[::-1]}\n")


# 4. Built-in Tuple Methods
print("--- 4. Core Tuple Methods ---")
methods_tup = (12, 45, 67, 45, 89, 45, 100)
print(f"Working Tuple: {methods_tup}")

# Method 1: .count(value) -> Returns the total occurrences of an element
count_45 = methods_tup.count(45)
print(f"Method [.count()]: Occurrences of number 45 -> {count_45}")

# Method 2: .index(value) -> Returns the first index of occurrence
# Throws a ValueError if the item does not exist.
first_index_45 = methods_tup.index(45)
print(f"Method [.index()]: First index position of 45 -> {first_index_45}\n")


# 5. Advanced Mechanics: Unpacking & Operations
print("--- 5. Advanced Tuple Mechanics ---")

# Tuple Unpacking: Mapping elements to descriptive variables cleanly
coordinates = (28.6139, 77.2090)
latitude, longitude = coordinates
print(f"Unpacked Latitude: {latitude}")
print(f"Unpacked Longitude: {longitude}")

# Tuple Concatenation (Joining two tuples into a new instance)
tup_a = (1, 2)
tup_b = (3, 4)
combined_tup = tup_a + tup_b
print(f"Concatenation (tup_a + tup_b): {combined_tup}")

# Tuple Replication (Multiplying sequences)
replicated_tup = tup_a * 3
print(f"Replication (tup_a * 3): {replicated_tup}")

# Membership Testing using 'in' operator
has_sixty_seven = 67 in methods_tup
print(f"Membership Test: Is 67 present in methods_tup? -> {has_sixty_seven}\n")
