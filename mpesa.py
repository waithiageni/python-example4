class MpesaAccount:
		def __init__(self,Name,Phone_no,Balance):
				self.Name=Name
				self.Phone_no=Phone_no
				self.Balance=Balance
		def check_balance(self):
				check_balance=self.Balance
				return "Your Balance is {}".format(self.Balance)

		def withdraw(self,p):
				withdraw=p
				p<self.Balance
				self.Balance=self.Balance-p
				return "Dear {} your withdrawal of {} was successful, current balance is {}".format(self.Name,p,self.Balance)
		def deposit(self,d):
				deposit=d
				self.Balance=self.Balance+d
				return "Dear {} you deposit of Ksh {} was successful ,current balance is {}".format(self.Name,d,self.Balance)		