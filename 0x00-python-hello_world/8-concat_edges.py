class MyString:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

obj = MyString("object-oriented programming with Python")
print(obj)
