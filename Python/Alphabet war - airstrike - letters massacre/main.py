dict = {"w" : 4, "p" : 3, "b" : 2, "s" : 1, "m" : -4,"q" : -3,"d" : -2, "z" : -1, "_" :0}
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def pop_bombs(str):
    str = list(str)
    for index in range(0,len(str)):
        if str[index] == '*':
            str[index] = '_'
            try:
                if str[index-1] in alphabet:
                    str[index-1] = '_'
            except:
                pass
            try:
                if str[index + 1] in alphabet:
                    str[index + 1] = '_'
            except:
                pass
    return "".join(str)

def alphabet_war(fight):
    fight = pop_bombs(fight)
    sum = 0
    for letter in fight:
        if letter in dict:
            sum += dict[letter]
    if sum > 0:
        return "Left side wins!"
    if sum < 0:
        return "Right side wins!"
    return "Let's fight again!"
