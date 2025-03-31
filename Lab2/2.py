import math
import random

class Point(object):
    def __init__(self,x : float,y : float):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ',' + str(self.y) + ")"

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not (self == other)

def distance(p1 : Point, p2 : Point):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

class Triangle(object):
    def __init__(self, p1 : Point , p2 : Point, p3 : Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        a = distance(self.p1, self.p2)
        b = distance(self.p2, self.p3)
        c = distance(self.p3, self.p1)
        p = (a + b + c) / 2
        self.area =math.sqrt(p*(p-a)*(p-b)*(p-c))

    def  __eq__(self,other):
        otherpoints = [other.p1, other.p2, other.p3]
        if self.p1 in otherpoints and self.p2 in otherpoints and self.p3 in otherpoints:
            return True
        return False

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return f"({str(self.p1)},{str(self.p2)},{str(self.p3)})"

    def is_in(self,other) -> bool: #проверка, является ли треугольник self вложенным в other
        selfpoints = [self.p1,self.p2,self.p3]


        for i in selfpoints:
            t1 = Triangle(i,other.p2,other.p3)
            t2 = Triangle(other.p1,i,other.p3)
            t3 = Triangle(other.p1,other.p2,i)
            if not(other.area == t1.area + t2.area + t3.area):
                return False
        return True

    # def get_area(self):
    #     a = distance(self.p1,self.p2)
    #     b = distance(self.p2,self.p3)
    #     c = distance(self.p3,self.p1)
    #     p = (a+b+c)/2
    #     return math.sqrt(p*(p-a)*(p-b)*(p-c))


def is_on_line(p1: Point,p2 : Point, p3: Point):
    return p3.x * (p2.y - p1.y) - p3.y * (p2.x - p1.x) == p1.x * p2.y - p2.x * p1.y

def console_input()-> list[Point]:
    points = list()
    n = int(input("Введите количество точек: "))
    print("Введите координаты точек: ")
    for i in range(n):
        tmp = Point(float(input()), float(input()))
        if not (tmp in points):
            points.append(tmp)
    return points

def rand_input()->list[Point]:
    points = list()
    n = int(input("Введите количество точек: "))
    for i in range(n):
        tmp = Point(random.randint(-1000, 1000) / 10, random.randint(-1000, 1000) / 10)
        if not (tmp in points):
            points.append(tmp)
    return points

def proggres(a):
    print(f"\rproggress:{a}%",end ="")
    if a == 100:
        print(f"\r",'',sep = '',end = "")

def main():
    #points = console_input()
    points = rand_input()

    triangles = list()

    for p1_ind in range(len(points)-2):
        for p2_ind in range(p1_ind + 1,len(points)-1):
            for p3_ind in range(p2_ind + 1,len(points)):
                triangles.append( Triangle(points[p1_ind],points[p2_ind],points[p3_ind]) )

    #for proggres
    lastprog = -2

    for i in range(len(triangles)-1):
        for j in range(i+1,len(triangles)):
            if triangles[i].area< triangles[j].area:
                triangles[i],triangles[j] = triangles[j],triangles[i]

            # for proggres
            tmp = int((i/(len(triangles)-2))*100)
            if tmp != lastprog:
                proggres(tmp)
                lastprog = tmp

    flag = True
    for i in range(len(triangles)-1):
        for j in range(i+1,len(triangles)):
            if triangles[j].is_in(triangles[i]):
                print(f"Да, есть вложенные треугольники, пример: {triangles[j]} вложен в {triangles[i]}")
                flag = False
                break
        if not flag:
            break
    if flag:
        print("Не существует таких точек, чтобы треугольники составленные из их координат оказались вложенными")

if __name__ == "__main__":
    main()
