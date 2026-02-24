
a = 2
b = 1
c = 2
d = 2

def pack4(a,b,c,d):
    if a == 0:
        a,b,c,d = b,c,d,0
    if b == 0:
        b,c,d = c,d,0
    if c == 0:
        c,d = d,0
    if a == b:
        a,b,c,d = a*2,c,d,0
    if b == c:
        b,c,d = b*2,d,0
    if a == 0:
        a,b,c,d = b,c,d,0
    if c == d:
        c,d = c*2,0
    if a == 0:
        a,b,c,d = b,c,d,0
    return(a,b,c,d)


a,b,c,d = pack4(a,b,c,d)

print(a,b,c,d)