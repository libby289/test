def f(user_name):
    def g(x):
        print(user_name,x)
    return g
g1=f("haha")
g1(1)
g1(2)