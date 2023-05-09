class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = list()
    self.balance = 0
  
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount

  def withdraw(self,amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      self.balance -= amount
      return True
    return False
  
  def get_balance(self):
    return self.balance

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    return False
  
  def check_funds(self, amount):
    if self.balance >= amount:
      return True
    return False

  def __str__(self):
    total = 0
    title = self.name.center(30, "*") + "\n"
    itemlist = str()
    for items in self.ledger:
      itemlist += (items["description"][:23].ljust(23) + ("{:.2f}".format(float(items["amount"]))[:7].rjust(7))) + "\n"
      ("{:.2f}".format(int(items["amount"]))[:7].rjust(7))
      total += items["amount"]
    lastline = "Total: " + str(total)
    itemlist.rstrip()
    return title + itemlist + lastline

def create_spend_chart(categories):
  firstline = "Percentage spent by category\n"
  
  spent_per_category = list()
  for category in categories:
    onecat = 0
    for withdraws in category.ledger:
      if withdraws["amount"] < 0:
        onecat += withdraws["amount"]
    spent_per_category.append(onecat)
    
  precentage = list()
  for x in spent_per_category:
    precentage.append((int(x/sum(spent_per_category)*100)) // 10 * 10)
  chartlines = str()
  for x in range(100,-10,-10):
    plus = ""
    for y in precentage:
      if y >= x:
        plus += " o "
      else:
        plus += "   "
    chartlines += (str(x).rjust(3) + "|" + plus + " \n")
    
  dashes = "    " + ("---" * len(precentage) + "-\n")
  
  namelist = list()
  count = -1
  for category in categories:
    count += 1
    for x in range(len(category.name)):
      if len(namelist) < x+1:
        namelist.append("    ")
      while len(namelist[x]) < count*3 + 4:
        namelist[x] += "   "
      namelist[x] += " " + category.name[x] + " "
      
  names = str()
  for x in namelist:
    names += x + " \n"
    
  result = (firstline + chartlines + dashes + names).rstrip("\n")
  return result