def rot(s):
    # strings = s.split("\n")
    # strings = strings[::-1]
    # for index in range(0,len(strings)):
    #     strings[index] = strings[index][::-1]
    # return "\n".join(strings)
    return s[::-1]


def selfie_and_rot(s):
    strings = s.split("\n")
    inv_strings = strings[::-1]
    dots = "." * len(strings[1])
    for index in range(0, len(inv_strings)):
        inv_strings[index] = inv_strings[index][::-1]
    strings1 = f"{dots}\n".join(strings)
    strings2 = f"\n{dots}".join(inv_strings)
    return f"{strings1}{dots}\n{dots}{strings2}"


def oper(operation, string):
    return operation(string)


s = "PnVf\nNpcJ\nSbsj\nVBZx"
oper(rot, s)

s1 = "uLcq....\nJkuL....\nYirX....\nnwMB....\n....BMwn\n....XriY\n....LukJ\n....qcLu"
s2 = "xZBV....\njsbS....\nJcpN....\nfVnP....\n....PnVf\n....NpcJ\n....Sbsj\n....VBZx"


if oper(selfie_and_rot, "uLcq\nJkuL\nYirX\nnwMB") == s1:
    print(True)

if oper(selfie_and_rot, "xZBV\njsbS\nJcpN\nfVnP") == s2:
    print(True)
