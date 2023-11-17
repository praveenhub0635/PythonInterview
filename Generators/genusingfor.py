# What happens when we try to access an Element that is not in a range opf Generator?
# We will get an error of STOPITERATION 

def generetators1():
    print("Hello Generator 5:")
    yield 5

    print("Hello Generator 10:")
    yield 10

    print("Hello Generator 15:")
    yield 15

gen = generetators1()
print(gen)

for i in gen:
    print(i)