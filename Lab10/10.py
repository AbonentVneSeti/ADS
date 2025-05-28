def min_egg_throws(floors):
    m = 0
    while m * (m + 1) // 2 < floors:
        m += 1
    return m

result = min_egg_throws(100)
print(result)