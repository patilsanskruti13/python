class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass            #(__) jar aapn attribute chya aadhi don __ underscoore  lavle ta te private hota 
        
    def reset_pass(self):
        print(self.__acc_pass)  
acc1=Account(12345,"abc")
print(acc1.acc_no)
#print(acc1.__acc_pass)    #THIS WI THROW AN ERROR , AS PASSWORD IS PRIVATE
print(acc1.reset_pass())