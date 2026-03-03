
a = 2
b = 0
c = 0
d = 2

def pack4(a,b,c,d):
    # Déplacer les zéros vers la gauche
    if a == 0:
        a,b,c,d = b,c,d,0
    if a == 0:
        a,b,c,d = b,c,d,0
    if a == 0:
        a,b,c,d = b,c,d,0
    if b == 0:
        b,c,d = c,d,0
    if b == 0:
        b,c,d = c,d,0
    if c == 0:
        c,d = d,0
    # Fusionner les cases
    if a == b and a != 0:
        a,b,c,d = a*2, c, d, 0
    if b == c and b != 0:
        b,c,d = b*2, d, 0
    if c == d and c != 0:
        c,d = c*2, 0
    # Déplacer à nouveau les zéros après fusion
    if a == 0:
        a,b,c,d = b,c,d,0
    if a == 0:
        a,b,c,d = b,c,d,0
    if b == 0:
        b,c,d = c,d,0
    if c == 0:
        c,d = d,0
    return (a,b,c,d)


a,b,c,d = pack4(a,b,c,d)

print(a,b,c,d)