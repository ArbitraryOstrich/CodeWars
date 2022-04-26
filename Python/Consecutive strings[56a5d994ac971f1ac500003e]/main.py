def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""
    a = ["" for i in range(0,k)]
    len_buffer = 0
    for index in range(0,len(strarr)):
        a.pop(0)
        a.append(strarr[index])
        if len("".join(a)) > len_buffer:
            len_buffer = len("".join(a))
            longest_a = "".join(a)
    return longest_a




s = ["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"]
s = ["zone", "abigail", "theta", "form", "libe", "zas"]
longest_consec(s, 2)



# wrote all this code and its based on a misunderstanding of the request
#
# def longest_of_list(str_arry):
#     largest = [0,""]
#     for a in str_arry:
#         if len(a) > largest[0]:
#             largest = [len(a),a]
#     return largest[1]
#
# def longest_two(str_list):
#     str_len = []
#     for a in str_list:
#         str_len.append(len(a))
#     largest = [0,0,0]
#     for index_x in range(0,len(str_list)):
#         for index_y in range(0,len(str_list)):
#             if index_y == index_x:
#                 continue
#             if str_len[index_x] + str_len[index_y] > largest[0]:
#                 largest = [str_len[index_x] + str_len[index_y],index_x,index_y]
#     return  [str_list[largest[1]], str_list[largest[2]]]
#
# def longest_consec(strarr, k):
#     if len(strarr) == 0 or k > len(strarr) or k <= 0:
#         return ""
#     if k == 1:
#         longest_of_list(strarr)
#     temp_strarr = strarr[:]
#     str_buffer = longest_two(temp_strarr)
#     temp_strarr.remove(str_buffer[0])
#     temp_strarr.remove(str_buffer[1])
#     temp_strarr.append("".join(str_buffer))
#     if k > 2:
#         for index in range(0,k):
#             str_buffer = longest_two(temp_strarr)
#     return "".join(str_buffer)
#
#
#
