def diag_2_sym(s):
    s = s.split()
    output_str = []
    for index in range(0,len(s[1])):
        output_str.append("")
        for line in s:
            output_str[index] = output_str[index] + line[index]
        output_str[index] = output_str[index][::-1]
    return "\n".join(output_str[::-1])

def rot_90_counter(s):
    output_str = diag_2_sym(s).split()
    for index in range(0,len(output_str)):
        output_str[index] = output_str[index][::-1]
    return "\n".join(output_str)

def selfie_diag2_counterclock(s):
    r90s = rot_90_counter(s).split()
    d2syms = diag_2_sym(s).split()
    s = s.split()
    newstr = []
    for index in range(0,len(s)):
        newstr.append(f"{s[index]}|{d2syms[index]}|{r90s[index]}")
    return "\n".join(newstr)

def oper(fct, s):
    return fct(s)
