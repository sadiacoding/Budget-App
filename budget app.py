class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

# Deposit 
    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })
     
# Withdraw 
    def withdraw(self, amount, description=""):
        if self.get_balance()>=amount:
            self.ledger.append({
                "amount": -amount,
            "description": description
            })
            return True
        else:
            return False
       
# Get Balance
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total+=item["amount"]
        return total

# Transfer
    def transfer(self, amount, category):
        if self.get_balance()>=amount:

            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")

            return True
        else:
            return False

# Check Funds
    def check_funds(self, amount):
        if amount>self.get_balance():
            return False
        else:
            return True

# Total
    def __str__(self):
        title=self.name.center(30, '*')+"\n"

        items=""

        for item in self.ledger:
            desc=item['description'][:23]
            amt="{:.2f}".format(item["amount"])
            items+=f"{desc:<23}{amt:>7}\n"
            
        total="Total: "+str(self.get_balance())

        return title+items+total

# Spend Chart
def create_spend_chart(categories):
    spends=[]

    # Spendings
    for category in categories:
        total=0
        for item in category.ledger:
            if item['amount'] < 0:
                total+=-item['amount']

        spends.append(total)

    # Total Spending
    total_spend=sum(spends)

    # Percentages
    percentages=[]
    for spend in spends:
        p=(spend/total_spend)*100
        percentages.append(int(p//10)*10)

    # Chart
    chart="Percentage spent by category"+"\n"
    # (percentagse)
    for i in range(100, -1, -10):
        line=str(i).rjust(3)+"| "
        for percentage in percentages:
            if percentage >= i:
                line+="o  "
            else:
                line+="   "
        chart+=line+"\n"
    # (line)
    line="    " + "-" * (len(categories) * 3 + 1)
    chart+=line+"\n"
    # (names)
    names=[c.name for c in categories]
        
    max_length=max(len(n) for n in names)
        

    for i in range(max_length):
        line="     "
        for name in names:
            if i<len(name):
                line+=name[i]+"  "
            else:
                line+="   "

        chart+=line+"\n"

    return chart.rstrip("\n")