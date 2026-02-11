# binary string problem using recursion (print all binary string of size n with out consigitive ones)

def bitstr(n,lastplace=0,string=""):
    if n == 0:
        print(string)
        return 
    bitstr(n-1,0,string+"0")
    if (lastplace == 0):
        bitstr(n-1,1,string+"1")
        
 bitstr(3)


# For a given integer array of size N.Youhavetofindalltheoccurrences(indices)ofagivenelement(Key)andprintthem.Usearecursivefunctiontosolvethisproblem.Sample Input: arr[ ] = {3, 2, 4, 5, 6, 2, 7, 2, 2},key = 2Sample Output: 1 5 7 8
def findkey(arr,key,res,idx=0):
  n = len(arr)
  if idx == n:
    return arr
  if arr[idx] == key:
    res.append(idx)
  findkey(arr,key,res,idx+1)
  return res
  
arr =[3, 2, 4, 5, 6, 2, 7, 2, 2]
res= []
print(findkey(arr,2,res))

# You are given a number (eg -  2019), convert it into a String of english like“two zero one nine”.  Use a recursive function to solve this problem.NOTE-Thedigitsofthenumberwillonlybeintherange0-9andthelastdigitofanumbercan’t be 0

def convert(n):
  words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  if n < 10:
    return words[n]
  return convert(n//10)+" "+words[n%10]
print(convert(2019))
  
  
  


# Write a program to findLength of aStringusing Recursion

def length(s="",c=0):
  if s == "":
    return c
  return length(s[1:], c + 1)
print(length("abcd",0))
