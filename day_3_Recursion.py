# binary string problem using recursion (print all binary string of size n with out consigitive ones)

def bitstr(n,lastplace=0,string=""):
    if n == 0:
        print(string)
        return 
    bitstr(n-1,0,string+"0")
    if (lastplace == 0):
        bitstr(n-1,1,string+"1")
        
 bitstr(3)


For a given integer array of size N.Youhavetofindalltheoccurrences(indices)ofagivenelement(Key)andprintthem.Usearecursivefunctiontosolvethisproblem.Sample Input: arr[ ] = {3, 2, 4, 5, 6, 2, 7, 2, 2},key = 2Sample Output: 1 5 7 8
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
    
