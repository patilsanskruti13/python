with open("practice.txt","w") as f:
    f.write("HII EVERYONE \n we are learning file I/O")
    f.write("using java. \n i like programming in java")
    
with open("practice.txt","r") as f:  
    data=f.read()
new_data=data.replace("java","python") 
print(new_data) 

with open("practice.txt","w") as f:  
    data=f.write(new_data)
def check_for_word():
    word="learning"    
    with open("practice.txt","r") as f:  
        data=f.read()
        if(data.find(word)!=-1)    :
            print("found")
        else:

