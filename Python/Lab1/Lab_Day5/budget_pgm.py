#
# Create a Budget class that can instantiate objects based on different budget categories like food, 
# clothing, and entertainment. These objects should allow for depositing and withdrawing funds from 
# each category, as well computing category balances and transferring balance amounts between categories

class Budget:

    def __init__(self,pot,funds):
        self.pot = pot
        self.funds = funds

    def depositFunds(self):
        deposit_amount = int(input("Enter the amount to deposit into the pot " + self.pot))
        print(deposit_amount)
        self.funds = self.funds + deposit_amount  #calculation
        print("Funds = ",self.funds)  
        
    def withdrawFunds(self):
        withdraw_amount = int(input("How much would you like to withdraw from the pot " + self.pot))
        print(withdraw_amount)
        self.funds = self.funds - withdraw_amount  #calc
        print("Funds = ",self.funds)
        
    def transferFunds(self, otherPot):
        transfer_amount = int(input("How much do you wish to transfer from the pot " + self.pot + "into the pot " + otherPot.pot))
        print(transfer_amount)
        otherPot.funds = otherPot.funds + transfer_amount
        print(otherPot.funds)
        self.funds = self.funds - transfer_amount
        print(self.funds)

# main

# food budget
food_budget = Budget("Food",400)

# Deposit 
food_budget.depositFunds()

# Withdraw 
food_budget.withdrawFunds()

#**************

# Clothing budget
clothing_budget = Budget("Clothing",70)

# Deposit funds into the pot:
clothing_budget.depositFunds()

# Withdraw funds from the pot:
clothing_budget.withdrawFunds()

#**************

# Entertainment budget
entertainment_budget = Budget("Entertainment",100)

# Deposit funds into the pot:
entertainment_budget.depositFunds()

# Withdraw funds from the pot:
entertainment_budget.withdrawFunds()

#======


# Transfer funds 
food_budget.transferFunds(clothing_budget)
clothing_budget.transferFunds(entertainment_budget)