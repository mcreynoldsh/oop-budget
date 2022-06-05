
from BudgetCategory import BudgetCategory
import csv
class Budget:
    def __init__(self,name, monthly_income):
        self.name = name
        self.monthly_income = monthly_income
        self.categories = [BudgetCategory("Living"),BudgetCategory("Food"),BudgetCategory("Travel"),BudgetCategory("Savings"),BudgetCategory("Leisure")]
        self.total_expenses = 0
        
    def load_monthly_budgets(self):
        budgets=[]
        with open(f"/Users/huntermcreynolds/code/exercises/Week2/oop-budget/data/Monthly_budgets.csv") as f :     
            student_reader = csv.DictReader(f,skipinitialspace=True)
            for i,row in enumerate(student_reader):
                self.categories[i].add_budget(int(row['monthly_budget']))
                    
    def input_monthly_budgets(self):
        for x in self.categories:
            monthly_exp= input(f"Input monthly budget for {x.name} category: ")
            x.add_budget(monthly_exp) 
            with open('/Users/huntermcreynolds/code/exercises/Week2/oop-budget/data/Monthly_budgets.csv', mode='a') as csv_file:
                fieldnames = ['categ_name','monthly_budget']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow({'categ_name': x.name, 'monthly_budget': monthly_exp})
       
    
    def create_category(self, name):
        self.categories.append(BudgetCategory(name))
    
    def list_expenses(self):
        for expense in self.categories:
            print(str(expense))

hunts_budge = Budget("Hunters", 9000)
hunts_budge.load_monthly_budgets()
hunts_budge.list_expenses()


