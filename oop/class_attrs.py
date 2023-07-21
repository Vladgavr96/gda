class TestClass():
    test_attr = 1


my_object1 = TestClass()
my_object2 = TestClass()

my_object2.test_attr = 3

TestClass.test_attr = 2

print(my_object1.test_attr)
print(my_object2.test_attr)