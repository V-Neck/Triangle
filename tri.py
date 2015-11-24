BLANK = " "

f = open("Triangle.txt", "w+")
def trim(s):
    while(s[0] == BLANK):
        s =  s[1:]
    while(s[-1] == BLANK):
        s = s[:-1]
    return ltos(s)

def ltos(l):
    s = ""
    for i in l:
        s += i
    return s


triangle = []

def tri(width, iteration):
    if iteration == 0:
        line  = BLANK*(width/2 -1 )
        line += "#"
        line += BLANK*(width/2)
        triangle.append(line)
    else:
        tri(width, iteration-1)
        for i in range(0,2**(iteration-1)):
            char = trim(triangle[i]) +BLANK*(2**(iteration) - 2*(i) -1) + trim(triangle[i])
            ws = BLANK*( ((width - len(char))/2) )
            triangle.append(ws + char + ws)
n = 8
tri(2**n, n-1)

for i in triangle:
    for j in i:
        f.write( j,)
    f.write("\n")
