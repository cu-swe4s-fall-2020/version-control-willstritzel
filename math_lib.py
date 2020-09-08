import sys
op = sys.argv[1]
a = int(sys.argv[2])
b = int(sys.argv[3])

if op == 'add':
    print(a + b)
elif op == 'sub':
    print (a - b)

else:
    print("unknown operator")
