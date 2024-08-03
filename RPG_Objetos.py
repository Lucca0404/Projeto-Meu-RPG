import os
from time import sleep
import random
from msvcrt import getch
from Biblioteca_RPG import print_attribut, roll_dice
#from pygame import mixer
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self):
        self._name = None
        self._rpg_class = None
        self.items = []
        self.exp = 0
    
        self.life = None
        self.aux_life = self.life
        self.mana = None
        self.dex = None
        self.cos = None
        self.strn = None
        self.car = None
        self.wis = None
        self.mag = None
        self.heal = None
        self.ca = None
        self.weak = None
        self.weapon = None

        self.acrobatics = None
        self.arcana = None
        self.athletics = None
        self.deception = None
        self.intimidation = None
        self.perception = None
        self.persuasion = None
        self.sleight_of_hand = None
        self.special_attack = None
        self.stealth = None

    @property
    @abstractmethod
    def name(self): ...

    @property
    def inf(self):
        print(f'Informações sobre {self.name}\n\n'
              f'Status:\n'
              f'- Força: {self.strn}\n'
              f'- Constituição: {self.cos}\n'
              f'- Destreza: {self.dex}\n'
              f'- Magia: {self.mag}\n'
              f'- Carisma: {self.car}\n'
              f'- Sabedoria: {self.wis}\n'
              f'- Cura: {self.heal}\n'
              f'- Vida: {self.life}\n'
              f'- Fraqueza: {self.weak}\n'
              f'- Classe de Armadura: {self.ca}\n\n'

              f'Skills:\n'
              f'- Acrobacia: {self.acrobatics}\n'
              f'- Arcana: {self.arcana}\n'
              f'- Atletismo: {self.athletics}\n'
              f'- Enganação: {self.deception}\n'
              f'- Intimidação: {self.intimidation}\n'
              f'- Percepção: {self.perception}\n'
              f'- Persuasão: {self.persuasion}\n'
              f'- Prestidigitação: {self.sleight_of_hand}\n'
              f'- Furtividade: {self.stealth}\n'
              f'- Ataque Especial: {self.special_attack}\n')
              
    @property
    def show_life(self):
         print_attribut(self.life)

    @property
    def show_heal(self):
         print_attribut(self.heal)

    @staticmethod
    def rolling_dice(attribut):
        return roll_dice(attribut)
    
    @abstractmethod
    def special_charge(self) -> bool: ...

    @abstractmethod
    def class_attack(self): ...
    
class Warrior(Character):

    class_bonus = 2

    def __init__(self):
        super().__init__()
        self._rpg_class = 'warrior'
        self.items = [Machado]

        #stats
        self.life = random.randrange(50,61)
        self.aux_life = self.life
        self.mana = 30
        self.dex = 2
        self.cos = 4
        self.strn = 4
        self.mag = 0
        self.car = 2
        self.wis = 1
        self.ca = 16
        self.weak = 'magic'
        self.weapon = Machado

        #skills
        self.acrobatics = self.dex
        self.arcana = self.mag
        self.athletics = self.strn + Warrior.class_bonus
        self.deception = self.car
        self.intimidation = self.car + Warrior.class_bonus
        self.perception = self.wis
        self.persuasion = self.car
        self.sleight_of_hand = self.dex
        self.special_attack = 'Executar'
        self.stealth = self.dex

    def special_charge(self) -> bool:
        if self.mana >= 50:
            return True
        return False

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    def class_attack(self,defender : Character):
        result = Character.rolling_dice(self.strn)
        if result == 1+self.strn:
            return 'CriticError'
        elif result == 20+self.strn:
            return 'CriticHit'
        elif result < defender.ca:
            return 'Error'
        return 'Hit'
    
    def class_action(self,test_skill,test_difficult):
        result = Character.rolling_dice(test_skill)
        if result == 1+test_skill:
            return 'CriticError'
        elif result == 20+test_skill:
            return 'CriticHit'
        elif result < test_difficult:
            return 'Error'
        return 'Hit'

