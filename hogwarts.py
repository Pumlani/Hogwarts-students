# List of students' names
students = ["Hermione", "Harry", "Ron", "Draco"]

# Iterating over each student in the list and printing their name
for student in students:
    print(student)

# Iterating over each index in the range of the length of the list
for i in range(len(students)):
    # Printing the index incremented by 1 (to start from 1 instead of 0) and the corresponding student's name
    print(i + 1, students[i])
