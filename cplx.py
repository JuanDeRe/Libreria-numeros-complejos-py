import math
test1a = (2,3)
test1b = (5,-1)
test2a = (0,10)
test2b = (1.5,-7)

def sumacplx(tup1,tup2):
    return((tup1[0]+tup2[0],tup1[1]+tup2[1]))

def restacplx(tup1,tup2):
    return((tup1[0]-tup2[0],tup1[1]-tup2[1]))

def multpcplx(tup1,tup2):
    return(((tup1[0]*tup2[0])-(tup1[1]*tup2[1]),(tup1[0]*tup2[1])+(tup1[1]*tup2[0])))

def divcplx(tup1,tup2):
    if tup2[0] == 0 and tup2[1] == 0:
        return("Operacion no definida.")
    return(((tup1[0]*tup2[0])+(tup1[1]+tup2[1]))/((tup2[0])**2+(tup2[1])**2),((tup2[0]*tup1[1])-(tup1[0]*tup2[1]))/((tup2[0])**2+(tup2[1])**2))

def modcplx(tup):
    return((tup[0]**2)+(tup[1]**2))**0.5

def conjcplx(tup):
    return(tup[0],-tup[1])

def fasecplx(tup):
    return math.atan(tup[1]/tup[0])

def cart_polarcplx(tup):
    p = modcplx(tup)
    theta = fasecplx(tup)
    return (p,theta)
def polar_cartcplx(p,theta):
    return((p*math.cos(theta),p*math.sin(theta)))


