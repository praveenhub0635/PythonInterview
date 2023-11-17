# What do you mean by Generator?
# A Generator is a special type of function which does not return a single value, instead it returns an iterator object with a sequwnce of values
# In Generator YIELD statement is used instead of RETURN
#Generator uses YIELD keyword

# Difference between YIELD and RETURN ?
#YIELD returns a value and passess the execution while maintaining the internal states.
# whereas return statement returns a value and terminates the execution of the function.

# What happens if we use return keyword before yield in a Generator in Python?
# If we use return keyword before yield in Genrator the function won't execute remaining yield statements.It will throw an error if we try to execute.
# When we use return after yiled it first execute yield and then execute return.
#Example

def generetators1():
    print("Hello Generator 5:")
    yield 5

    print("Hello Generator 10:")
    yield 10

    print("Hello Generator 15:")
    yield 15

gen = generetators1()
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))