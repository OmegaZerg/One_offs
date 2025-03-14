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
        if self.card1 > self.card2:
            return 1
        elif self.card2 > self.card1:
            return 2
        elif self.card1 == self.card2:
            return 0


class LowCardRound(Round):
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

    def resolve_round(self):
        if self.card1 < self.card2:
            return 1
        elif self.card2 < self.card1:
            return 2
        elif self.card1 == self.card2:
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
print (middle_result)
