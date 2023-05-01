import random
import time
import os
clear_output = lambda: os.system('cls' if os.name in ('nt') else 'clear')

class Blackjack():
    

    def __init__(self):
        self.deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']
        self.player_hand = []
        self.dealer_hand = []
        self.player_in = True
        self.dealer_in = True
        clear_output()
        self.driver()

    def deal_cards(self, turn):
        card = random.choice(self.deck)
        turn.append(card)
        self.deck.remove(card)

    def calc_hand_total(self, turn):
        hand_total = 0
        face_card = ['J','Q','K']
        for card in turn:
            if card in range(1, 11):
                hand_total += card
            elif card in face_card:
                hand_total += 10
            else:
                if hand_total > 11:
                    hand_total += 1
                else:
                    hand_total += 11

        return hand_total

    def driver(self):
        for _ in range(2):
            self.deal_cards(self.dealer_hand)
            self.deal_cards(self.player_hand)
        while self.player_in or self.dealer_in:
            print(f'\nDealer hand (one card hidden):\n[{self.dealer_hand[0]}, ?]')
            print(f'\nPlayer hand:\n{self.player_hand}\nCurrent hand total:{self.calc_hand_total(self.player_hand)}\n')
            
            if self.player_in:
                stay_or_hit = input('Type S to stay or H to hit:').lower()
            if stay_or_hit == 's':
                self.player_in = False
            else:
                time.sleep(2)
                self.deal_cards(self.player_hand)

            if self.player_in == False and self.calc_hand_total(self.dealer_hand) > 16:
                self.dealer_in = False
            elif self.player_in == False and self.calc_hand_total(self.dealer_hand) < 16:
                print(f'Dealer hand:\n{self.dealer_hand}')
                time.sleep(2)
                print(f'Dealer total:\n{self.calc_hand_total(self.dealer_hand)}')
                time.sleep(2)
                print('Dealer forced to hit below 16')
                self.deal_cards(self.dealer_hand)
                print(f'Dealer hand:\n{self.dealer_hand}')

            if self.calc_hand_total(self.player_hand) >=21:
                break
            elif self.calc_hand_total(self.dealer_hand) >=21:
                break

        self.game_results()

    def game_results(self):
        print(f'\nPlayer has {self.player_hand} for a total of {self.calc_hand_total(self.player_hand)} and the dealer has {self.dealer_hand} for a total of {self.calc_hand_total(self.dealer_hand)}')

        if self.calc_hand_total(self.dealer_hand) > 21 and self.calc_hand_total(self.player_hand) < 22:
            print('Dealer bust. Player wins.')
        elif self.calc_hand_total(self.player_hand) > 21 and self.calc_hand_total(self.dealer_hand) < 22:
            print('Player bust. Dealer wins.')
        elif self.calc_hand_total(self.player_hand) > 21 and self.calc_hand_total(self.dealer_hand) > 21:
            print('Player and dealer bust, this hand\'s a wash.')
        elif len(self.dealer_hand) == 2 and self.calc_hand_total(self.dealer_hand) == 21:
            print('The dealer wins with a blackjack, this must be rigged...')
        elif len(self.player_hand) == 2 and self.calc_hand_total(self.player_hand) == 21:
            print('Blackjack! Player wins!')
        elif self.calc_hand_total(self.dealer_hand) == self.calc_hand_total(self.player_hand):
            print('Dealer wins the tie.')
        elif self.calc_hand_total(self.dealer_hand) == 21:
            print('Dealer wins.')
        elif self.calc_hand_total(self.player_hand) == 21:
            print('Blackjack, player wins!')
        elif self.calc_hand_total(self.dealer_hand) > self.calc_hand_total(self.player_hand) and self.calc_hand_total:
            print('Dealer wins.')
        elif self.calc_hand_total(self.dealer_hand) < self.calc_hand_total(self.player_hand):
            print('Player wins.')    

        play_again = input('\nWould you like to play again? Y/N\n').lower()
        if play_again == 'y':
            Blackjack()
        else:
            print('Thanks for playing!')

Blackjack()