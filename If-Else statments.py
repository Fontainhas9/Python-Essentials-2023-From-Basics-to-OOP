if __name__ == '__main__':
    length = 800

    if length < 500:
        print("Small")
    elif 500 <= length < 1000:
        print("Medium")
    elif 1000 <= length < 2000:
        print("Large")
    else:
        print("Huge")

    is_premier_member = True
    days_registered = 400
    special_acess_code = False

    if (is_premier_member and days_registered > 365) or special_acess_code:
        print("You have access to the premium content")
    else:
        print("You do not have access to the premium content")
