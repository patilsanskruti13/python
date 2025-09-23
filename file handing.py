# openinf file and readng the data
"""f=open("sampe.txt","r")
data=f.read()
# line1=f.readline
print(data)
f.close()

#writing to a file
f=open("sampe.txt","w")
f.write("hii i'm ROHAN")
f.close()

f=open("sampe.txt","a")
f.write("hii i'm ROHAN")
f.close()"""

#combining reading and writing mode

"""f=open("sampe.txt","r+")
f.write("hello how are you ")
f.close()"""

"""f=open("sampe.txt","w+")
f.write("hello how are you ")
f.close()"""
#append
"""'f=open("sampe.txt","a+")
f.write("hello how are you dear? ")
f.close()
"""

#with syntax
with open("sampe.txt","r") as f:            #automatically close file
    data=f.read()
    print(data)
    
#deleting file

import os
os.remove("sampe.txt")