class Rogue(Character):

    class_bonus = 4

    def __init__(self):
        super().__init__()
        self._rpg_class = 'rogue'
        self.items = [Adaga]

        #stats
        self.life = random.randrange(40,46)
        self.aux_life = self.life
        self.mana = 40
        self.dex = 4
        self.cos = 2
        self.strn = 2
        self.mag = 0
        self.car = 3
        self.wis = 2
        self.ca = 15
        self.weak = 'slash'
        self.weapon = Adaga

        #skills
        self.acrobatics = self.dex + Rogue.class_bonus
        self.arcana = self.mag
        self.athletics = self.strn
        self.deception = self.car + Rogue.class_bonus
        self.intimidation = self.car 
        self.perception = self.wis
        self.persuasion = self.car
        self.sleight_of_hand = self.dex + Rogue.class_bonus
        self.special_attack = 'Sumir'
        self.stealth = self.dex + Rogue.class_bonus

    def special_charge(self) -> bool:
        if self.mana >= 60:
            return True
        return False

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    def class_attack(self, defender : Character):
        result = Character.rolling_dice(self.dex)
        if result == 1+self.dex:
            return 'CriticError'
        elif result == 20+self.dex:
            return 'CriticHit'
        elif result < defender.ca:
            return 'Error'
        return 'Hit'
    
    def class_action(self,test_skill,test_difficult):
        result = Character.rolling_dice(test_skill)
        if result == 1+test_skill:
            return 'CriticError'
        elif result == 20+test_skill:
            return 'CriticHit'
        elif result < test_difficult:
            return 'Error'
        return 'Hit'

class Mage(Character):

    class_bonus = 2

    def __init__(self):
        super().__init__()
        self._rpg_class = 'mage'
        self.items = [Cajado]

        #stats
        self.life = random.randrange(30,36)
        self.aux_life = self.life
        self.mana = 60
        self.dex = 2
        self.cos = 1
        self.strn = 1
        self.mag = 4
        self.car = 2
        self.wis = 3
        self.ca = 13
        self.weak = 'piercing'
        self.weapon = Cajado

        #skills
        self.acrobatics = self.dex
        self.arcana = self.mag + Mage.class_bonus
        self.athletics = self.strn
        self.deception = self.car
        self.intimidation = self.car 
        self.perception = self.wis + Mage.class_bonus
        self.persuasion = self.car
        self.sleight_of_hand = self.dex
        self.special_attack = 'Ignimpacto'
        self.stealth = self.dex

    def special_charge(self) -> bool:
        if self.mana >= 100:
            return True
        return False

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    def class_attack(self, defender : Character):
        result = Character.rolling_dice(self.mag)
        if result == 1+self.mag:
            return 'CriticError'
        elif result == 20+self.mag:
            return 'CriticHit'
        elif result < defender.ca:
            return 'Error'
        return 'Hit'

    def class_action(self,test_skill,test_difficult):
        result = Character.rolling_dice(test_skill)
        if result == 1+test_skill:
            return 'CriticError'
        elif result == 20+test_skill:
            return 'CriticHit'
        elif result < test_difficult:
            return 'Error'
        return 'Hit'
    
class Hunter(Character):

    class_bonus = 2

    def __init__(self):
        super().__init__()
        self._rpg_class = 'hunter'
        self.items = [Besta]

        #stats
        self.life = random.randrange(45,56)
        self.aux_life = self.life
        self.mana = 40
        self.dex = 4
        self.cos = 3
        self.strn = 3
        self.mag = 0
        self.car = 1
        self.wis = 2
        self.ca = 15
        self.weak = 'slash'
        self.weapon = Besta

        #skills
        self.acrobatics = self.dex 
        self.arcana = self.mag 
        self.athletics = self.strn + Hunter.class_bonus
        self.deception = self.car
        self.intimidation = self.car 
        self.perception = self.wis 
        self.persuasion = self.car
        self.sleight_of_hand = self.dex
        self.special_attack = 'Disparo mortal'
        self.stealth = self.dex + Hunter.class_bonus

    def special_charge(self) -> bool:
        if self.mana >= 80:
            return True
        return False

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    def class_attack(self, defender : Character):
        result = Character.rolling_dice(self.dex)
        if result == 1+self.dex:
            return 'CriticError'
        elif result == 20+self.dex:
            return 'CriticHit'
        elif result < defender.ca:
            return 'Error'
        return 'Hit'
    
    def class_action(self,test_skill,test_difficult):
        result = Character.rolling_dice(test_skill)
        if result == 1+test_skill:
            return 'CriticError'
        elif result == 20+test_skill:
            return 'CriticHit'
        elif result < test_difficult:
            return 'Error'
        return 'Hit'

