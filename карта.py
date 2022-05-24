import requests



class Card:
   emo_SPADES = "U0002660"
   emo_CLUBS = "U0002663"
   emo_HEARTS = "U0002665"
   emo_DIAMONDS = "U0002666"

   def __init__(self, card):
       if isinstance(card, dict):
           self.__card_JSON = card
           self.code = card["code"]
           self.suit = card["suit"]
           self.value = card["value"]
           self.cost = self.get_cost_card()
           self.color = self.get_color_card()
           self.__imagesPNG_URL = card["images"]["png"]
           self.__imagesSVG_URL = card["images"]["svg"]

       elif isinstance(card, str):
           self.__card_JSON = None
           self.code = card

           value = card[0]
           if value == "J":
               self.value = "JACK"
           elif value == "Q":
               self.value = "QUEEN"
           elif value == "K":
               self.value = "KING"
           elif value == "A":
               self.value = "ACE"
           elif value == "J":
               self.value = "JACK"
           else:
               self.value = value

           suit = card[1]
           if suit == "S":
               self.suit = "SPADES"
           elif suit == "C":
               self.suit = "CLUBS"
           elif suit == "H":
               self.suit = "HEARTS"
           elif suit == "D":
               self.suit = "DIAMONDS"

           self.cost = self.get_cost_card()
           self.color = self.get_color_card()

   def get_cost_card(self):
       if self.value == "JACK":
           return 2
       elif self.value == "QUEEN":
           return 3
       elif self.value == "KING":
           return 4
       elif self.value == "ACE":
           return 11
       elif self.value == "JOKER":
           return 1
       else:
           return int(self.value)

   def get_color_card(self):
       if self.suit == "SPADES":  # Пики
           return "BLACK"
       elif self.suit == "CLUBS":  # Крести
           return "BLACK"
       elif self.suit == "HEARTS":  # Черви
           return "RED"
       elif self.suit == "DIAMONDS":  # Буби
           return "RED"



class Game21:
   def __init__(self, deck_count=1):
       new_pack = self.new_pack(deck_count)
       if new_pack is not None:
           self.pack_card = new_pack
           self.remaining = new_pack["remaining"],
           self.card_in_game = []
           self.arr_cards_URL = []
           self.score = 0
           self.status = None


   def new_pack(self, deck_count):
       response = requests.get(f"https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={deck_count}")

       if response.status_code != 200:
           return None
       pack_card = response.json()
       return pack_card


   def get_cards(self, card_count=1):
       if self.pack_card == None:
           return None
       if self.status != None:
           return None

       deck_id = self.pack_card["deck_id"]
       response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={card_count}")

       if response.status_code != 200:
           return False

       new_cards = response.json()
       if new_cards["success"] != True:
           return False
       self.remaining = new_cards["remaining"]

       arr_newCards = []
       for card in new_cards["cards"]:
           card_obj = Card(card)
           arr_newCards.append(card_obj)
           self.card_in_game.append(card_obj)
           self.score = self.score + card_obj.cost
           self.arr_cards_URL.append(card["image"])

       if self.score > 21:
           self.status = False
           text_game = "Очков: " + str(self.score) + " ВЫ ПРОИГРАЛИ!"

       elif self.score == 21:
           self.status = True
           text_game = "ВЫ ВЫИГРАЛИ!"
       else:
           self.status = None
           text_game = "Очков: " + str(self.score) + " в колоде осталось карт: " + str(self.remaining)

       return text_game



if __name__ == "__main__":
   print("Этот код должен использоваться ТОЛЬКО в качестве модуля!")