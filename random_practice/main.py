"""
#Practice
class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1, y1, x2, y2):
        pass


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.fire_range = fire_range
        self.height = height
        self.width = width
        self.__hit_box = Rectangle(self.pos_x - self.width/2, self.pos_y - self.height/2, self.pos_x + self.width/2, self.pos_y + self.height/2)
        

    def in_area(self, x1, y1, x2, y2):
        self.area = Rectangle(x1, y1, x2, y2)
        return self.area.overlaps(self.__hit_box)
    
    #This method was added
    def breathe_fire(self, target_x, target_y):
        distance = ((target_x - self.pos_x)**2 + (target_y - self.pos_y)**2)**0.5
        return distance <= self.fire_range



# Don't touch below this line


class Rectangle:
    def overlaps(self, rect):
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2
        
SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)

    def __eq__(self, other):
        return (
            self.rank_index == other.rank_index and self.suit_index == other.suit_index
        )

    def __lt__(self, other):
        if self.rank_index == other.rank_index:
            return self.suit_index < other.suit_index
        return self.rank_index < other.rank_index

    def __gt__(self, other):
        if self.rank_index == other.rank_index:
            return self.suit_index > other.suit_index
        return self.rank_index > other.rank_index

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Round:
    def resolve_round(self):
        raise NotImplementedError("Subclasses must implement resolve_round()")


class HighCardRound(Round):
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

    def resolve_round(self):
        if self.card1.__gt__(self.card2):
            return 1
        elif self.card2.__gt__(self.card1):
            return 2
        elif self.card1.__eq__(self.card2):
            return 0


class LowCardRound(Round):
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

    def resolve_round(self):
        if self.card1.__lt__(self.card2):
            return 1
        elif self.card2.__lt__(self.card1):
            return 2
        elif self.card1.__eq__(self.card2):
            return 0

#Card closest to the middle(Number of "8", index of 6) wins.
class MiddleCardRound(Round):
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        self.card1_rank = abs(card1.rank_index - 6)
        self.card2_rank = abs(card2.rank_index - 6)

    def resolve_round(self):
        if self.card1_rank == self.card2_rank:
            if self.card1.suit_index > self.card2.suit_index:
                return 1
            elif self.card2.suit_index > self.card1.suit_index:
                return 2
            else:
                print("Tie Game!")
                return 0
        elif self.card1_rank < self.card2_rank:
            return 1
        elif self.card2_rank < self.card1_rank:
            return 2
        
#card1 = Card("Jack", "Clubs")
#card1 = Card("2", "Clubs")
card1 = Card("2", "Spades")
card2 = Card("2", "Spades")

middle_round = MiddleCardRound(card1, card2)
middle_result = middle_round.resolve_round()
print (middle_result)"
"""