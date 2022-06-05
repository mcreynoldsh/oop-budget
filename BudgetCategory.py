from Transaction import Transaction
import csv
class BudgetCategory:
    
    def __init__(self,name):
        self.name = name
        self.amount_spent=0
        self.budgeted_amount=0
        self.transactions = self.fill_transactions()

    def __str__(self):
        if len(self.transactions) > 0:
            ret_str= f"""
            {self.name} Expenses
            -----------------"""
            for x in self.transactions:
                ret_str += str(x)
            ret_str += f"""\n\nYou've spent ${self.amount_spent} of your ${self.budgeted_amount} that you budgeted towards {self.name} expenses this month\n"""
            return ret_str
        else:
            return  f"""
            {self.name} Expenses
            -----------------
            No current expenses"""   

    def add_budget(self, budget_num):
        self.budgeted_amount = budget_num

    def fill_transactions(self):
        transactions=[]
        money_spent=0
        with open(f"/Users/huntermcreynolds/code/exercises/Week2/oop-budget/data/{self.name}_expenses.csv") as f :     
            student_reader = csv.DictReader(f,skipinitialspace=True)
            for row in student_reader:
                transactions.append(Transaction(**dict(row)))
                money_spent+= int(row['trans_amount'])
            self.amount_spent=money_spent    
            return transactions 
    
    def new_transaction(self,name,amount):
        with open(f"/Users/huntermcreynolds/code/exercises/Week2/oop-budget/data/{self.name}_expenses.csv", mode='a') as csv_file:
            fieldnames = ['trans_name','trans_amount']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'trans_name': name, 'trans_amount': amount})
        self.transactions= self.fill_transactions()    





