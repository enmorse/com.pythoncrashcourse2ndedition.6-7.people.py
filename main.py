# Start with the program you wrote for Exercise
# 6-1 (page 99). Make two new dictionaries
# representing different people, and store all three
# dictionaries in a list called people. Loop through
# your list of people. As you loop through the list,
# print everything you know about each person.

parents = {
    "abruce": {
        "first_name": "Bruce",
        "last_name": "Morse",
        "relationship": "Father",
        "age": 74,
        "city": "San Diego"
    },
    "ajanet": {
        "first_name": "Janet",
        "last_name": "Morse",
        "maiden_name": "McElwee",
        "relationship": "Mother",
        "age": 69,
        "city": "San Diego"
    },
}

for key, value in parents.items():
    print(f"\nUsername: {key}")
    print(f"Information: {value}")
