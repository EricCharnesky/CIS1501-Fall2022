def get_product_name():
    product_name = input("Enter the name of the product")
    return product_name


def get_product_price(product_name):
    price = float(input(f"Enter the price of {product_name}"))
    return price


def get_product_quantity(product_name):
    quantity = int(input(f"Enter the quantity of {product_name}"))
    return quantity


def add_item_to_dictionary(store_dictionary, product_name, product_price, product_quantity ):
    store_dictionary[product_name] = { "price" : product_price, "quantity" : product_quantity }


def get_total_money():
    money = float(input("How much money do you have to spend?"))
    return money


def calculate_total_cost_of_item(store_dictionary, item_name, item_quantity):
    total_cost = item_quantity * store_dictionary[item_name]["price"]
    return total_cost


def get_quantity_available(store_dictionary, item_name):
    return store_dictionary[item_name]['quantity']


def reduce_quantity_available(store_dictionary, item_name, quantity):
    store_dictionary[item_name]['quantity'] -= quantity


def print_store(store_dictionary):
    for item in store_dictionary:
        print(f'{item} has {store_dictionary[item]["quantity"]} remaining')


# avoid using built-in function names - this is bad
def sum(some_list):
    return 10


def upper_case_string(some_string):
    some_string = some_string.upper()
    print(some_string)


def upper_case_list(some_list):
    # re-assign where some_list points - no longer modify the original
    some_list = ['a', 'b', 'c']
    for index in range(len(some_list)):
        some_list[index] = some_list[index].upper()


# optional parameters - always have to be at the end
def print_entire_name(first_name, last_name, middle_name='' ):
    print(first_name, middle_name, last_name)


def get_lucky_numbers():
    """
    some fun function!
    :return:
    """
    # automatically 'packs' into a tuple
    return 1, 2, 3, 4, 5

# unpacking with comma separators
number1, number2, number3, number4, number5 = get_lucky_numbers()

number_tuple = get_lucky_numbers()
number1 = number_tuple[0]
number2 = number_tuple[1]
number3 = number_tuple[2]
number4 = number_tuple[3]
number5 = number_tuple[4]

print(number_tuple)

print_entire_name('eric', 'charnesky')

name = "eric"
print(name)
upper_case_string(name)
print(name)

name = ['e', 'r', 'i', 'c']
print(name)
upper_case_list(name)
print(name)

store = {}

for item in range(5):
    name = get_product_name()
    price = get_product_price(name)
    quantity = get_product_quantity(name)
    # named arguments - helps avoid bugs with passing arguments in the wrong order
    add_item_to_dictionary(store_dictionary=store, product_price=price, product_quantity=quantity, product_name=name)

total_money = get_total_money()
receipt_costs = []
receipt_items = []
cheapest_item = 10000000
most_expensive_item = 0

for item in range(5):
    name = get_product_name()
    quantity_to_buy = get_product_quantity(name)

    if name not in store:
        print("We don't sell that")
    else:
        money_needed = calculate_total_cost_of_item(store, name, quantity_to_buy)
        if money_needed > total_money:
            print("You don't have enough money to buy that!")
        elif quantity_to_buy > get_quantity_available(store, name):
            print(f"We only have {get_quantity_available(store, name)} available!")
        else:
            total_money -= money_needed
            reduce_quantity_available(store, name, quantity_to_buy)
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

print_store(store)