class Budget():

    def __init__(self, user, food, clothing, entertainment):
        self.user = user
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment


    def printsome(self):
        print('something')

    def deposit_food(self, new_food):
        self.food = self.food + new_food

   
    def deposit_clothing(self,new_clothing):
        self.clothing = self.clothing + new_clothing

    def deposit_entertainment(self,new_entertainment):
        self.entertainment = self.entertainment + new_entertainment

      
    def withdraw_food(self, new_food, new_clothing, new_entertainment):
        
        self.food = self.food - new_food


    def withdraw_clothing(self, new_food, new_clothing, new_entertainment):

        self.clothing = self.clothing - new_clothing
    
    def withdraw_entertainment(self, new_food, new_clothing, new_entertainment):
        
        self.entertainment = self.entertainment - new_entertainment
   
    def compute_balance(self):
        total_balance = self.clothing+self.entertainment+self.food

        print( f" For {self.user}, The budget for food is {self.food}, The budget for entertainment is {self.entertainment} and the budget for clothing is {self.clothing} and the total balance is {total_balance} ")

    def transfer_foodtocloth(self, transfer_amount):
        self.food = self.food - transfer_amount
        self.clothing = self.clothing + transfer_amount

    def transfer_clothtofood(self, transfer_amount):
        self.food = self.food + transfer_amount
        self.clothing = self.clothing - transfer_amount

    def transfer_foodtoentertainment(self, transfer_amount):
        self.food = self.food - transfer_amount
        self.entertainment = self.entertainment + transfer_amount

    def transfer_entertainment_to_food(self, transfer_amount):
        self.food = self.food + transfer_amount
        self.entertainment = self.entertainment - transfer_amount

    def transfer_cloth_to_entertainment(self, transfer_amount):
        self.entertainment = self.entertainment + transfer_amount
        self.clothing = self.clothing - transfer_amount

    def transfer_entertainment_to_cloth(self, transfer_amount):
        self.entertainment = self.entertainment - transfer_amount
        self.clothing = self.clothing + transfer_amount

        
tree = Budget('rex',1,2,3)

tree.compute_balance()



