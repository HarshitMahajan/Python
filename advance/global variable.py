#progream with a global variable
def fun():
    global s
    print(s)
    s="i love india"
    print(s)

s="i love world"
fun()
print(s)
