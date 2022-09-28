store = {}

for item in range(5):
    name = input("Enter the item name")
    price = float(input(f"Enter the price of {name}"))
    quantity_to_buy = int(input(f"Enter the quantity of {name}"))
    store[name] = {"price": price, "quantity": quantity_to_buy}

total_money = float(input("How much money do you have to spend?"))
receipt_costs = []
receipt_items = []
cheapest_item = 10000000
most_expensive_item = 0

for item in range(5):
    name = input("What do you want to buy?")
    quantity_to_buy = int(input(f"How many {name} do you want to buy?"))

    if name not in store:
        print("We don't sell that")
    else:
        money_needed = quantity_to_buy * store[name]["price"]
        if money_needed > total_money:
            print("You don't have enough money to buy that!")
        elif quantity_to_buy > store[name]["quantity"]:
            print(f"We only have {store[name]['quantity']} available!")
        else:
            # naive approach, but it works!
            if money_needed < cheapest_item:
                cheapest_item = money_needed
            if money_needed > most_expensive_item:
                most_expensive_item = money_needed

            total_money -= money_needed
            store[name]['quantity'] -= quantity_to_buy
            receipt_costs.append(money_needed)
            receipt_items.append(f"{quantity_to_buy} {name} - ${money_needed}")

for item in receipt_items:
    print(item)

print(f'Total Cost: ${sum(receipt_costs)}')

index_of_cheapest_item = receipt_costs.index(min(receipt_costs))
print(f"Cheapest item was {receipt_items[index_of_cheapest_item]}")

index_of_most_expensive_item = receipt_costs.index(max(receipt_costs))
print(f"The most expensive item was {receipt_items[index_of_most_expensive_item]}")

print(f"You have ${total_money} remaining")


print("remaining store items and quantities")
print(store)

for item in store:
    print(f'{item} has {store[item]["quantity"]} remaining')
