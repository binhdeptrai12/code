#### This one is like you scrips with argv
def print_two(*args):
    #### *argv: dont know how many variable of args
    arg1, arg2 = args
    print("arg1: %r ,arg2: %r" % (arg1, arg2))

### ok, that *args isactually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1:%r, arg2:%r" % (arg1, arg2))

## This just take one argument
def print_one(arg1):
    print("arg1:%r" % arg1)

## This one takes no arguments
def print_none():
    print("I got nothing")

print_two("Zed", "Shaw")
print_two_again("Zed","Shaw")
print("First!")
print_none()