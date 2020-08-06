l = []
n = int(input("enter no. of inputs"))
for x in range(0, n, 1):
    ele = int(input())
    l.append(ele)
print("required list is:")
for x in l:
    if x > 0:
        print(x)
