import random

class Card:
	def __init__(self):
		self.suit=["Hearts","Diamonds","Clubs","Spades"]
		self.value=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
	def __repr__(self):
		return f"{self.value[random.randint(0,len(self.value)-1)]} of {self.suit[random.randint(0,len(self.suit)-1)]}"

class Deck:
	def __init__(self):
		all_cards=Card()
		self.deck=[f"{v} of {s}" for s in all_cards.suit for v in all_cards.value]
		# self.deck=[]
		# for s in all_cards.suit:
		# 	for v in all_cards.value:
		# 		self.deck.append(f"{v} of {s}")
	def __repr__(self):
		return f"Deck of {len(self.deck)} cards"
	def count(self):
		return len(self.deck)
	def _deal(self,number):
		if self.count()==0:
			raise ValueError("All cards have been dealt")
		elif number == 1:
			self.dealt_card=self.deck.pop()
		elif number <= self.count():
			self.dealt_card=[]
			for i in range(0,number):
				self.dealt_card.append(self.deck.pop())
		else:
			self.dealt_card=[]
			for i in range(0,self.count()):
				self.dealt_card.append(self.deck.pop())
	def shuffle(self):
		if self.count()!=52:
			raise ValueError("Only full decks can be shuffled")
		else:
			random.shuffle(self.deck)
			return self
	def deal_card(self):
		self._deal(1)
		return self.dealt_card
	def deal_hand(self,number):
		self._deal(number)
		return self.dealt_card




my_deck=Deck()
print(my_deck)
my_deck.shuffle()
print(my_deck.deck)
hand=my_deck.deal_hand(5)
print(hand)
card=my_deck.deal_card()
print(card)
print(my_deck.count())