class Priest(Character):

    class_bonus = 2

    def __init__(self):
        super().__init__()
        self._rpg_class = 'priest'
        self.items = [Pergaminhos]

        #stats
        self.life = random.randrange(50,61)
        self.aux_life = self.life
        self.heal = random.randrange(30,61)
        self.mana = 60
        self.dex = 0
        self.cos = 4
        self.strn = 1
        self.mag = 3
        self.car = 1
        self.wis = 4
        self.ca = 14
        self.weak = 'piercing'
        self.weapon = Pergaminhos

        #skills
        self.acrobatics = self.dex 
        self.arcana = self.mag + Priest.class_bonus
        self.athletics = self.strn 
        self.deception = self.car
        self.intimidation = self.car 
        self.perception = self.wis + Priest.class_bonus
        self.persuasion = self.car
        self.sleight_of_hand = self.dex
        self.special_attack = 'Sepultar'
        self.stealth = self.dex 

    def special_charge(self) -> bool:
        if self.mana >= 80:
            return True
        return False

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    def class_attack(self, defender : Character):
        result = Character.rolling_dice(self.wis)
        if result == 1+self.wis:
            return 'CriticError'
        elif result == 20+self.wis:
            return 'CriticHit'
        elif result < defender.ca:
            return 'Error'
        return 'Hit'
    
    def class_heal(self):
        result = Character.rolling_dice(self.wis)
        if result == 1+self.wis:
            return 'CriticError'
        elif result == 20+self.wis:
            return 'CriticHeal'
        elif result < self.ca:
            return 'Error'
        return 'Heal'
    
    def class_action(self,test_skill,test_difficult):
        result = Character.rolling_dice(test_skill)
        if result == 1+test_skill:
            return 'CriticError'
        elif result == 20+test_skill:
            return 'CriticHit'
        elif result < test_difficult:
            return 'Error'
        return 'Hit'

class Paladin(Character):

    class_bonus = 2

    def __init__(self):
        super().__init__()
        self._rpg_class = 'paladin'
        self.items = [Espada]

        #stats
        self.life = random.randrange(50,56)
        self.aux_life = self.life
        self.heal = random.randrange(10,31)
        self.mana = 50
        self.dex = 1
        self.cos = 3
        self.strn = 3
        self.mag = 1
        self.car = 3
        self.wis = 2
        self.ca = 17
        self.weak = 'magic'
        self.weapon = Espada

        #skills
        self.acrobatics = self.dex 
        self.arcana = self.mag 
        self.athletics = self.strn + Paladin.class_bonus
        self.deception = self.car
        self.intimidation = self.car + Paladin.class_bonus
        self.perception = self.wis 
        self.persuasion = self.car
        self.sleight_of_hand = self.dex
        self.special_attack = 'Redenção'
        self.stealth = self.dex

    def special_charge(self) -> bool:
        if self.mana >= 100:
            return True
        return False

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    def class_attack(self, defender : Character):
        result = Character.rolling_dice(self.strn)
        if result == 1+self.strn:
            return 'CriticError'
        elif result == 20+self.strn:
            return 'CriticHit'
        elif result < defender.ca:
            return 'Error'
        return 'Hit'
    
    def class_heal(self):
        result = Character.rolling_dice(self.car)
        if result == 1+self.car:
            return 'CriticError'
        elif result == 20+self.car:
            return 'CriticHeal'
        elif result < self.ca:
            return 'Error'
        return 'Heal'
    
    def class_action(self,test_skill,test_difficult):
        result = Character.rolling_dice(test_skill)
        if result == 1+test_skill:
            return 'CriticError'
        elif result == 20+test_skill:
            return 'CriticHit'
        elif result < test_difficult:
            return 'Error'
        return 'Hit'

class Monster(Character):
    def __init__(self):
        self._monster_class = None
        self._level = None

    @property
    @abstractmethod
    def level(self): ...

class Slunker(Monster):
    def __init__(self):
        super().__init__()
        self._monster_class = 'slunker'
        self.mana = 30
        self.weapon = Espada
        self.weak = 'magic'

    def special_charge(self) -> bool:
        if self.mana >= 60:
            return True
        return False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    def class_attack(self, defender : Character):
        result = Character.rolling_dice(self.strn)
        if result == 1+self.strn:
            return 'CriticError'
        elif result == 20+self.strn:
            return 'CriticHit'
        elif result < defender.ca:
            return 'Error'
        return 'Hit'

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self,level):
        self._level = level

    def give_attribut(self):
        match self._level:
            case 1:
                self.life = random.randrange(10,31)
                self.aux_life = self.life
                self.exp = 15
                self.dex = 0
                self.cos = 1
                self.strn = 1
                self.car = 0
                self.wis = 0
                self.mag = 0
                self.ca = 10
            case 2:
                self.life = random.randrange(30,51)
                self.aux_life = self.life
                self.exp = 30
                self.dex = 1
                self.cos = 1
                self.strn = 2
                self.car = 1
                self.wis = 0
                self.mag = 0
                self.ca = 11
            case 3:
                self.life = random.randrange(60,71)
                self.aux_life = self.life
                self.exp = 60
                self.dex = 2
                self.cos = 2
                self.strn = 3
                self.car = 1
                self.wis = 0
                self.mag = 0
                self.ca = 12
            case 4:
                self.life = random.randrange(80,101)
                self.aux_life = self.life
                self.exp = 100
                self.dex = 3
                self.cos = 3
                self.strn = 4
                self.car = 1
                self.wis = 0
                self.mag = 0
                self.ca = 14
            case 5:
                self.life = random.randrange(100,121)
                self.aux_life = self.life
                self.exp = 145
                self.dex = 3
                self.cos = 4
                self.strn = 5
                self.car = 2
                self.wis = 1
                self.mag = 0
                self.ca = 15
            case 6:
                self.life = random.randrange(120,141)
                self.aux_life = self.life
                self.exp = 190
                self.dex = 4
                self.cos = 5
                self.strn = 5
                self.car = 2
                self.wis = 2
                self.mag = 0
                self.ca = 15
            case 7:
                self.life = random.randrange(140,161)
                self.aux_life = self.life
                self.exp = 240
                self.dex = 5
                self.cos = 6
                self.strn = 6
                self.car = 2
                self.wis = 2
                self.mag = 0
                self.ca = 16
            case 8:
                self.life = random.randrange(160,181)
                self.aux_life = self.life
                self.exp = 310
                self.dex = 6
                self.cos = 7
                self.strn = 7
                self.car = 2
                self.wis = 2
                self.mag = 0
                self.ca = 17
            case 9:
                self.life = random.randrange(180,211)
                self.aux_life = self.life
                self.exp = 400
                self.dex = 7
                self.cos = 8
                self.strn = 8
                self.car = 2
                self.wis = 3
                self.mag = 0
                self.ca = 18
            case 10:
                self.life = random.randrange(250,301)
                self.aux_life = self.life
                self.exp = 500
                self.dex = 9
                self.cos = 9
                self.strn = 9
                self.car = 3
                self.wis = 3
                self.mag = 0
                self.ca = 20

