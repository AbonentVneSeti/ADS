import math
import random

#Точка пересечения двух прямых

#Точка пересечения прямой и отрезка

#Точка пересечения двух отрезков

#Точка пересечения прямой и окружности

#Точка пересечения отрезка и окружности

#Точка пересечения двух окружностей

class Point(object):
    def __init__(self,x : float,y : float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

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
        return f"Triangle({str(self.p1)},{str(self.p2)},{str(self.p3)}):{self.area:.2f}"

    def __repr__(self):
        return str(self)

    def is_in(self,other) -> bool: #проверка, является ли треугольник self вложенным в other
        selfpoints = [self.p1,self.p2,self.p3]

        for i in selfpoints:
            t1 = Triangle(i,other.p2,other.p3)
            t2 = Triangle(other.p1,i,other.p3)
            t3 = Triangle(other.p1,other.p2,i)
            if not(other.area == t1.area + t2.area + t3.area):
                return False
            #elif t1.area == 0 or t2.area == 0 or t3.area == 0:
            #    return False
        return True

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

def check_occur(points):
    triangles = list()

    for p1_ind in range(len(points) - 2):
        for p2_ind in range(p1_ind + 1, len(points) - 1):
            for p3_ind in range(p2_ind + 1, len(points)):
                t1 = Triangle(points[p1_ind],points[p2_ind],points[p3_ind])
                n = 0
                while n< len(triangles):
                    if t1.area > triangles[n].area:
                        break
                    n+=1
                triangles.insert(n,t1)

                for i in range(len(triangles)-1,n,-1):
                    if triangles[i].is_in(t1):
                        print(f"Да, есть вложенные треугольники, пример: {triangles[i]} вложен в {t1}")
                        return True
                for i in range(0,n):
                    if t1.is_in(triangles[i]):
                        print(f"Да, есть вложенные треугольники, пример: {t1} вложен в {triangles[i]}")
                        return True
    print("Не существует таких точек, чтобы треугольники составленные из их координат оказались вложенными")
    return False

def main():
    points = rand_input()
    check_occur(points)

if __name__ == "__main__":
    main()