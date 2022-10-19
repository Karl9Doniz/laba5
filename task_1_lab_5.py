import math
# 1 task
def distance_between_paralell(k1,c1,k2,c2):
    return round(abs((c2-c1)*math.sqrt(1/(1+k1**2))),2)

def lines_intersection(k1, c1, k2, c2):
    """
    Input- equation of two lines
    Ouput- intersection point
    lines_intersection(1, 1, 2, 2)
    >>> -1,0
    """
    if k1==k2:
        return None
    x=round((c2-c1)/(k1-k2) , 2)
    y=round(k1*(c2-c1)/(k1-k2)+c1 , 2)
    return x,y

def distance(x1, y1, x2, y2):
    """
    Input- 2 coordinates of points
    Output- distance between points
    distance(3,4,6,8)
    >>> 5.0
    """
    k=(x2-x1)**2+(y2-y1)**2
    if k>0:
        return round(math.sqrt(k),2)
    return None
def area_of_trapecia(k1,c1,k2,c2,k3,c3,k4,c4):
    """
    outputs area of trapecia
    input - k1 should == k3 ( in such order that 1&3 are paralel)

    """
    koefficients=[k1,k2,k3,k4]
    c_of_lines=[c1,c2,c3,c4]
    dots=[]
    for i in range(4):
        dots.append(lines_intersection(koefficients[i], c_of_lines[i], koefficients[(i+1)%4], c_of_lines[(i+1)%4]))
    side_1=distance(dots[1][0],dots[1][1],dots[2][0],dots[2][1])
    side_2=distance(dots[3][0],dots[3][1],dots[0][0],dots[0][1])
    side_average=(side_1+side_2)/2
    return(side_average*distance_between_paralell(k1, c1, k3, c3) )
print(area_of_trapecia(2, 1, -1, 5, 2, -3, -5, 3))
#2 task
def tangential_check(sides):
    """
    check if quadliteral is tangential
    """
    if sides[1]+sides[3]==sides[2]+sides[0]:
        return True
    return False
def cos_theorem(side_1,side_2,side_3):
    """
    calculates area of triangle
    """
    return ((side_1**2+side_2**2-side_3**2)/(2*side_1*side_2))
def cyclic_check(sides,diagonal):
    """
    check if quadliteral is cyclic
    """
    if cos_theorem(sides[0], sides[1], diagonal)+ cos_theorem(sides[2], sides[3], diagonal)==0:
        return True
    return False

def area_search(k1,c1,k2,c2,k3,c3,k4,c4):
    s=0
    koefficients=[k1,k2,k3,k4]
    c_of_lines=[c1,c2,c3,c4]
    dots=[]
    sides=[]
    for i in range(4):
        dots.append(lines_intersection(koefficients[i], c_of_lines[i], koefficients[(i+1)%4], c_of_lines[(i+1)%4]))
    for i in range(4):
        sides.append(distance(dots[i][0], dots[i][1], dots[(i+1)%4][0], dots[(i+1)%4][1]))
    diagonal_02=distance(dots[0][0], dots[0][1], dots[2][0], dots[2][1])
    if not(convex_check(dots)):
        if (cyclic_check(sides,diagonal_02)):
            if (tangential_check(sides)):

                return math.sqrt(sides[0]*sides[1]*sides[2]*sides[3])
            for i in range(4):
                p=p+sides[i]
            p=p/2
            s=math.sqrt((p-sides[0])*(p-sides[1])*(p-sides[2])*(p-sides[3]))
            return s
    else:
        special_point=convex_return(dots)
        if special_point==0:
            return( triangle_area([ dots[0] ,dots[1],dots[2]])+triangle_area([dots[0],dots[2],dots[3]]))
        if special_point==1:
            return( triangle_area([dots[3],dots[1],dots[2]])+triangle_area([dots[1],dots[0],dots[3]]))
        if special_point==2:
            return( triangle_area([dots[0],dots[1],dots[2]])+triangle_area([dots[0],dots[2],dots[3]]))
        if special_point==3:
            return( triangle_area([dots[3],dots[1],dots[2]])+triangle_area([dots[1],dots[0],dots[3]]))

#print(cyclic_check([3,4,3,4], 5))
def convex_check(dots):
    """
    check if convex
    """
    k1,c1=diagonal_equation(dots[0], dots[2])
    k2,c2=diagonal_equation(dots[1], dots[3])
    if dots[1][0]*k1+c1<dots[1][1]:
        if dots[3][0]*k1+c1<dots[3][1]:
            return True
    if dots[1][0]*k1+c1>dots[1][1]:
        if dots[3][0]*k1+c1>dots[3][1]:
            return True


    if dots[0][0]*k2+c2<dots[0][1]:
        if dots[2][0]*k2+c2<dots[2][1]:
            return True
    if dots[0][0]*k2+c2>dots[0][1]:
        if dots[2][0]*k2+c2>dots[2][1]:
            return True
    return False
def convex_return(dots):
    """
    find conveex point
    """
    k1,c1=diagonal_equation(dots[0], dots[2])
    k2,c2=diagonal_equation(dots[1], dots[3])
    if dots[1][0]*k1+c1<dots[1][1]:
        if dots[3][0]*k1+c1<dots[3][1]:
            if abs(dots[3][0]*k1+c1-dots[3][1])>abs(dots[1][0]*k1+c1-dots[1][1]):
                return 1
            else:
                return 3
    if dots[1][0]*k1+c1>dots[1][1]:
        if dots[3][0]*k1+c1>dots[3][1]:
            if abs(dots[3][0]*k1+c1-dots[3][1])>abs(dots[1][0]*k1+c1-dots[1][1]):
                return 1
            else:
                return 3


    if dots[0][0]*k2+c2<dots[0][1]:
        if dots[2][0]*k2+c2<dots[2][1]:
            if abs(dots[2][0]*k1+c1-dots[2][1])>abs(dots[0][0]*k1+c1-dots[0][1]):
                return 0
            else:
                return 2
    if dots[0][0]*k2+c2>dots[0][1]:
        if dots[2][0]*k2+c2>dots[2][1]:
            if abs(dots[2][0]*k2+c2-dots[2][1])>abs(dots[0][0]*k2+c2-dots[0][1]):
                return 0
            else:
                return 2
    return False
def triangle_area(dots):
    """ 
    find area of triangle
    """
    a_1=distance(dots[0][0],dots[0][1],dots[1][0],dots[1][1])
    b_1=distance(dots[2][0],dots[2][1],dots[1][0],dots[1][1])
    c_1=distance(dots[0][0],dots[0][1],dots[2][0],dots[2][1])
    p=a_1+b_1+c_1
    p=p/2
    return math.sqrt(p*(p-a_1)*(p-b_1)*(p-c_1))


    
def diagonal_equation(point1,point2):
    """
    calculate koefficients for diagonal
    """
    k=(point2[1]-point1[1])/(point2[0]-point1[0])
    c=point1[1]-k*point1[0]
    return (k,c)
#print(convex_return([[0,0],[1,1],[0.5,0.5],[1.1,0]]))
#print(area_search(1, 0, 1.5, -1, -1.7, 2, 0, 0))
