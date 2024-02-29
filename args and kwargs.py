def func_with_args_and_kwargs(*args, **kwargs):
    print(f"Arguments were: {args}")
    print(f"Type of args: {type(args)}")
    print(f"Keyword arguments were: {kwargs}")
    print(f"Type of kwargs: {type(kwargs)}")


def common_function(age, name, job, **kwargs):
    formatted_info = {
        "age": age,
        "name": name,
        "job": job,
        'description': f"{name} is a {age} year old {job}.",
        "other_info": kwargs
    }
    return formatted_info


if __name__ == '__main__':
    func_with_args_and_kwargs(1, 2, 3, a=4, b=5, c=6)
    age, name, job = 30, 'John', 'Software Developer'
    print(common_function(age, name, job, city='New York', country='USA'))
