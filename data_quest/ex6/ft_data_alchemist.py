import random


if __name__ == "__main__":
    players_to_upper: list[str]
    players_upper_only: list[str]
    players: list[str] = ["Alice", "bob", "Charlie", "dylan", "Emma",
                          "Gregory", "john", "kevin", "Liam"]
    players_to_upper = [player.capitalize() for player in players]
    players_upper_only = [player for player in players
                          if player[0] >= 'A' and player[0] <= 'Z']

    first_dic: dict[str, int] = {}
    second_dic: dict[str, int] = {}
    total: float = 0.0
    size: float = 0.0

    average: float = 0.0

    print("Initial list of players:", players)
    print("New list with all names capitalized:", players_to_upper)
    print("New list of capitalized names only", players_upper_only)

    print()
    first_dic.update({key: random.randint(0, 1000)
                      for key in players_to_upper})
    print("Score dict:", first_dic)

    total = sum(first_dic.values())
    size = len(first_dic.values())
    average = round((total / size), 2)
    print("Score average is", average)
    second_dic.update({key: value for key, value in first_dic.items()
                       if value > average})
    print("High scores:", second_dic)
