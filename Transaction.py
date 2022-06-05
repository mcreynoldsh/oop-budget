class Transaction:
    def __init__(self, trans_name, trans_amount):
        self.trans_name = trans_name
        self.trans_amount = trans_amount
    
    def __str__(self):
        return f"""
            {self.trans_name}: ${self.trans_amount}"""