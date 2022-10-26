# encapsulated the idea of a tree into a nice neat little class

# encapsulation allows us to 'protect' our attributes

# abstraction - we don't need to know the details - use public functions

# private attributes with public functions


class BankAccount:

    def __init__(self, owner, account_number):
        self._owner = owner
        self._account_number = account_number
        self._balance = 0

    def __eq__(self, other):
        return self._balance == other.get_balance() and \
            self._owner == other.get_owner() and \
            self._account_number == other.get_account_number()

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self._balance < other.get_balance()

    def __le__(self, other):
        return self._balance <= other.get_balance()

    def __gt__(self, other):
        return self._balance > other.get_balance()

    def __ge__(self, other):
        return self._balance >= other.get_balance()

    def __str__(self):
        return f"Bank account owner: {self._owner} " \
               f"- Number: {self._account_number} " \
                f"- Balance: {self._balance}"

    def get_account_number(self):
        return self._account_number

    def get_owner(self):
        return self._owner

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount


class Tree:

    # constructor - initializer
    # this runs when we create an instance of the class
    # init's job is to give values to the attributes
    def __init__(self):

        # using an underscore to start a variable name indicates it is 'private'
        # private means it shouldn't be accessed directly
        self._height_in_meters = 0
        self.type = ""
        self.color = ""

    # public set method, allows us to bounds checking for attributes
    def set_height_in_meters(self, height_in_meters):
        if height_in_meters > 0:
            self._height_in_meters = height_in_meters
        else:
            self._height_in_meters = 0

    def get_height_in_meters(self):
        return self._height_in_meters

    def grow(self):
        self._height_in_meters *= 1.1 # 10% height growth


class ElectricVehicle:

    # if you accept an argument in the init, and don't have a set, it's pretty much read only
    def __init__(self, make, model, battery_max_kilowatt_hours_capacity, kilometers_per_kilowatt_hour):
        self._make = make
        self._model = model
        # TODO should sanity check the capacity, we'll do that later
        self._battery_max_kilowatt_hours_capacity = battery_max_kilowatt_hours_capacity
        self._battery_current_kilowatt_hours = 0
        self._odometer_in_kilometers = 0

        # we know it doesn't work like this in real life
        self._kilometers_per_kilowatt_hour = kilometers_per_kilowatt_hour

    def get_battery_current_kilowatt_hours(self):
        return self._battery_current_kilowatt_hours

    def get_odometer_in_kilometers(self):
        return self._odometer_in_kilometers

    def get_battery_max_kilowatt_hours_capacity(self):
        return self._battery_max_kilowatt_hours_capacity

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_kilometers_per_kilowatt_hour(self):
        return self._kilometers_per_kilowatt_hour

    # pretend we did the arithmetic for hours charging to kilowatt hours
    def charge(self, kilowatt_hours_to_charge):
        # don't use input in classes - use the arguments
        #hours = float(input("Enter some value"))
        if kilowatt_hours_to_charge > 0:
            self._battery_current_kilowatt_hours += kilowatt_hours_to_charge
        if self._battery_current_kilowatt_hours > self._battery_max_kilowatt_hours_capacity:
            self._battery_current_kilowatt_hours = self._battery_max_kilowatt_hours_capacity

    def drive(self, kilometers_to_drive):
        kilowatts_required = kilometers_to_drive / self._kilometers_per_kilowatt_hour

        # do we have enough battery charge to drive that far
        if kilowatts_required <= self._battery_current_kilowatt_hours:
            self._battery_current_kilowatt_hours - kilowatts_required
            self._odometer_in_kilometers += kilometers_to_drive
            return True

        return False


def print_tree_details(tree):
    print("Tree Type: " + tree.type )
    print("Tree color: " + tree.color)
    print("Tree height: " + str(tree.get_height_in_meters()) + " meters")


checking = BankAccount("Eric", 123)
checking.deposit(10)
# print(str(checking))
print(checking)

savings = BankAccount("Eric", 234)
print(f"checking == savings : { checking == savings }")





# object is an instance of a class





maple_tree = Tree() # calls the tree __init__ method
maple_tree.type = "Maple"
maple_tree.color = "Orange"
maple_tree.set_height_in_meters(10)
# you can access private values, but you should not
# maple_tree._height_in_meters = -5

oak_tree = Tree()
oak_tree.type = "Oak"
oak_tree.color = "brown"
oak_tree.set_height_in_meters(-5)

print_tree_details(maple_tree)
print_tree_details(oak_tree)

maple_tree.grow()

print_tree_details(maple_tree)


bolt = ElectricVehicle("Chevy", "Bolt", 13, 7)
bolt.charge(500)

kilometers_to_drive = int(input("How many kilometers do you want to drive?"))

if bolt.drive(kilometers_to_drive):
    print("You had a nice drive")
else:
    print("You can't go that far, try again")