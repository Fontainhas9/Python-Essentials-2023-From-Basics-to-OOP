if __name__ == '__main__':
    fruits = ['banana', 'orange', 'mango', 'lemon']

    for fruit in fruits:
        print(fruit)

    for i in range(len(fruits)):
        print(fruits[i])

    for i, fruit in enumerate(fruits):
        print(i, fruit)

    for i in range(3):
        for j in range(3):
            print(f"i={i}, j={j}")

    count = 0
    while count < 5:
        print(count)
        count += 1
