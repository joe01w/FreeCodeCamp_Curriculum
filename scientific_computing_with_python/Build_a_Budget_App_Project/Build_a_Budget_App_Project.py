class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        # Add a deposit to the ledger
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        # Check if there are enough funds, and if so, add a negative entry to the ledger
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        # Calculate the current balance by summing the amounts in the ledger
        balance = sum(item["amount"] for item in self.ledger)
        return balance

    def transfer(self, amount, category):
        # Transfer amount to another category if funds are available
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        # Check if the amount is less than or equal to the current balance
        return amount <= self.get_balance()

    def __str__(self):
        # Create a formatted string to represent the category
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            # Limit the description to 23 characters and format the amount
            description = f"{item['description'][:23]:23}"
            amount = f"{item['amount']:7.2f}"
            items += f"{description}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    
    # Calculate total withdrawals for each category
    total_spent = 0
    category_spent = []
    
    for category in categories:
        spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        category_spent.append(spent)
        total_spent += spent
    
    # Calculate percentage spent for each category (rounded down to nearest 10)
    percentages = [int((spent / total_spent) * 100 // 10) * 10 for spent in category_spent]
    
    # Create the chart from 100 down to 0
    chart = ""
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for percent in percentages:
            if percent >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"
    
    # Add the horizontal line
    chart += "    -" + "---" * len(categories) + "\n"
    
    # Find the longest category name for vertical labels
    max_len = max(len(category.name) for category in categories)
    
    # Add the category names vertically (correct alignment)
    for i in range(max_len):
        chart += "    "  # Adjusted spacing (removed one space)
        for category in categories:
            if i < len(category.name):
                chart += f" {category.name[i]} "
            else:
                chart += "   "
        chart += " \n"
    
    return title + chart.rstrip("\n")

# Example output

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
clothing.deposit(500, "initial deposit")
clothing.withdraw(25.55, "clothes shopping")

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(100, "car maintenance")

entertainment = Category("Entertainment")
entertainment.deposit(600, "initial deposit")
entertainment.withdraw(100, "movies")
entertainment.withdraw(50, "concert")

health = Category("Health")
health.deposit(300, "initial deposit")
health.withdraw(45.50, "gym membership")
health.withdraw(30, "doctor visit")

# Perform transfers
food.transfer(50, clothing)
entertainment.transfer(20, health)

# Print the categories
print(food)
print(clothing)
print(auto)
print(entertainment)
print(health)

# Print the spend chart
print(create_spend_chart([food, clothing, auto, entertainment, health]))