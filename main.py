def param_transfer(func):
    def wrapper(arg):
        print("Run function: " + str(func.__name__) + "(), with param: " + str(arg))
        func(arg)

    return wrapper


@param_transfer
def print_sqrt(num):
    print(num * 5)


print_sqrt(4)
