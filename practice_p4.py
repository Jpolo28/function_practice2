def max_num(x, y, z):
    max_num = max(x, y, z)
    return(max_num)
print(max_num(1, 4, 3))

import math
lst = [1, 2, 3, 4, 5]
def multi_list(*lst):
    result1 = math.prod(*lst)
    return result1
print(multi_list(lst))

def rev_string(s):
    s1 = ''.join(reversed(s))
    return s1
print(rev_string("apple"))

def num_within(n):
    if n in range(1,10):
        return("True")
    else:
        return("False")
print(num_within(5))

class Solution:
   def pascal(self, n):
      if n==0:
         return [1]
      if n==1:
         return [1,1]
      ls=[1,1]
      temp=[1,1]
      for i in range(2,n+1):
         ls=temp
         temp=[1]
         for i in range(len(ls)-1):
            temp.append(ls[i]+ls[i+1])
         temp.append(1)
      return temp
ob = Solution()
print(ob.pascal(5))
 
