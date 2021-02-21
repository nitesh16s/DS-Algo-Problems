def search(haystack, needle):
    if not len(haystack) or not len(needle):
        return None
    ans = []
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i] == needle[0]:
            # print(haystack[i+1: i+len(needle)], needle[1:len(needle)+1])
            if haystack[i+1: i+len(needle)] == needle[1:len(needle)+1]:
                ans.append(i)
    return ans


# def search1(haystack, needle):
#     if not len(haystack) or not len(needle):
#         return None
#     ans = []
#     for i in range(len(haystack)):
#         if haystack[i] == needle[0]:
#             for j in range(1, len(needle)):
#                 if j == len(needle)-1:
#                     ans.append(i)
#                 if haystack[i+j] != needle[j]:
#                     break
#     return ans


print(search(haystack='ahabcksdfabceadwweabc', needle='abc'))
print(search(haystack='', needle='abc'))
print(search(haystack='ahabcksdfabceadwweabc', needle=''))
print(search(haystack='abcabcabcabc', needle='abc'))
