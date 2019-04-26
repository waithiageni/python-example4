class MpesaAccount:
        def __init__(self,Name,Phone_no):
                self.Name = Name
                self.Phone_no = Phone_no
                self.Balance = 0
                self.deposits = []
                self.withdrawals = []
                self.loan = 0


        def deposit(self,d):
                deposit=d
                self.Balance=self.Balance+d
                self.deposits.append(d)
                print ("Dear {} you deposit of Ksh {} was successful ,current balance is {}".format(self.Name,d,self.Balance))  
        

        def withdraw(self,p):
        
                if p<self.Balance:
                    self.Balance=self.Balance-p
                    self.withdrawals.append(p)
                    sms1= "Dear {} your withdrawal of {} was successful, current balance is {}".format(self.Name,p,self.Balance)
                    print (sms1)
                else:
                    print ("you have insufficient balance")


        def check_balance(self):
                check_balance=self.Balance
                return "Your Balance is {}".format(self.Balance)


        def my_deposits(self):
                for d in self.deposits:
                    print(d)

                
        def my_withdrawals(self):
            for w in self.withdrawals:
                print(w)
                
        
        def give_loan(self,l):
                
                if len(self.deposits)>=5 and l<1/3*sum(self.deposits) and self.loan==0:
                    self.loan = self.loan + l
                    print("Dear {} your loan of {} has been approved".format(self.Name,l))
                    
                else:
                    print("loan not succesful")     


        def loan_payment(self,p):
                payment=p
                if p<self.loan:
                    self.loan=self.loan-p
                    sms3="Dear {} you loan balance is {}".format(self.Name,self.loan)
                    print(sms3)
                elif p>self.loan:
                    over_payment=p-self.loan
                    self.loan=p-over_payment-self.loan  
                    self.Balance=over_payment-self.Balance
                    sms4="Dear {} you loan is fully paid the excess amount has been deposited to you account".format(self.Name)
                    print(sms4)



                else:
                    self.loan==0
                    sms5="Dear {} you loan of {}  is fully settled ".format(self.Name,self.loan)
                    print(sms5)     