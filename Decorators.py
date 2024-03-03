def announce(f):
    def wrapper():
        print("about to run the function")
        f()
        print("completed function")

    return wrapper


@announce
def hello():
    print("Hello, world!")


hello()
