# Creating a list
fruits = ["apple", "banana", "cherry", "date"]

# Printing the entire list
print("List of fruits:", fruits)

# Accessing elements in a list by index
print("First fruit:", fruits[0])  # Output: apple
print("Second fruit:", fruits[1])  # Output: banana

# Negative indexing (accessing elements from the end)
print("Last fruit:", fruits[-1])  # Output: date
print("Second last fruit:", fruits[-2])  # Output: cherry

# Slicing a list (getting a sublist)
print("First two fruits:", fruits[0:2])  # Output: ['apple', 'banana']
print("Fruits from index 1 to 3:", fruits[1:4])  # Output: ['banana', 'cherry', 'date']

# Modifying an element in the list
fruits[1] = "blueberry"
print("Updated list of fruits:", fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']

# Adding an element to the end of the list
fruits.append("elderberry")
print("List after appending:", fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry']

# Removing an element from the list
fruits.remove("cherry")
print("List after removing 'cherry':", fruits)  # Output: ['apple', 'blueberry', 'date', 'elderberry']

# Checking if an element exists in the list
if "banana" in fruits:
    print("Banana is in the list")
else:
    print("Banana is not in the list")  # Output: Banana is not in the list

# Length of the list
print("Number of fruits in the list:", len(fruits))  # Output: 4

# Looping through the list
print("Fruits in the list:")
for fruit in fruits:
    print(fruit)

# List comprehension (creating a new list based on existing list)
uppercase_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", uppercase_fruits)  # Output: ['APPLE', 'BLUEBERRY', 'DATE', 'ELDERBERRY']

# Clearing the list
fruits.clear()
print("List after clearing:", fruits)  # Output: []