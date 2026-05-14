import random


"""
Classe du joueur.
Chaque joueur possede une liste d achivement random en fonction
de la liste de base
ainsi qu un nom
"""


class Player:

    def __init__(self, name: str, achivement_list: list[str]):
        self._name = name
        self._achivements = gen_player_achievements(achivement_list)

    def get_name(self) -> str:
        return self._name

    def get_achivement(self) -> set[str]:
        return self._achivements

    def show(self) -> None:
        print("Player " + self.get_name() + ":", self.get_achivement())


"""
Genere 2 nombres random.
les 2 nombres sont compris entre 0 et len list
return un set compris entre lst[nb1:nb2]
"""


def gen_player_achievements(achivements: list[str]) -> set[str]:
    lenght: int = len(achivements)
    n1: int
    n2: int
    n1 = random.randint(0, lenght - 2)
    n2 = random.randint(n1 + 1, lenght - 1)

    if (n1 > n2):
        return set()
    return (set(achivements[n1:n2]))


# Retourne les achivement present entre tout les joueurs.
# La liste unique des achivements totaux
def get_common_uniq_achiv(players: list[Player]) -> set[str]:
    all: set[str] = set()
    for player in players:
        all = all.union(player.get_achivement().difference(all))
    return (all)


# Return la liste des achivements que tout les joueurs ont obtenu
def get_commun_all_player(player: list[Player], set_achivement):
    all: set[str] = set_achivement
    name: Player
    for name in players:
        all = name.get_achivement().intersection(all,
                                                 name.get_achivement())
    return all


# Affiche joueur apres joueurs, leurs achivement que seul eux possedent
def print_user_achivement(players) -> None:
    for player in players:
        all = player.get_achivement()
        for other in players:
            if (other.get_name() != player.get_name()):
                all = all.difference(other.get_achivement())
        print("Only " + player.get_name() + " has:", all)


# affiche les achivements manquant aux joueurs pour tous les avoir
def print_user_missing_achivement(players, achivements) -> None:
    for player in players:
        print(player.get_name() + " is missing:",
              set(achivements).intersection(player.get_achivement()))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    achivements: list[str] = ["Crafting Genius", "World Savior",
                              "Master Explorer", "Collector Supreme",
                              "Untouchable", "Boss Slayer",
                              "Demon", "Ingeniorrr",
                              "Senior", "Debilous",
                              "Explosed", "The rat",
                              "Useless boy", "Useless Girl",
                              "JPP", "Yeahh",
                              "Boooommm", "Easter Egg",
                              "Lol", "Defeat",
                              "Winner", "Better",
                              "Loser", "You can't",
                              "The end", "Black hole",
                              "Nothing", "Blbla",
                              "Next", "Original",
                              "Crap", "Fish",
                              "None", "Pat",
                              "Batman", "Spiderman",
                              "Wonder", "Nails",
                              "Mini", "Maxi",
                              "Diamond", "Bronze",
                              "Gold", "loserrr"]

    # Les joueurs
    alice: Player = Player("Alice", achivements)
    charlie: Player = Player("Charlie", achivements)
    robert: Player = Player("Robert", achivements)
    jean: Player = Player("Jean", achivements)

    # Affichage de leurs achivement
    alice.show()
    charlie.show()
    robert.show()
    jean.show()

    # recuperation des achivement present chez les player
    players: list[Player] = [alice, charlie, robert, jean]
    set_achivement = get_common_uniq_achiv(players)
    print("\nAll distinct achievements:", set_achivement)

    # recuperation des Common achievements
    common: set[str] = get_commun_all_player(players, set_achivement)
    print("\nCommon achievements:", common)

    # achivement unique par utilisateur
    print()
    print_user_achivement(players)

    # Achivement manquant pour tous les avoir
    print()
    print_user_missing_achivement(players, achivements)
