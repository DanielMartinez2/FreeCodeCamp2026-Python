import itertools

class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []
    
    def get_balance(self):        
        return sum(item['amount'] for item in self.ledger)

    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })
    
    def withdraw(self, amount, description=''):
        
        if self.check_funds(amount):
            self.ledger.append({
                'amount': - amount,
                'description': description
            })
            return True 
        return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')        
            deposit_value = category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False
    
    def check_funds(self, amount):
        balance = self.get_balance()
        return False if amount > balance else True
    
    def __str__(self):        
        
        header = self.name.center(30,'*')
        body = ''
        
        for record in self.ledger:           
            total = sum(item['amount'] for item in self.ledger)
            description = record['description'][:23]
            amount = f"{record['amount']:.2f}"
            body += (f'\n{description:<23}{amount:>7}')

        final_line = f'\nTotal: {total}'
        return header + body + final_line

def create_spend_chart(categories):
    list_categories_dict =  []
    total = 0
    for category in categories:
        
        withdraw_ledger = { 
            category.name: 0
        }        
        for record in category.ledger:
            if record['amount'] < 0:
                withdraw_ledger[category.name] += record['amount']               
                total += record['amount']
        list_categories_dict.append(withdraw_ledger)    
    
    percentage_categories = {}
    for item in list_categories_dict:
        for index,x in enumerate(item):
            percentage = abs(item[x] / total) * 100
            percentage_categories[x] = int(percentage / 10) * 10

    header = 'Percentage spent by category'
    body = ''

    for i in range(100, -10, -10):
        bars = ''

        for key, value in percentage_categories.items():
            bars += 'o  ' if value >= i else '   '

        body += f'\n{i:>3}| {bars}'

    names = list(percentage_categories.keys())

    separator = '\n    ' + '-' * (len(names) * 3 + 1)

    max_length = max(len(name) for name in names)

    legend = ''

    for i in range(max_length):
        legend += '\n     '

        for name in names:
            if i < len(name):
                legend += name[i] + '  '
            else:
                legend += '   '

    text = header + body + separator + legend
    return text

    
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
clothing.deposit(100)
food.transfer(50, clothing)
clothing.withdraw(55, 'skirt')
print(food)
print(clothing)
print(create_spend_chart([food,clothing]))
