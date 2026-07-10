print("\n--- Questions & Solutions (Interactive) ---")

# Question 1: Ask the user to enter names of their 3 favorite movies & store them in a list.
print("\n--- Q1: Favorite Movies List ---")
movies = []
mov1 = input("Enter 1st favorite movie: ")
mov2 = input("Enter 2nd favorite movie: ")
mov3 = input("Enter 3rd favorite movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print("Your Favorite Movies List:", movies)


# Question 2: Write a program to check if a list contains a palindrome of elements.
print("\n--- Q2: Palindrome List Check ---")
# Let's take dynamic inputs to build a list for the palindrome check
user_list = []
print("Let's build a list of 3 elements to check for a palindrome:")
user_list.append(input("Enter 1st element: "))
user_list.append(input("Enter 2nd element: "))
user_list.append(input("Enter 3rd element: "))

# Logic to check palindrome
list_copy = user_list.copy()
list_copy.reverse()

if list_copy == user_list:
    print(f"The list {user_list} is a Palindrome!")
else:
    print(f"The list {user_list} is NOT a Palindrome.")


# Question 3: Write a program to count the number of students with the 'A' grade in a tuple.
print("\n--- Q3 & Q4: Grade Counter & Sorter ---")
# Pre-defined tuple from the lecture problem statement
grade_tuple = ("C", "D", "A", "A", "B", "B", "A")
print("Given student grades:", grade_tuple)

count_A = grade_tuple.count("A")
print(f"Number of students with 'A' grade: {count_A}")

# Question 4: Store the above values in a list & sort them from 'A' to 'D'.
grade_list = list(grade_tuple)
grade_list.sort()
print("Sorted Grades List:", grade_list)