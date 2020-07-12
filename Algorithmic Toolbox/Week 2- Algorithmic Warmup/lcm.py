x, y = [int(i) for i in input().split()]

def gcd(x,y):
    if y == 0:
        return x
    z = x%y
    return gcd(x,y)

if x>y:
    gcd2 = gcd(x,y)
else:
    gcd2 = gcd(y,x)

print(x*y//gcd2)