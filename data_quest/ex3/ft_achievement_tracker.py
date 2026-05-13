import random


class Player:

    def __init__(self, name: str, achivement_list: list[str]):
        self._name = name
        self._achivements = gen_player_achievements(achivement_list)
    
    def get_name(self):
        return self._name
    
    def get_achivement(self):
        return self._achivements
    
    def show(self):
        print("Player " + self.get_name() + ":", self.get_achivement())


"""
Genere 2 nombres random. 
les 2 nombres sont compris entre 0 et len list
si le 2 eme est plus grand que le premier -> aucun achivement
return un set compris entre lst[nb1:nb2] 
"""
def gen_player_achievements(achivements: list[str]):
    lenght: int = len(achivements)
    n1: int
    n2: int
    n1 = random.randint(0, lenght - 1)
    n2 = random.randint(0, lenght - 1)

    if (n1 > n2):
        return set()
    return(set(achivements[n1:n2]))

if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    achivements: list[str] = ["Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer"]
    
    #Les joueurs
    alice: Player = Player("Alice", achivements)
    charlie: Player = Player("Charlie", achivements)
    robert: Player = Player("Robert", achivements)
    jean: Player = Player("Jean", achivements)

    #Affichage de leurs achivement
    alice.show()
    charlie.show()
    robert.show()
    jean.show()

