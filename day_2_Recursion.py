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
# Friend of n pairs or single find ways they can be in party
# def friend(n):
#     if n == 1 or n == 2:
#         return n 
#     single = friend(n-1)
#     pair = friend(n-2)
#     pairs = (n-1)*pair
#     total = single+pairs
#     return total 
    
# print(friend(3))





