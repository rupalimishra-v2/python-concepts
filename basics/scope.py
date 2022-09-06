# Scope - what variables do I have access to?
def outer():
    x = "local"
    def inner():
        x = "innerlocal"
        def inner1():
            nonlocal x
            print("inner in inner1:", x)
            x = "nonlocal"
            print("inner1:", x)
        inner1()
        print("inner:", x)
    inner()
    print("outer:", x)
outer()

#1 - start with local
#2 - Parent local
#3 - global
#4 - built in python functions