import numpy as num
import random 
masiv = num.zeros((3,3),dtype = num.int)
 
def multiply ( myarr ):
    res = myarr[0][0]*myarr[0][-1]*myarr[-1][0]*myarr[-1][-1]
    return (res)

for i in range(3):     
    for j in range (3):
                 
        masiv[i][j] = random.randint(0, 30)
        
multi_masiv = masiv * 2
sum_masiv = masiv + multi_masiv

print(masiv)        
print(multi_masiv)
print(sum_masiv)
print(multiply(multi_masiv))
