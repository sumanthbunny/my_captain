n = int(input("enter how many digits to be printed"))
t1 = 0
t2 = 1

for x in range(1, n+1 , 1):
    print(t1)
    nxt = t1 + t2
    t1 = t2
    t2 = nxt
