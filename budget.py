from builtins import range
import os 
import copy as cp

# Main Class
class Category:
  
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
      

    def deposit(self, amount, desc=""):
        self.ledger.append({'amount': amount,'description': desc,
        })
        self.balance += amount


    def withdraw(self, amount, desc=""):
        if self.check_funds(amount) == False:
            return False

        self.balance -= amount
        self.ledger.append({'amount': -amount,'description': desc,
        })

        return True


    def transfer(self, amount, cat):
        if self.withdraw(amount, "Transfer to " + cat.name) == False:
            return False

        cat.deposit(amount, "Transfer from " + self.name)
        return True


    def get_balance(self):
        return self.balance


    def check_funds(self, amount):
        return self.balance >= amount

  
    def test_functions(self):
      
      if True:
        return None

  
    def spent(self):
        b = 0
        for t in self.ledger:
            amount = t["amount"]
            if amount < 0:
                b += amount

        return -b


    def __str__(self):
        show = [self.name.center(30, "*")]
        for t in self.ledger:
            desc = t["description"][0:23]
            t = t["amount"]
            show.append(f"{desc:<23}{t:>7.2f}")

        show.append(f"Total: {self.balance}")
        return "\n".join(show)


def create_spend_chart(categories):
    spend = [c.spent() for c in categories]
    total = sum(spend)
    percen = [s * 100 / total for s in spend]
    show = ["Percentage spent by category"]
    for i in range(0, 11):
        level = 10 * (10 - i)
        s = f'{level:>3}| '
        
        for p in percen:
            if p >= level:
                s += "o  "
            else:
                s += "   "
        show.append(s)
    padd = " " * 4
    len_spnd = len(spend)
    show.append(padd + "-" * 3 * len_spnd + "-")

    names = [c.name for c in categories]

    for i in range(0, max(map(len, names))):
        s = padd
        for x in names:
            len_x = len(x)
            s += " "
            s += x[i] if len_x > i else " "
            s += " "

        show.append(s + " ")

    return "\n".join(show)