class Flunker(Monster):
    def __init__(self):
        super().__init__()
        self._monster_class = 'flunker'
        self.mana = 30
        self.weapon = Besta
        self.weak = 'slash'

    def special_charge(self) -> bool:
        if self.mana >= 60:
            return True
        return False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    def class_attack(self, defender : Character):
        result = Character.rolling_dice(self.dex)
        if result == 1+self.dex:
            return 'CriticError'
        elif result == 20+self.dex:
            return 'CriticHit'
        elif result < defender.ca:
            return 'Error'
        return 'Hit'

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self,level):
        self._level = level

    def give_attribut(self):
        match self._level:
            case 1:
                self.life = random.randrange(5,21)
                self.aux_life = self.life
                self.exp = 10
                self.dex = 1
                self.cos = 1
                self.strn = 0
                self.car = 0
                self.wis = 0
                self.mag = 0
                self.ca = 8
            case 2:
                self.life = random.randrange(20,31)
                self.aux_life = self.life
                self.exp = 25
                self.dex = 2
                self.cos = 1
                self.strn = 1
                self.car = 0
                self.wis = 0
                self.mag = 0
                self.ca = 8
            case 3:
                self.life = random.randrange(40,51)
                self.aux_life = self.life
                self.exp = 55
                self.dex = 3
                self.cos = 2
                self.strn = 1
                self.car = 1
                self.wis = 0
                self.mag = 0
                self.ca = 10
            case 4:
                self.life = random.randrange(50,61)
                self.aux_life = self.life
                self.exp = 90
                self.dex = 4
                self.cos = 3
                self.strn = 1
                self.car = 1
                self.wis = 0
                self.mag = 0
                self.ca = 11
            case 5:
                self.life = random.randrange(60,71)
                self.aux_life = self.life
                self.exp = 130
                self.dex = 4
                self.cos = 4
                self.strn = 2
                self.car = 2
                self.wis = 1
                self.mag = 0
                self.ca = 12
            case 6:
                self.life = random.randrange(70,81)
                self.aux_life = self.life
                self.exp = 170
                self.dex = 5
                self.cos = 5
                self.strn = 3
                self.car = 3
                self.wis = 2
                self.mag = 0
                self.ca = 13
            case 7:
                self.life = random.randrange(80,101)
                self.aux_life = self.life
                self.exp = 220
                self.dex = 6
                self.cos = 6
                self.strn = 4
                self.car = 3
                self.wis = 3
                self.mag = 0
                self.ca = 14
            case 8:
                self.life = random.randrange(100,111)
                self.aux_life = self.life
                self.exp = 290
                self.dex = 8
                self.cos = 7
                self.strn = 4
                self.car = 3
                self.wis = 3
                self.mag = 0
                self.ca = 14
            case 9:
                self.life = random.randrange(110,121)
                self.aux_life = self.life
                self.exp = 350
                self.dex = 9
                self.cos = 8
                self.strn = 5
                self.car = 3
                self.wis = 3
                self.mag = 0
                self.ca = 15
            case 10:
                self.life = random.randrange(130,151)
                self.aux_life = self.life
                self.exp = 450
                self.dex = 10
                self.cos = 9
                self.strn = 5
                self.car = 4
                self.wis = 4
                self.mag = 0
                self.ca = 17

