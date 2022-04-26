def drop_bombs(bf,strike):
    bf = list(bf)
    strike = list(strike)
    for strike_index in range(0,len(strike)):
        if strike[strike_index] == '*':
            bf[strike_index] = "_"    
            if strike_index > 1:
                bf[strike_index-1] = "_"
            if strike_index+1 < len(bf):
                bf[strike_index+1] = "_"
    return "".join(bf)

def bring_reinforcements(bf,rf):
    bf = list(bf)
    # iter over BF looking for _
    for bf_index in range(0,len(bf)):
        if bf[bf_index] == '_':
            
            ## look for reinforcements
            for rf_index in range(0,len(rf)):
                temp = list(rf[rf_index])
                ## If current place is a _ hop to next loop
                if rf[rf_index][bf_index] == '_':
                    continue
                ## If we get here we can reinforce and break our loop
                bf[bf_index] = rf[rf_index][bf_index]
                temp[bf_index] = "_"
                rf[rf_index] = "".join(temp)
                
                break
    return "".join(bf),rf


def alphabet_war(re_array,strike_array):
    bf = re_array[0]
    re_array = re_array[1:]
    for index in range(0,len(strike_array)):
        print(f"strike {index}")
        bf = drop_bombs(bf,strike_array[index])
        print(bf)
        try:
            print(f"reinforcments {index}")
            bf,re_array = bring_reinforcements(bf, re_array)
            print(f"re_array: {re_array}")
            print(f"{bf}")
        except:
            pass
    return bf


reinforces = ["g964xxxxxxxx",
            "myjinxin2015",
            "steffenvogel",
            "smile67xxxxx",
            "giacomosorbi",
            "freywarxxxxx",
            "bkaesxxxxxxx",
            "vadimbxxxxxx",
            "zozofouchtra",
            "colbydauphxx" ];

airstrikes = ["* *** ** ***",
            " ** * * * **",
            " * *** * ***",
            " **  * * ** ",
            "* ** *   ***",
            "***   ",
            "**",
            "*",
            "*" ]

alphabet_war(reinforces,airstrikes)


alphabet_war(["ab___fg","hijklmn"], ["   *   ", "*  *   "])#'hi___fg');               
alphabet_war(["aaaaa","bbbbb", "ccccc", "ddddd"],  ["*", " *", "   "]) #'ccbaa');