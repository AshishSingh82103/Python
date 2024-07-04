#-------------------global scope = > when function not find the value in own scope then pick with global scope-----------------------
userName = "singhashish"

def func():
    # userName = "Ashish"
    print(userName)

func()
print(userName)


x = 10 
def func(y):
    z = x + y 
    return (x + y)

result = func(1)
print(result)






