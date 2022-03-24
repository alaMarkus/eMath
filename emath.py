import scipy
import matplotlib.pyplot as plt
import numpy as n
import math as m
import array as arr

def acosd(x):
    #print(x)
    return m.acos(x)*180/3.1415

def cosinilause(vastainen, viereinen1,viereinen2):
    a = vastainen
    b = viereinen2
    c = viereinen1
    return acosd(-(m.pow(a,2)-m.pow(b,2)-m.pow(c,2))/(2*b*c))

def cosinilauseSAS(viereinen1,viereinen2,alpha):
    b = viereinen1
    c = viereinen2
    a = m.sqrt(m.pow(b,2)+m.pow(c,2)-2*b*c*m.cos(m.radians(alpha)))
    return a

def cosinilauseKulmalla(a,b,angle):
    c2 = m.pow(a,2)+m.pow(b,2)-(2*a*b*m.cos(angle))
    #print(c2)
    c = m.sqrt(c2)
    #print(c)
    return(c)

def sinilause(b,viereinenkulma,vastainenkulma):
    sinalpha = m.sin(m.radians(viereinenkulma))
    sinbeta = m.sin(m.radians(vastainenkulma))
    a = sinalpha*b/sinbeta
    #print("sinilause:")
    #print(a)
    return a

def point(x0,y0,distance,alpha):
    x = x0 + (distance*m.cos(m.radians(alpha)))
    y = y0 + (distance*m.sin(m.radians(alpha)))
    print(x,y)
    return [x,y]

def kolmionala(b,c,alpha):
    #kaavasto s.18 
    sin = m.sin(m.radians(alpha))
    #print("sin:")
    #print(sin)
    return 0.5*b*c*sin

def pointToPoint(point1,point2):
    a = n.array(point1)
    b = n.array(point2)
    length = n.linalg.norm(a-b)
    print(length)
    return length

def kulmanPuolittaja(sivu1,sivu2,vastainen):
    osa1 = sivu1/(sivu1+sivu2)*vastainen
    osa2 = sivu2/(sivu1+sivu2)*vastainen
    print(osa1)
    print(osa2)
    return [osa1,osa2]

def intersect(line1,line2):
    x1 = line1[0][0]
    y1 = line1[0][1]
    x2 = line1[1][0]
    y2 = line1[1][1]
    x3 = line2[0][0]
    y3 = line2[0][1]
    x4 = line2[1][0]
    y4 = line2[1][1]

    px = ((x1*y2 - y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    py = ((x1*y2 - y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    print("px:")
    print(px)
    print("py:")
    print(py)
    return [px,py]

def centerOfCircleWithThreePoints(point1,point2,point3):
    x1 = point1[0]
    x2 = point2[0]
    x3 = point3[0]
    y1 = point1[1]
    y2 = point2[1]
    y3 = point3[1]
    print(x1,y1,x2,y2,x3,y3)

    h = [[(x1^2+y1^2), y1, 1], [(x2^2+y2^2), y2, 1], [(x3^2+y3^2), y3, 1]]/(2*[[x1,y1,1], [x2,y2,1], [x3,y3,1]])
    print(h)

def findCirclesIntersect(a,r,angle,alpha):
    x,y = a
    print(a)
    beta = angle+alpha
    print(beta)
    sx = x+r*m.cos(m.radians(beta))
    sy = y+r*m.sin(m.radians(beta))
    s = sx,sy
    print(s)
    return s

def ympyränKaari(alpha,radius):
    b = (alpha/360)*2*m.pi*radius
    return b
def sektorinPintaAla(alpha,radius):
    a = (alpha/360)*m.pi*m.pow(radius,2)
    return a

def pythagoras(kateetti1,kateetti2,hypotenuusa):
    if(kateetti1==0):
        return m.sqrt(m.pow(hypotenuusa,2)-m.pow(kateetti2,2))
    if(kateetti2==0):
        return m.sqrt(m.pow(hypotenuusa,2)-m.pow(kateetti1,2))
    if(hypotenuusa==0):
        return m.sqrt(m.pow(kateetti2,2)+m.pow(kateetti1,2))

def placeInSin(Amplitudi,kulmanopeus,hetki,kulma):
    return Amplitudi*m.sin(kulmanopeus*hetki+kulma)

def timeInSin(Amplitudi,y,kulmanopeus,kulma,n1):
    if(n1==0):
        return (-(m.asin((y/Amplitudi))+kulma-((2*n1+1)*n.pi)))/kulmanopeus
    else:
        return (-(m.asin((y/Amplitudi))+kulma-((2*n1)*n.pi)))/kulmanopeus

def equationOfLine(a,b):
    points = [(a[0],a[1]),(b[0],b[1])]
    x_coords, y_coords = zip(*points)
    A = n.vstack([x_coords,n.ones(len(x_coords))]).T
    m, c = n.linalg.lstsq(A, y_coords)[0]
    print("Line Solution is y = {m}x + {c}".format(m=round(m,3),c=round(c,3)))
    print("k=",round(m,3)," b=",round(c,3))
    kb = [m,c]
    return kb

