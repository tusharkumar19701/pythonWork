"""
Category class. It should be able to instantiate objects based on different budget categories like food, clothing,
and entertainment. When objects are created, they are passed in the name of the category.
The class should have an instance variable called ledger that is a list.

Here is an example usage:

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)


And here is an example of the output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96



function create_spend_chart() takes different categories and prints a bar graph showing percentage spend on that category 
along with the name of the category.
Output looks like this:

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     

"""



class Category:
    def __init__(self,cat_name):
        self.cat_name = cat_name
        self.ledger = []
    
    def __str__(self):
        name = self.cat_name.center(30,"*")
        name += '\n'

        items = ''
        for i in self.ledger:
            items += i['description'][:23].ljust(23)
            items += f"{i['amount']:.2f}".rjust(7)
            items += '\n'
        total = self.get_balance()
        items += f'Total: {total:.2f}'
        res = name + items
        return res

    
    def deposit(self,amount,description=""):
        self.ledger.append({'amount':amount,'description':description})
    
    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount':-(amount),'description':description})
            return True
        return False
    
    def transfer(self,amount,bud_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {bud_category.cat_name}")
            bud_category.deposit(amount,f'Transfer from {self.cat_name}')
            return True
        return False

    def get_balance(self):
        total = 0
        for i in self.ledger:
            amt = i['amount']
            total = total + amt
        return total
    
    def check_funds(self,amount):
        if amount <= self.get_balance():
            return True
        return False


def create_spend_chart(categories):
    expense = {}
    for item in categories:
        s1 = 0
        for ele in item.ledger:
            if ele['amount'] < 0:
                s1 += abs(ele['amount'])
        expense[item.cat_name] = s1 #
    total = sum(expense.values())
    percent = {}

    for catego in expense.keys():
        if total > 0:
            percent[catego] = int(round(expense[catego] / total,2) * 100)
            percent[catego] = (percent[catego] // 10) * 10
        else:
            percent[catego] = 0
    result = 'Percentage spent by category\n'
    for i in range(100,-10,-10):
        result += str(i).rjust(3) + '| '
        for p in percent.values():
            if p >= i:
                result += 'o  '
            else:
                result += '   '
        result += '\n'
    result += ' '*4
    result += '-'*(len(categories)*3 + 1)
    result += '\n'
    result += '     '

    array = list(percent.keys())
    length = max([len(i) for i in array])

    for i in range(length):
        for name_of_category in array:
            if i < len(name_of_category):
                result += name_of_category[i]+'  '
            else:
                result += '   '
        if i < length-1:
            result += '\n'
            result += '     '
    return result

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

business = Category('Business')
business.deposit(1000,'deposit')
business.transfer(100,clothing)
print(food)


print(create_spend_chart([food,clothing,business]))
