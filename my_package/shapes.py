def circle(radius):
    return 22/7 * radius**2

    # circumference = 2 * math.pi * radius
    # return circumference

def triangle(a,b,c):
    s = (a+b+c)/2
    area = s * (s-a)*(s-b)*(s-c)
    return area**0.5
