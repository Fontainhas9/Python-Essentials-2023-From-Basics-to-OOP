if __name__ == '__main__':
    my_dictionary = {"name": "John", "age": 25}
    my_dictionary = dict(name='John', age=25)  # same as before

    my_dictionary["age"] = 26  # Updates the age to 26
    print(my_dictionary['age'])

    # Combining Data Structures
    students = [
        {"name": "John", "grades": (90, 85, 88)},
        {"name": "Jane", "grades": [92, 82, 78]}
    ]
    print(students[0]["grades"][1])  # Outputs: 85
