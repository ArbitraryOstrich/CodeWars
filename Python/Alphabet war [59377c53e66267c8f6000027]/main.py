
### Clever to do it with one dict, and negative values on one side
### Sum the powers, neg result means neg side wins ect.
left_side = {"w" : 4, "p" : 3, "b" : 2, "s" : 1}
right_side = {"m" : 4,"q" : 3,"d" : 2,"z" : 1}


def alphabet_war(fight):
    lPoints = 0
    rPoints = 0
    for letter in fight:
        if letter in left_side:
            lPoints += left_side[letter]
        if letter in right_side:
            rPoints += right_side[letter]
    if lPoints > rPoints:
        return "Left side wins!"
    if rPoints > lPoints:
        return "Right side wins!"
    return "Let's fight again!"
