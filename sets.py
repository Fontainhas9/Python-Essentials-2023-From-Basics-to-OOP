if __name__ == '__main__':
    my_set = {1, 2, 3, 5, 4}
    print(my_set)

    my_set.add(6)
    print(my_set)
    my_set.update([7, 8])
    print(my_set)

    my_set.remove(8)  # raises error if element is not present
    my_set.discard(10)  # does not raise error if element is not present

    print(my_set)

    # SET OPERATIONS
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print(a | b)  # union
    print(a & b)  # intersection
    print(a - b)  # difference

    x = [1, 2, 3, 4, 5]
    print(x)
    print("Set X", set(x))
