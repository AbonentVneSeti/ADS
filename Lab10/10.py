import math


def optimal_step(total_floors):
    return math.ceil((math.sqrt(8 * total_floors + 1) - 1) / 2)


def egg_broken(floor, critical_floor):
    return floor >= critical_floor


def find_critical_floor(total_floors=100, critical_floor = 100):
    import random

    step = optimal_step(total_floors)
    current_floor = step
    eggs_left = 2
    throws = 0

    while eggs_left > 0 and current_floor <= total_floors:
        throws += 1
        if egg_broken(current_floor, critical_floor):
            eggs_left -= 1
            lower_floor = current_floor - step + 1 if step > 1 else 1
            for floor in range(lower_floor, current_floor):
                throws += 1
                if egg_broken(floor, critical_floor):
                    return floor, throws
            return current_floor, throws
        else:
            step -= 1
            current_floor += step

    if current_floor > total_floors:
        throws += 1
        if egg_broken(total_floors, critical_floor):
            eggs_left -= 1
            lower_floor = total_floors - step + 1
            for floor in range(lower_floor, total_floors):
                throws += 1
                if egg_broken(floor, critical_floor):
                    return floor, throws
            return total_floors, throws
        else:
            return -1, throws


critical_floor, throws = find_critical_floor(100,5)
print(f"Результат: критический этаж = {critical_floor}, бросков = {throws}")
