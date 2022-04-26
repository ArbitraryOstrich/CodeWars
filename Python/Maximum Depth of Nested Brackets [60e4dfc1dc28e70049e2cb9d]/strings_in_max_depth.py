def strings_in_max_depth(s):
    ## Cases (), (()())
    ## Track the locations and depth of each bracket set
    ##{depth:[[open_index,close_index],[open_index,close_index]]}
    if s.count("(") == 0:
        return [s]
    depth = 0
    brackets = []
    for index in range(0,len(s)):
        if s[index] == "(":
            depth += 1
            if depth > len(brackets):
                brackets.append([])
            brackets[depth-1].append([index])
            continue
        if s[index] == ")":
            brackets[depth-1][-1].append(index)
            depth -= 1
            continue
    final_list = []
    for pair in brackets[-1]:
        final_list.append(s[pair[0]+1:pair[1]])

    return final_list

s = "(f(d(asds))s)(a)"
strings_in_max_depth(s)
