
a = 0
b = 0
c = 0

def pack3(a,b,c):
    if a == 0:
        a,b,c = b, c, 0
    if b == 0:
        b,c = c,0
    if a == b:
        a,b,c = a*2,c,0
    if b == c:
        a,b,c = a,b*2,0
    if a == 0:
        a,b,c = b,c,0
    return(a,b,c)


a,b,c = pack3(a,b,c)

print(a,b,c)
