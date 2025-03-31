import math
from logging import exception

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

    def __iadd__(self, other):
        ...

def is_on_line(points):
    p1 = points[0]
    p2 = points[1]

    for p in points[2:]:
        if (p.y - p1.y) * (p2.x - p1.x) != (p.x - p1.x) * (p2.y - p1.y):
            return False
    return True

# Полярный угол вектора по двум точкам [0;2π]
def polar_angle(a: Point, b : Point):
    x = b.x - a.x
    y = b.y - a.y
    if x==0 and y == 0:
        exception("[polar_angle]: same points")

    res = math.atan2(y, x)
    if (res < 0):
        res += 2 * math.pi
    return res

def main():
    # Ввод точек
    inputpoints = list()
    n = int(input("Введите количество точек: "))
    print("Введите координаты точек: ")
    for i in range(n):
        inputpoints.append(Point(float(input()),float(input())))

    # Форматирование ввода
    points = list()
    minpoint = inputpoints[0]
    for i in inputpoints:
        if i.y < minpoint.y:
            minpoint = i
        if not( i in points):
            points.append(i)

    # Проверка на существование оболочки
    if len(points) < 3:
        print("Оболочку невозможно построить: слишком мало точек")
    elif is_on_line(points):
        print("Оболочку невозможно построить: все точки лежат на одной прямой")
    else:
        # Алгоритм Джарвиса
        MCH = list()
        MCH.append(minpoint)

        while True:
            minangle = 99
            minpoint = MCH[-1]
            for p in points:
                if MCH[-1] == p:
                    pass
                elif polar_angle(MCH[-1],p) < minangle:
                    minangle = polar_angle(MCH[-1],p)
                    minpoint = p

            if minpoint == MCH[0]:
                break

            MCH.append(minpoint)
            points.remove(minpoint)

        print("Исходные точки:")
        for i in inputpoints: print(i)
        print("Оболочка:")
        for i in MCH: print(i)

if __name__ == "__main__":
    main()