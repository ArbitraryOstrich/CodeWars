def bit_march(n: int) -> list:
    start = []
    end = []
    ##Could use zfill here
    ### But then i need to split it into a list.
    for i in range(0, 8):
        n += -1
        if n > -1:
            start.insert(0, 1)
        else:
            start.insert(0, 0)
    while start[0] != 1:
        ## This was strange something to do with it adding the variable as opposed to the value of the variable to the end list
        ## This resulted in end being filled with multiples of only a single state of start
        end.append(list(start))
        start.pop(0)
        start.append(0)
    end.append(list(start))
    return end


print(bit_march(3))
