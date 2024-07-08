#-------------------global scope = > when function not find the value in own scope then pick with global scope-----------------------
userName = "singhashish"

def func():
    # userName = "Ashish"
    print(userName)

func()
print(userName)


# x = 10 
# def func(y):
#     z = x + y 
#     return z

# result = func(1)
# print(result)

# x = 99
# def func3():
#     global x
#     x = 88
# func3()
# print(x) # 88

# x = 99
# def f1():
#     # x = 88
#     def f2():
#         print(x)
#     f2()
# f1()

x = 99
def f1():
    x = 88
    def f2():
        print(x)
    return f2

myResult = f1()
myResult()

def singhashish(num):
    def actual(x):
        return x ** num
    return actual


f = singhashish(2)
g = singhashish(3)
print(f(3))
print(g(3))






