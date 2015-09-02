# Calculates maximum possible burst out of the basic mage deck
import itertools as it

"""
Class Definitions
"""

class Minion(object):
    def __init__(self, name, mana, attack, health, state = False, frozen = False, taunt = False):
        self.name = name
        self.mana = mana
        self.attack = attack
        self.health = health
        self.state = state
        self.frozen = frozen
        self.taunt = taunt
    
    #def can_attack(self):
    #    if self.state == False:
    #        damage = 0
    #    else:
    #        damage = self.attack
    
    def damaged(self, n):
        if self.health <= n:
            self.health = 0
            self.state = False
        else:
            self.health -= n
    
    def frostbolt(self):
        if self.health <= 3:
            self.health = 0
            self.state = False
        else:
            self.health -= 3
            self.state = False
            self.frozen = True

class Spell(object):
    def __init__(self, name, mana, damage, state = True):
        self.name = name
        self.mana = mana
        #self.target = target
        self.attack = damage
        self.state = state
    
    #def dealdmg(self):
    #    for minion in self.target:
    #        if minion.health <= self.attack:
    #            minion.health = 0
    #            minion.state = False
    #        else:
    #            minion.health -= self.attack


"""
Minions in Deck
"""

Ogre = Minion("Ogre", 6, 6, 7)
Wolfrider = Minion("Wolfrider", 3, 3, 1, True)
Crocolisk = Minion("Crocolisk", 2, 2, 3)
Murloc_Raider = Minion("Murloc_Raider", 1, 2, 1)
Oasis_Snapjaw = Minion("Oasis_Snapjaw", 4, 2, 7)
Novice_Engineer = Minion("Novice_Engineer", 2, 1, 1)
Bloodfen_Raptor = Minion("Bloodfen_Raptor", 2, 3, 2)
Senjin = Minion("Senjin", 4, 3, 5, taunt = True)

w1 =Minion('w1',1,1,1, True)
w2 =Minion('w2',2,2,2, True)
w3 =Minion('w3',3,3,3, True)
w4 =Minion('w4',4,4,4, True)
w5 =Minion('w5',2,5,5, True)
w6 =Minion('w6',1,6,6, True)

"""
Spells in Deck
"""

Fireball = Spell("Fireball", 4, 6)

"""
Calculation
"""

hand = [w1,w2,w3,w4,w5,w6, Fireball]
friendly_board = [Crocolisk,Ogre]
enemy_board = [Crocolisk, Ogre]

def damage(mana, hand, board):
    
    attacking = []
    manaboard = []
    
    for minion in friendly_board:
        if minion.frozen == False and minion.health > 0:
            minion.state = True
            attacking.append(minion)
            manaboard.append(minion.mana)
            minion.mana = 0
            
    for card in hand:
        if card.state == True:
            attacking.append(card)
            
    dmg = 0
    for i in range(len(attacking)+1):
        for cards in it.combinations(attacking, i):
            cards = list(cards)
            cards_mana = []
            cards_dmg = []
            for card in cards:
                cards_mana.append(card.mana)
                cards_dmg.append(card.attack)
            if sum(cards_mana) > mana: continue
            else:
                for minion in enemy_board:
                    if minion.taunt == False: continue
                    else:
                        pass
            if sum(cards_dmg) <= dmg: continue
            else:
                dmg = sum(cards_dmg)
                names = []
                for card in cards:
                    names.append(card.name)
    
    for i in range(len(friendly_board)):
        friendly_board[i].mana = manaboard[i]
    
    return dmg, names


print damage(7,friendly_board,enemy_board)