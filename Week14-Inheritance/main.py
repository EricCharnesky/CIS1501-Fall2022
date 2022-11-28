
class Dealer:

    def __init__(self):
        self.hand = []


class Player:

    def __init__(self):
        self.name = ""


class Game:

    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()


class Card:

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit


# deck HAS cards - not IS A card
class Deck:

    def __init__(self):
        self.cards = []
        self.cards.append( Card("Ace", "Spades"))


class Item:

    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    def get_total_cost(self):
        return self._price * self._quantity


class TaxableItem(Item):

    def __init__(self, name, price, quantity, tax_rate):
        super().__init__(name, price, quantity)
        #Item.__init__(self, name, price, quantity)

        # please sanity check
        self._tax_rate = tax_rate

    def get_total_cost(self):
        return super().get_total_cost() * ( 1 + self._tax_rate )


coke = TaxableItem("coke", 2.5, 1, .06)
print(coke.get_total_cost())


class Book:

    def __init__(self, author, title, publisher):
        self._author = author
        self._title = title
        self._publisher = publisher

    def get_display_string(self):
        return f"{self._title} written by {self._author} published by {self._publisher}"


class PictureBook(Book):

    def __init__(self, author, title, publisher, illustrator):
        # has to happen first
        Book.__init__(self, author, title, publisher)
        self.illustrator = illustrator

    def get_display_string(self):
        # does the super class version
        return f"{super().get_display_string()} illustrated by {self.illustrator}"


foxInSocks = PictureBook("Dr. Suess", "Fox in Socks", "publisher", "illustrator?")
print(foxInSocks.get_display_string())