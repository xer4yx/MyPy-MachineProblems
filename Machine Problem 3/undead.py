class Undead:
    #Initializer for the child classes
    def __init__(self, name=None, hp=None): 
        self.__initial_hp = 100
        if name != None:
            self.__name = f'{name} - {self.__class__.__name__}'
        else:
            self.__name = self.__class__.__name__

        if hp != None:
            self.__hp = hp
        else:
            self.__hp = self.__initial_hp
            self.__abilities = ["Attack"]
        self.__isDead = False
        print(f"""
          {self.__class__.__name__} has been created
        Name: {self.__name}
        HP: {self.__hp}
              """)

    def isDead(self, dead=None):
        """Method used to check of an undead (e.g. Zombie) is at 0 HP.
        
            Args:
                dead (bool): Sets to True if undead is at 0 HP and False if not. Defaults to None.

            Returns:
                self.__isDead: A boolean value based on the conditional statment
        """
        if dead != None:
            self.__isDead = dead
        elif self.getHP() <= 0:
            self.__isDead = True
        return self.__isDead

    # Getter Methods
    def getName(self):  
        return self.__name

    def getHP(self):  
        return self.__hp

    def getInitHP(self):  
        return self.__initial_hp

    def getAbility(self): 
        return self.__abilities

    # Setter Methods
    def setName(self, name):  
        self.__name = name

    def setHP(self, hp=None, multiplier=None):
        if multiplier == None:
            self.__hp = hp
        else:
            self.__hp = self.__hp * multiplier

    def appendAbility(self, ability):
        """Method for appending an ability as a string in a list.

        Args:
            ability (str): Name for a type of ability in the child class of Undead.
        """
        self.__abilities.append(ability)

    def Attack(self, enemy):
        """Method for setting a new hp for an instance.

        Args:
            enemy (Instance): Points to the instance of a class
        """
        if not self.__isDead:
            enemy.setHP(enemy.getHP() - self.getDamage())
            if enemy.getHP() < 0:
                enemy.setHP(0)
        else:
            print(f"{self.__name} is dead and cannot attack.")

    def DisplayStat(self):
        print(f"""      Name: {self.__name}
      HP: {self.getHP()}
      State: {"Dead" if self.isDead() else "Alive"}
            """)