class Hunker(Monster):
    def __init__(self):
        super().__init__()
        self._monster_class = 'hunker'
        self.weapon = Pergaminhos
        self.mana = 30
        self.weak = 'piercing'

    def special_charge(self) -> bool:
        if self.mana >= 60:
            return True
        return False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    def class_attack(self, defender : Character):
        result = Character.rolling_dice(self.mag)
        if result == 1+self.mag:
            return 'CriticError'
        elif result == 20+self.mag:
            return 'CriticHit'
        elif result < defender.ca:
            return 'Error'
        return 'Hit'
    
    def class_heal(self):
        result = Character.rolling_dice(self.wis)
        if result == 1+self.wis:
            return 'CriticError'
        elif result == 20+self.wis:
            return 'CriticHeal'
        elif result < self.ca:
            return 'Error'
        return 'Heal'

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self,level):
        self._level = level

    def give_attribut(self):
        match self._level:
            case 1:
                self.life = random.randrange(10,21)
                self.aux_life = self.life
                self.heal = random.randrange(10,21)
                self.exp = 20
                self.dex = 0
                self.cos = 1
                self.strn = 0
                self.car = 0
                self.wis = 1
                self.mag = 1
                self.ca = 10
            case 2:
                self.life = random.randrange(30,51)
                self.aux_life = self.life
                self.heal = random.randrange(20,31)
                self.exp = 40
                self.dex = 0
                self.cos = 2
                self.strn = 0
                self.car = 0
                self.wis = 2
                self.mag = 1
                self.ca = 11
            case 3:
                self.life = random.randrange(50,71)
                self.aux_life = self.life
                self.heal = random.randrange(30,41)
                self.exp = 70
                self.dex = 0
                self.cos = 3
                self.strn = 0
                self.car = 1
                self.wis = 2
                self.mag = 2
                self.ca = 12
            case 4:
                self.life = random.randrange(70,91)
                self.aux_life = self.life
                self.heal = random.randrange(40,51)
                self.exp = 110
                self.dex = 0
                self.cos = 3
                self.strn = 0
                self.car = 1
                self.wis = 3
                self.mag = 3
                self.ca = 13
            case 5:
                self.life = random.randrange(90,111)
                self.aux_life = self.life
                self.heal = random.randrange(50,61)
                self.exp = 160
                self.dex = 1
                self.cos = 3
                self.strn = 0
                self.car = 1
                self.wis = 4
                self.mag = 4
                self.ca = 14
            case 6:
                self.life = random.randrange(110,131)
                self.aux_life = self.life
                self.heal = random.randrange(60,71)
                self.exp = 200
                self.dex = 2
                self.cos = 4
                self.strn = 0
                self.car = 2
                self.wis = 4
                self.mag = 5
                self.ca = 15
            case 7:
                self.life = random.randrange(130,151)
                self.aux_life = self.life
                self.heal = random.randrange(70,81)
                self.exp = 260
                self.dex = 2
                self.cos = 5
                self.strn = 0
                self.car = 2
                self.wis = 5
                self.mag = 6
                self.ca = 16
            case 8:
                self.life = random.randrange(150,171)
                self.aux_life = self.life
                self.heal = random.randrange(80,91)
                self.exp = 340
                self.dex = 2
                self.cos = 6
                self.strn = 0
                self.car = 3
                self.wis = 6
                self.mag = 7
                self.ca = 17
            case 9:
                self.life = random.randrange(170,191)
                self.aux_life = self.life
                self.heal = random.randrange(90,101)
                self.exp = 440
                self.dex = 2
                self.cos = 7
                self.strn = 0
                self.car = 3
                self.wis = 7
                self.mag = 9
                self.ca = 18
            case 10:
                self.life = random.randrange(200,251)
                self.aux_life = self.life
                self.heal = random.randrange(100,141)
                self.exp = 600
                self.dex = 3
                self.cos = 8
                self.strn = 0
                self.car = 3
                self.wis = 8
                self.mag = 10
                self.ca = 19

class Items:
    def __init__(self) -> None:
        self._name = None
        self._category = None
        self._power = None
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self,category):
        self._category = category

    @property
    def power(self):
        return self._power
    @power.setter
    def power(self,power):
        self._power = power

    def give_function(self):
        match self._category:
            case 'heal':
                self.cure = self.power
            case 'damage':
                self.damage = self.power

class Weapon(Items):

    def __init__(self,duration,type,damage):
        super().__init__()
        self.duration = duration
        self.type = type
        self.damage = damage
        self._category = 'weapon'

