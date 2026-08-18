class GameCharacter:
    def __init__(self,name):
        self._name = name
        self.health =  100
        self.mana = 50
        self._level = 1
    
    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, new_health):
        if not isinstance(new_health, (int,float)):
            raise TypeError("Must be a number")
        if new_health < 0:
            self._health = 0    
        elif new_health > 100:
            self._health = 100
        else:    
            self._health = new_health

    @property 
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, new_mana):
        if not isinstance(new_mana, (int,float)):
            raise TypeError("Must be a number")
        if new_mana < 0:
            self._mana = 0
        elif new_mana > 50:
            self._mana = 50
        else:    
            self._mana = new_mana

    @property
    def level(self):
        return self._level
    
    def level_up(self):
        self._level = self._level + 1
        self.mana =  50
        self.health = 100
        print(f"{self.name} leveled up to {self.level}!")
    
    def __str__(self):
        return f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}"

toby = GameCharacter('Toby')
print(toby.name)
print(toby.health)
print(toby.mana)
print(toby.level)
toby.health = 90
toby.mana = 20
toby.level_up()
print(toby.level)
print(toby.mana)
print(toby.health)
print(toby)