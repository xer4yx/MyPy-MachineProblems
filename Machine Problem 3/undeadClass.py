from undead import Undead

class Zombie(Undead):
    
    def __init__(self, name = None, hp = None):
        super().__init__(name, hp)
        super().appendAbility("Munch")
        
    def Attack(self, enemy):
        if super().getHP() > 50 :
            super().Attack(enemy)
        else:
            print(f'{self.getName()} is weakned therefore it cannot attack.')
            
    def isDead(self, dead = None):
        if dead == None and super().getHP() <= 0: 
            dead = True
        return super().isDead(dead)
            
    def getDamage(self):
        """Method for setting an attack damage for an instance

        Returns:
           super().getHP() * (float): sets the attack damage for the method Attack()
        """
        return super().getHP() * 0.5

    def Munch(self, enemy):
        if not self.isDead():
            super().setHP(super().getHP() + (enemy.getHP() * 0.5))
        else:
            print(f'{self.getName()} is weakned therefore it cannot attack.')

class Vampire(Undead):
    
    def __init__(self, name = None, hp = None):
        super().__init__(name, hp)
        super().setHP(120)
        super().appendAbility("Bite")
    
    def isDead(self, dead = None):
        if dead != None:
            dead = False
        return super().isDead(dead)

    def getDamage(self):
        return super().getHP()

    def Bite(self, enemy):
        """A method for health regeneration of an instance.

        Args:
            enemy (Instance): Sets what instance should get hp from
        """
        super().setHP(super().getHP() + (enemy.getHP() * 0.8))
    
class Skeleton(Undead):

    def __init__(self, name = None, hp = None):
        super().__init__(name, hp)
        super().setHP(multiplier = 0.8)
        
    def isDead(self, dead = None):
        if dead == None and super().getHP() <= 0: 
            dead = True
        return super().isDead(dead)
        
    def getDamage(self):
        return super().getHP() * 0.70
        
        
class Ghost(Undead):
    
    def __init__(self, name = None, hp = None):
        super().__init__(name, hp)
        super().setHP(multiplier = 0.5)
        super().appendAbility("Haunt")
        
    def setHP(self, hp=None, multiplier=None):
        if hp < super().getHP():
            hp = super().getHP() - ((super().getHP() - hp) * 0.1)
        super().setHP(hp, multiplier)
        
    def isDead(self, dead = None):
        if dead == None and super().getHP() <= 0: 
            dead = True
        return super().isDead(dead)
        
    def getDamage(self):
        return super().getHP() * 0.2 
        
    def Haunt(self, enemy):
        if not self.isDead():
            super().setHP(super().getHP() + (enemy.getHP() * 0.1))
        else:
            print(f'{self.getName()} is weakned therefore it cannot attack.')
        
class Lich(Undead):
    
    def __init__(self, name = None, hp = None):
        super().__init__(name, hp)
        super().appendAbility("Spellvamp")
        
    def isDead(self, dead=None):
        if dead != None: 
            dead = False
        return super().isDead(dead)
        
    def getDamage(self):
        return super().getHP() * 0.7
                
    def SpellVamp(self, enemy):
        hp = enemy.getHP() * 0.1
        dmg_toEnemy = enemy.getHP()
        enemy.setHP(enemy.getHP() - hp)
        dmg_toEnemy -= enemy.getHP()
        self.setHP(self.getHP() + dmg_toEnemy)
        
class Mummy(Undead):
    
    def __init__(self, name = None, hp = None):
        super().__init__(name, hp)
        super().appendAbility("Revive")
        
    def isDead(self, dead = None):
        if dead == None and super().getHP() <= 0:
            dead = True
        return super().isDead(dead)
        
    def Attack(self, enemy):
        if self.__class__ != enemy.__class__:
            if not super().isDead():
                enemy.setHP(enemy.getHP() - self.getDamage(enemy))
                if enemy.getHP() < 0:
                    enemy.setHP(0)
            else:
                print(f"{self.getName()} is weakened therefore it cannot attack.")

    def getDamage(self, enemy):
        return (super().getHP() * 0.5) + (enemy.getHP() * 0.1)
    
    def Revive(self):
        """A method for setting hp to its initial values when hp is at 0. Only available for Mummy class
        """
        if super().isDead():
            super().setHP(hp = self.getInitHP())
            super().isDead(False)
        else:
            print(f"{self.__name} is not dead, it cannot revive.")