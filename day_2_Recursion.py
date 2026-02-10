# def tiling(n):
#   if n == 0 or n ==1 :
#     return 1
#   fnm1 = tiling(n-1)
#   fnm2 = tiling(n-2)
#   total = fnm1+fnm2
#   return total
# tiling (5)



# added removing duplicates from a string (a-z) using recursion:
# def remove_duplicates(s, index=0, seen=None, result=""):
#     if seen is None:
#         seen = [False] * 26

#     if index == len(s):
#         return result

#     pos = ord(s[index]) - ord('a')

#     if not seen[pos]:
#         seen[pos] = True
#         result += s[index]

#     return remove_duplicates(s, index + 1, seen, result)

# print(remove_duplicates("recursion")) 




