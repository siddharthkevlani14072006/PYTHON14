#ALGORITHM
1. Start the program.
2. Create a tuple containing different elements.
3. Display the original tuple.
4. Find and display the length of the tuple using len().
5. Display the maximum and minimum values using max() and min().
6. Count the occurrence of an element using count().
7. Find the position of an element using index().
8. Perform slicing to access a range of elements.
9. Perform concatenation using the + operator.
10. Perform repetition using the * operator.
11. Display the final results.
12. Stop the program.

  #CODE
  
# Program to demonstrate Tuples and its functions

numbers = (10, 20, 30, 40, 50, 20, 60)

print("Original Tuple:", numbers)

print("Length:", len(numbers))

print("Maximum:", max(numbers))

print("Minimum:", min(numbers))

print("Count of 20:", numbers.count(20))

print("Index of 40:", numbers.index(40))

print("Slicing:", numbers[1:5])

print("Reverse:", numbers[::-1])

t2 = (70, 80, 90)

print("Concatenation:", numbers + t2)

print("Repetition:", numbers * 2)

print("Element at index 2:", numbers[2])

#OUTPUT
Original Tuple: (10, 20, 30, 40, 50, 20, 60)
Length: 7
Maximum: 60
Minimum: 10
Count of 20: 2
Index of 40: 3
Slicing: (20, 30, 40, 50)
Reverse: (60, 20, 50, 40, 30, 20, 10)
Concatenation: (10, 20, 30, 40, 50, 20, 60, 70, 80, 90)
Repetition: (10, 20, 30, 40, 50, 20, 60, 10, 20, 30, 40, 50, 20, 60)
Element at index 2: 30
