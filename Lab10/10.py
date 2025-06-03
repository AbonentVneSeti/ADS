class Building:
    def __init__(self, critical_floor):
        self.critical_floor = critical_floor

    def drop_egg(self, floor):
        return floor >= self.critical_floor


def find_critical_floor(building):
    low = 0
    step = 14
    current_floor = step
    eggs = 2
    throws = 0

    while eggs > 1 and current_floor <= 100:
        throws += 1
        if building.drop_egg(current_floor):
            eggs -= 1
        else:
            low = current_floor
            step -= 1
            current_floor += step
            if current_floor > 100:
                current_floor = 100

    if eggs == 1:
        for floor in range(low + 1, current_floor):
            throws += 1
            if building.drop_egg(floor):
                return floor, throws
        return current_floor, throws
    else:
        return None, throws


if __name__ == "__main__":
    for i in range(1,101):
        critical_floor, throws = find_critical_floor(Building(i))
        print(f"Результат(критический этаж = {i}): критический этаж = {critical_floor}, бросков = {throws}")