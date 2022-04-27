def bit_march(n: int) -> list:
    start = []
    end = []
    for i in range(0, 8):
        n += -1
        if n > -1:
            start.insert(0, 1)
        else:
            start.insert(0, 0)
    while start[0] != 1:
        end.append(list(start))
        start.pop(0)
        start.append(0)
    end.append(list(start))
    return end


print(bit_march(3))
