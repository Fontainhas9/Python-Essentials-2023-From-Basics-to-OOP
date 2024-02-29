if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    transformed_list = list(map(lambda x: x * x, my_list))

    new_transformed_list = []
    for x in my_list:
        new_transformed_list.append(x * x)

    print(new_transformed_list == transformed_list)
