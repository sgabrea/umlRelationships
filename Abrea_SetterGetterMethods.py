class BankAccount:
     def __init__ (self, account_number, balance):
         self.__account_number = account_number
         self.__balance = balance
         
     def set_account_number(self, account_number):
         self.__account_number = account_number
         
     def set_balance(self, balance):
         if balance < 0:
             print("Balance must not be a negative number.")
         else:
             self.__balance = float(balance)
             
     @property
     def account_number(self):
         return self.__account_number
         
     @property
     def balance(self):
         return self.__balance
         
         
