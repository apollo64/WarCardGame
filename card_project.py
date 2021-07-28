import random


class Suit:
    SYMBOLS = {'clubs':'♣','diamonds':'♦','hearts':'♥', 'spades':'♠'}

    def __init__(self, description):
        self._description = description
        self._symbol = Suit.SYMBOLS[description.lower()]

    @property
    def symbol(self):
        return self._symbol

    @property
    def description(self):
        return self._description



class Card(Suit):
    SPECIAL = {'Jack': 11, 'Queen':12, 'King': 13, 'Ace': 14}

    def __init__(self,suit, value):
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit
    @property
    def value(self):
        return self._value

    def is_special(self):
        return self._value >= 11

    def show(self):
        card_value = self._value
        card_suit = self._suit.description.capitalize()
        card_symbol = self._suit.symbol
        if self.is_special():
            # card_value = card_desription
            for key, value in Card.SPECIAL.items():
                if value == card_value:
                    card_value = key

            # card_value = Card.SPECIAL[card_value]


        print(f'{card_value} of {card_suit} {card_symbol}')





class Deck:
    SUITS = ("clubs", "diamonds", "hearts", "spades")

    def __init__(self, is_empty=False):
        self._cards = []

        if not is_empty:
            self.build()

    @property
    def size(self):
        return len(self._cards)

    def build(self):
        for suit in Deck.SUITS:
            for value in range(2,15):
                self._cards.append(Card(Suit(suit), value))



    def show(self):
        for card in self._cards:
            card.show()


    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if self._cards:
            return self._cards.pop()
        else:
            return None


    def add(self, card):
        self._cards.insert(0, card)


class Player:

    def __init__(self, name, deck, is_computer=False):
        self.name = name
        self._deck = deck
        self._is_computer = is_computer

    @property
    def deck(self):
        return self._deck

    @property
    def is_computer(self):
        return self._is_computer

    def has_empty_deck(self):
        return self._deck.size ==0

    def draw_card(self):
        if not self.has_empty_deck():
            return self._deck.draw()
        else:
            return None

    def add_card(self, card):
        self._deck.add(card)



