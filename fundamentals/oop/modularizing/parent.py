local_val = "magical unicorns"

def square(x):
    return x * x

class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "Hello"

print(square(5))
user = User("Anna")
print(user.name)
print(user.say_hello())

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("test not same", __name__)