class Battle():

    def attack(self, attacker : Character,defender : Character):

        print(f'{attacker.name} tenta atacar {defender.name}')
        sleep(2.2)
        result = attacker.class_attack(defender)
        match result:
            case 'CriticError':
                sleep(3)
                print(f'{defender.name} esquivou do ataque')
                sleep(3)
                print(f'{attacker.weapon.name} perdeu 2 de duração')
                sleep(3)
                attacker.weapon.duration -= 5
            case 'CriticHit':
                damage = random.randrange(attacker.weapon.damage - 10,attacker.weapon.damage + 10)
                sleep(3)
                print(f'{attacker.name} ataca ferozmente {defender.name}')
                sleep(3)
                if attacker.weapon.type == defender.weak:
                    print('Nossa o ataque foi super-efetivo')
                    print(f'{defender.name} recebeu {damage*4} de dano')
                    sleep(3)
                    defender.aux_life -= damage*4
                else:
                    print(f'{defender.name} recebeu {damage*2} de dano')
                    sleep(3)
                    defender.aux_life -= damage*2
                attacker.mana += 10
                if attacker.mana > 100:
                    attacker.mana = 100
            case 'Error':
                sleep(3)
                print(f'{defender.name} esquivou do ataque')
                sleep(3)
            case 'Hit':
                damage = random.randrange(attacker.weapon.damage - 10,attacker.weapon.damage + 10)
                sleep(3)
                print(f'{attacker.name} acertou {defender.name}')
                sleep(3)
                if attacker.weapon.type == defender.weak:
                    print('Nossa o ataque foi super-efetivo')
                    print(f'{defender.name} recebeu {damage*2} de dano')
                    sleep(3)
                    defender.aux_life -= damage*2
                else:
                    print(f'{defender.name} recebeu {damage} de dano')
                    sleep(3)
                    defender.aux_life -= damage
                attacker.mana += 10
                if attacker.mana > 100:
                    attacker.mana = 100
        if defender.aux_life <= 0:
            print(f'{defender.name} foi derrotado')
            attacker.exp += defender.exp
            sleep(2)
            print(f'{attacker.name} ganhou {defender.exp} pontos de experiência')
            sleep(2)
            return True
        else:
            return False
        
    def heal(self, char: Character):
        print(f'{char.name} tenta se curar')
        sleep(2.2)
        result = char.class_heal()
        match result:
            case 'CriticError':
                sleep(3)
                print(f'Pelo resto da batalha {char.name} possuirá -5 de vida')
                char.aux_life -= 5
            case 'CriticHeal':
                sleep(3)
                print(f'{char.name} se cura perfeitamente')
                sleep(3)
                print(f'{char.name} recuperou toda a sua vida')
                sleep(3)
                char.aux_life = char.life
                char.mana += 5
                if char.mana > 100:
                    char.mana = 100
            case 'Error':
                sleep(3)
                print(f'Nossa, parece que {char.name} falhou em se curar')
                sleep(3)
            case 'Heal':
                if char.aux_life != char.life:
                    print(f'Ótimo, {char.name} conseguiu se curar')
                    sleep(3)
                    print(f'{char.name} se cura em {char.heal}')
                    sleep(3)
                    char.aux_life += char.heal
                    if char.aux_life > char.life:
                        char.aux_life = char.life
                else:
                    print(f'A vida de {char.name} já está cheia')
                char.mana += 5
                if char.mana > 100:
                    char.mana = 100

    def use_item(self, user : Character, item : Items, target : Character=None):
        match item.category:
            case 'heal':
                user.aux_life += item.cure
                if user.aux_life > user.life:
                    user.aux_life = user.life
                user.items.remove(item)
            case 'damage':
                target.aux_life -= item.damage
                user.items.remove(item)
    
    def use_special_attack(self, attacker : Character, *defender : Character):

        if attacker.special_charge():
            match attacker.special_attack:
                case 'Executar':
                    print(f'{attacker.name} ergue sua arma e usa Executar')
                    sleep(4)
                    if defender[0].aux_life < defender[0].life/2:
                        print(f'{defender[0].name} é completamente retalhado')
                        defender.aux_life = 0
                    else:
                        print(f'{defender[0].name} é recebe cortes em cada um de seus orgãos')
                        sleep(3)
                        defender[0].aux_life /= 2
                        print('a vida dele é reduzida pela metade')
                    attacker.mana -= 50
                case 'Sumir':
                    print(f'{attacker.name} recua e usa Sumir')
                    sleep(2)
                    print(f'{attacker.name} transforma-se em fumaça e fica completamente invisível')
                    sleep(4)
                    print(f'Por alguns turnos {attacker.name} possuirá +10 de CA')
                    sleep(3)
                    print('Mas seus ataques serão reduzidos pela metade')
                    attacker.mana -= 60
                    return True
                case 'Ignimpacto':
                    print(f'{attacker.name} ergue suas mãos e prepara Ignimpacto')
                    sleep(3)
                    print('Várias bolas de fogo azul gigantes surgem em meio ao céu')
                    sleep(3)
                    print('De repente todas elas caem sobre seus inimigos')
                    sleep(3)
                    print(f'Todos eles recebem {attacker.life} de dano')
                    for char in defender:
                        char.aux_life -= attacker.life
                    attacker.mana = 0
                case 'Disparo mortal':
                    print(f'{attacker.name} ergue sua arma e prepara Disparo mortal')
                    sleep(3)
                    print(f'{defender[0].name} é perfurado no meio de seu coração a uma velocidade próxima da do som')
                    sleep(3)
                    print(f'{defender[0].name} recebeu {attacker.weapon.damage**3} de dano')
                    defender[0].aux_life -= attacker.weapon.damage**2
                    attacker.mana -= 80
                case 'Sepultar':
                    print(f'{attacker.name} une suas mãos e prepara Sepultar')
                    sleep(3)
                    print(f'{defender[0].name} é mumificado e preso em um caixão')
                    sleep(3)
                    print(f'Ele ficará alguns turnos sem poder realizar nenhuma ação')
                    attacker.mana -= 80
                case 'Redenção':
                    print(f'{attacker.name} fecha seus olhos e prepara Redenção')
                    sleep(3)
                    print(f'A sua fé o concede os dons divinos da regeneração')
                    sleep(3)
                    print(f'{attacker.name} recuperou toda a sua vida e restaurou sua arma completamente')
                    attacker.aux_life = attacker.life
                    attacker.weapon.duration = 10
        if defender[0].aux_life <= 0:
            print(f'{defender.name[0]} foi derrotado')
            attacker.exp += defender.exp[0]
            sleep(2)
            print(f'{attacker.name} ganhou {defender.exp[0]} pontos de experiência')
            sleep(2)
            return True
        else:
            return False

