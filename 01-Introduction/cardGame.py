from typing import List
import random

class Card: 
    """Represents a single card in a deck, with a suit and a number.

    Attributes:
        suit (str): The suit of the card (e.g., "hearts", "spades").
        number (str): The number of the card (e.g., "A", "10", "K").
    """
    def __init__(self, suit: str = None, number: str = None): 
        """Initializes a new card with the given suit and number.

        Args:
            suit (str): The suit of the card (e.g., "hearts", "spades").
            number (str): The number of the card (e.g., "A", "10", "K").
        """
        self.suit = suit
        self.number = number
    
    def get_suit(self) -> str: 
        """Returns the suit of the card.

        Returns:
            str: The suit of the card.
        """
        return self.suit
    
    def get_number(self) -> str: 
        """Returns the number of the card.

        Returns:
            str: The number of the card.
        """
        return self.number
    
    def __str__(self) -> str: 
        """Returns a string representation of the card, combining the suit and number.

        Returns:
            str: The string representation of the card.
        """
        return f"{self.suit} - {self.number}"
    
    
class Deck: 
    """Represents a deck of cards, with methods to draw, return, and reset the deck.

    Attributes:
        suits (List[str]): A list of suits in a deck.
        numbers (List[str]): A list of numbers (or faces) in a deck.
        cards (List[Card]): A list of all cards in the deck.
    """
    def __init__(self) -> None: 
        """
        Initializes a deck of cards and shuffles it.
        """
        self.suits = ["clubs", "hearts", "diamonds", "spades"]
        self.numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                        "J", "Q", "K"]
        self.cards = self.reset_deck()
        
    def draw(self, number: int) -> List[Card]: 
        """Draws a specified number of cards from the deck.

        Args:
            number (int): The number of cards to draw.

        Returns:
            List[Card]: A list of drawn cards.

        Raises:
            AssertionError: If the number of cards to draw exceeds the number of cards in the deck.
        """
        assert number < len(self.cards), f"Cannot draw {number} cards from deck of size {len(self.cards)}"
        
        random.shuffle(self.cards)
        drawn = []
        for _ in range(number):
            drawn.append(self.cards.pop())
            
        return drawn
        
    def return_drawn(self, cards: List[Card]) -> None: 
        """Returns a list of cards to the deck.

        Args:
            cards (List[Card]): A list of cards to return to the deck.
        """
        self.cards.extend(cards)
        
    def reset_deck(self) -> None:
        """Resets the deck to its full set of 52 cards, including all suits and numbers.

        Returns:
            List[Card]: A full deck of 52 cards.
        """
        return [Card(suit, number) 
                for suit in self.suits 
                for number in self.numbers]
        
    def get_card_number_int(self, card: Card) -> int: 
        """Returns the integer value corresponding to the card's number.

        Args:
            card (Card): The card for which to fetch the integer value.

        Returns:
            int: The integer value of the card.
        """
        return self.numbers.index(card.number) + 1

        
class CountTillTwentyOne: 
    """A game where the player must achieve a score of exactly 21 points by drawing and dropping cards.

    Attributes:
        deck (Deck): The deck of cards used in the game.
        count_swaps (int): The number of times cards have been swapped.
        in_hand (List[Card]): A list of cards currently in the player's hand.
    """
    def __init__(self): 
        """Initializes the game by creating a deck and drawing 3 initial cards for the player."""
        self.deck = Deck()
        self.count_swaps = 0
        self.in_hand = self.deck.draw(3)
        print("""
Welcome to Count Till 21!
In this game, your goal is to achieve a score of exactly 21 points by drawing and dropping cards.

How to Play:
- You start with 3 cards.
- Each card has a point value based on its number (Ace = 1, 2 = 2, ..., King = 13).
- You can drop one of your current cards in exhange of new one to improve your score.
- Keep track of your score, and try to make it exactly 21 points.
- Choose a card to drop (1, 2, or 3) to exchange for a new one.
  
Good luck, and aim for 21! 

---""")
        
    def get_a_card(self) -> Card: 
        """Draws a single card from the deck.

        Returns:
            Card: The drawn card.
        """
        return self.deck.draw(1)[0]
    
    def put_a_card(self, card: Card) -> None: 
        """Returns a card back to the deck.

        Args:
            card (Card): The card to return to the deck.
        """
        self.deck.return_drawn([card])
        
    def get_score(self) -> int: 
        """Computes the total score of the cards in hand.

        Returns:
            int: The total score of the cards in hand.
        """
        return sum(self.deck.get_card_number_int(card) for card in self.in_hand)
    
    def print_cards_and_score(self) -> None: 
        """Prints the cards in hand and the current score."""
        print("\nCards in hand: ")
        for i, card in enumerate(self.in_hand): 
            print(f"Card {i}: {card}")
        print(f"Score: {self.get_score()}")
            
    def play(self) -> None: 
        """Starts the game and allows the player to play until they reach 21 points"""
        self.print_cards_and_score()
        while self.get_score() != 21: 
            index = 0
            while index not in {1, 2, 3}: 
                try:
                    index = int(input("Card to drop (1, 2, 3): "))
                    if index not in {1, 2, 3}: 
                        print("Invalid choice! Choose between 1, 2, or 3.")
                except ValueError:
                    print("Invalid input! Please enter a number between 1 and 3.")
            
            index -= 1  # Adjust to 0-based index
            self.put_a_card(self.in_hand[index])
            self.in_hand.pop(index)
            self.in_hand.append(self.get_a_card())
            self.print_cards_and_score()
            
        print("You have won the game!")
        
        
if __name__ == "__main__": 
    CountTillTwentyOne().play()
