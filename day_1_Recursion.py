def rec(n):
    if n == 1:
        print(1)
        return
    print(n)
    rec(n-1)
rec(10)
a=1
def increc(n):
    global a
    if n == 0:
        return 0
    print(a)
    a=a+1
    increc(n-1)
increc(10)