def start_battle(protagonist : Character, *enemys : Monster):
    battle = Battle()

    enemys_num = 0

    for enemy in enemys:
        if enemys_num:
            print(f'e {enemy.name}',end=' ')
            enemys_num+=1
        else:
            print(f'{protagonist.name} entrou em combate com {enemy.name}',end=' ')
            enemys_num+=1

    turn_order = sorted([protagonist,*enemys],key= lambda obj: obj.dex,reverse=True)

    print(f'\n\nA ordem dos turnos será:')
    sleep(2)
    cont = 1
    for char in turn_order:
        print(f'{cont}º',char.name)
        cont += 1
        sleep(1)
    
    char_alive = turn_order.copy()
    char_alive.remove(protagonist)

    while True:
        for char in turn_order:
            if char == protagonist:
                while True:
                    os.system('cls')
                    print('Seu turno começou, qual sua ação?\n\n'
                          f' [1] Atacar\t\tVida:{protagonist.aux_life}\n',
                          f'[2] Curar\t\tMana:{protagonist.mana}',
                          f'\n [3] Usar um item\t{protagonist.weapon.name} {'está em boas condições' if protagonist.weapon.duration > 5 else 'está quase quebrando'}\n',
                          f'[4] Ataque especial\tEspecial: {'carregado' if protagonist.special_charge() else 'carregando...'}\n')
                    choice = getch()
                    match choice.decode():
                        case '1':
                            print('Qual o alvo do seu ataque?')
                            target_num = 1
                            for enemy in char_alive:
                                print(f'[{target_num}] {enemy.name}')
                                target_num += 1
                            print('\nAperte "Q" para voltar')
                            target = getch().lower()
                            if target.decode() == 'q':
                                continue
                            target = int(target.decode())
                            target -= 1

                            battle.attack(protagonist,char_alive[target])
                            if char_alive[target].aux_life <= 0:
                                turn_order.remove(char_alive[target])
                                char_alive.remove(char_alive[target])
                            if protagonist.weapon.duration <= 0:
                                print(f'{protagonist.weapon.name} Quebrou')
                                sleep(2)
                                protagonist.weapon = None
                            break
                        case '2':
                            if not protagonist.heal:
                                print('Seu personagem não tem poderes de cura')
                                sleep(4)
                                continue
                            battle.heal(protagonist)
                            break
                        case '3':
                            print('Qual item você quer usar?')
                            target_num = 1
                            for item in protagonist.items:
                                print(f'[{target_num}] {item.name}')
                                target_num += 1
                            print('\nAperte "Q" para voltar')
                            target = getch().lower()
                            if target.decode() == 'q':
                                continue
                            target = int(target.decode())
                            target -= 1
                            if protagonist.items[target].category == 'heal':
                                print(f'{protagonist.name} usou {protagonist.items[target].name}')
                                sleep(3)
                                print(f'Recuperou {protagonist.items[target].cure} de vida')
                                battle.use_item(protagonist,protagonist.items[target])
                            elif protagonist.items[target]._category == 'weapon':
                                if protagonist.items[target] == protagonist.weapon:
                                    print('Você já está com essa arma equipada')
                                    sleep(3)
                                    continue
                                print(f'{protagonist.name} equipou {protagonist.items[target].name}')
                                protagonist.weapon = protagonist.items[target]
                            else:
                                print('Qual inimigo você quer atacar?')
                                target_num = 1
                                for enemy in char_alive:
                                    print(f'[{target_num}] {enemy.name}')
                                    target_num += 1
                                print('\nAperte "Q" para voltar')
                                target_e = getch().lower()
                                if target_e.decode() == 'q':
                                    continue
                                target_e = int(target_e.decode())
                                target_e -= 1
                                print(f'{protagonist.name} usou {protagonist.items[target].name}')
                                sleep(3)
                                print(f'{enemys[target_e].name} recebeu {protagonist.items[target].damage} de dano')
                                battle.use_item(protagonist,protagonist.items[target],enemys[target_e])
                            break
                        case '4':
                            if not protagonist.special_charge():
                                print('Seu especial ainda não está carregado')
                                sleep(4)
                                continue
                            if isinstance(protagonist,Rogue):
                                battle.use_special_attack(protagonist)
                                turns = random.randrange(1,4)
                                protagonist.ca += 10
                                protagonist.weapon.damage //=2
                                break
                            if isinstance(protagonist,Paladin):
                                battle.use_special_attack(protagonist)
                            if isinstance(protagonist,Mage):
                                battle.use_special_attack(protagonist,*enemys)
                                break
                            print('Qual o alvo do seu ataque?')
                            target_num = 1
                            for enemy in char_alive:
                                print(f'[{target_num}] {enemy.name}')
                                target_num += 1
                            print('\nAperte "Q" para voltar')
                            target = getch().lower()
                            if target.decode() == 'q':
                                continue
                            target = int(target.decode())
                            target -= 1
                            
                            battle.use_special_attack(protagonist,char_alive[target])
                            if isinstance(protagonist,Priest):
                                turns = random.randrange(1,4)
                                aux = char_alive[target].ca 
                                char_alive[target].ca = 0
                            break
                for enemy in char_alive:
                    if enemy.aux_life <= 0:
                        turn_order.remove(enemy)
                        char_alive.remove(enemy)
                if not char_alive:
                    print('Todos os inimigos foram derrotados')
                    sleep(3)
                    print('Você venceu parabéns, aperte qualquer botão para prosseguir')
                    pause = getch()
                    return True
                if isinstance(protagonist,Priest):
                    try:
                        if turns > 0:
                            turns -= 1
                            if turns == 0:
                                for enemy in char_alive:
                                    if enemy.ca == 0:
                                        enemy.ca = aux
                    except:
                        pass
                if isinstance(protagonist,Rogue):
                    try:
                        if turns > 0:
                            turns -= 1
                            if turns == 0:
                                protagonist.ca -= 10
                                protagonist.weapon.damage *= 2
                    except:
                        pass
            else:
                if char.ca == 0:
                    print(f'{char.name} está sepultado')
                    sleep(4)
                    continue
                if hasattr(char,'heal'):
                    if char.aux_life < char.life/4:
                        battle.heal(char)
                        continue
                battle.attack(char,protagonist)
                if protagonist.aux_life <= 0:
                    os.system('cls')
                    print('GAME OVER <0>')
                    exit()
                continue

#Armas Iniciais
Machado = Weapon(10,'slash',25)
Machado.name = 'Machado'
Adaga = Weapon(10,'piercing',15)
Adaga.name = 'Adaga'
Cajado = Weapon(10,'magic',30)
Cajado.name = 'Cajado'
Besta = Weapon(10,'piercing',20)
Besta.name = 'Besta'
Pergaminhos = Weapon(10,'magic',10)
Pergaminhos.name = 'Pergaminhos'
Espada = Weapon(10,'slash',25)
Espada.name = 'Espada'

#items
pocao = Items()
pocao.name = 'Poção'
pocao.power = 50
pocao.category = 'heal'
pocao.give_function()
bomba = Items()
bomba.name = 'Bomba'
bomba.power = 50
bomba.category = 'damage'
bomba.give_function()

Marcos_Paulo = Mage()
Marcos_Paulo.name = 'Marcos Paulo'
Lucca = Slunker()
Lucca.level = 3
Lucca.name = 'Lucca'
Lucca.give_attribut()
Alberto = Flunker()
Alberto.level = 1
Alberto.name = 'Alberto'
Alberto.give_attribut()