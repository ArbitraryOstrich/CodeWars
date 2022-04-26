def insurance(age, size, num_of_days):
    if num_of_days > 0:
        cost = num_of_days*50
        if age < 25:
            cost = cost + (num_of_days*10)
        if size == 'medium':
            cost = cost + (num_of_days*10)
        else:
            if not size == 'economy':
                cost = cost + (num_of_days*15)
        return cost
    else:
        return 0
