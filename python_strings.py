if __name__ == '__main__':
    string = "Python"
    print(string[0])  # P

    print(string[1:4])  # yth
    print(string[::2])  # Pto

    # string[0] = "C" #Can't do this

    job = 'Software Developer'

    print(f"If you learn Python you can be a {job}")

    print("If you learn Python you can be a {job}".format(job=job))
