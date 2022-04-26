def delete_nth(order,max_e):
    new_order = []
    for element in order:
        if new_order.count(element) < max_e:
            new_order.append(element)
        else:
            continue
    return new_order


delete_nth([20,37,20,21], 1)
delete_nth([1,1,3,3,7,2,2,2,2], 1)
delete_nth([1,1,3,3,7,2,2,2,2], 2)
delete_nth([1,1,3,3,7,2,2,2,2], 3)
