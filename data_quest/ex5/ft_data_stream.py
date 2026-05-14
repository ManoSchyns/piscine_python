import random
import typing


# choisi de maniere random
# 1 nom et une action
# la retourne sous la forme de tuple
def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players: list[str] = [
        "Alice", "Bob", "Charlie", "David", "Emma", "Fiona",
        "George", "Hannah", "Isaac", "Julia",
        "Kevin", "Laura", "Michael", "Nina", "Oscar", "Paul",
        "Quentin", "Rachel", "Simon", "Tina",
        "Ulysse", "Victoria", "William", "Xavier", "Yasmine",
        "Zoe", "Aaron", "Bella", "Chris", "Diana",
        "Ethan", "Freya", "Gavin", "Hugo", "Iris", "Jack",
        "Kara", "Liam", "Maya", "Noah",
        "Olivia", "Peter", "Queenie", "Ryan", "Sophie",
        "Thomas", "Uma", "Vince", "Wendy", "Xena",
        "Yanis", "Zara", "Arthur", "Bruno", "Celine", "Damien",
        "Elodie", "Fabien", "Gisele", "Helena",
        "Igor", "Jade", "Karl", "Lena", "Mathis", "Nicolas",
        "Olivier", "Pia", "Quentin2", "Romain",
        "Sarah", "Theo", "Ugo", "Valentin", "Wassim", "Xander",
        "Yohan", "Zoey", "Adrien", "Bastien",
        "Clara", "Dorian", "Estelle", "Florian", "Gael",
        "Hugo2", "Ines", "Julien", "Kevin2", "Lucie",
        "Manon", "Nathan", "Oceane", "Pierre", "Quentin3",
        "Rayan", "Sasha", "Tom", "Youssef", "Zinedine"
    ]
    actions: list[str] = [
        "attack", "defend", "heal", "run", "jump", "cast_spell",
        "dodge", "block", "charge", "retreat",
        "steal", "loot", "explore", "hide", "sneak", "parry",
        "counter", "slash", "shoot", "aim",
        "reload", "reload_weapon", "summon", "teleport",
        "charge_attack", "heavy_attack", "light_attack",
        "critical_hit", "miss", "stun", "freeze", "burn",
        "poison", "shock", "buff", "debuff", "heal_self",
        "heal_team", "revive", "escape", "ambush", "guard",
        "patrol", "rest", "wait", "observe", "scan", "track",
        "follow", "chase", "throw", "catch", "push", "pull",
        "lift", "break", "repair", "build", "craft", "upgrade",
        "equip", "unequip", "trade", "buy", "sell", "inspect",
        "analyze", "discover", "unlock", "open_chest", "close_door",
        "open_door", "activate", "deactivate", "trigger_trap",
        "disarm_trap", "enter_area", "exit_area", "climb", "swim",
        "fly", "glide", "dash", "slide", "roll", "dive", "sprint",
        "walk", "crawl", "meditate", "pray", "enchant", "curse",
        "bless", "transform", "duplicate", "combine", "split", "consume",
        "absorb"
    ]
    while (True):
        yield(random.choice(players), random.choice(actions))


# remove 1 tuple random de la liste lorsque le generateur
# est appelé
def consume_event(list_event: list[tuple[str, str]]):
    to_remove: tuple[str, str]
    while(list_event):
        to_remove = random.choice(list_event)
        list_event.remove(to_remove)
        yield to_remove


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    gen: typing.Generator[tuple[str, str], None, None] = gen_event()
    i: int = 0
    end: int = 1000
    event: tuple[str, str]
    list_event: list[tuple[str, str]] = []
    to_remove: tuple[str, str]

    # genere les 1000 events
    while (i < end):
        event = next(gen)
        print("Event ", i, ": " + "Player " + event[0] +
              " did action " + event[1], sep="")
        i += 1

    # creer une liste de 10 events
    i = 0
    end = 10
    while (i < end):
        list_event.append(next(gen))
        i += 1
    print("Built list of 10 events:", list_event)
    # remove 1 a un de maniere random les elements de la liste
    remove_event = consume_event(list_event)
    for to_remove in remove_event:
        print("Got event from list:", to_remove)
        print("Remains in list:", list_event)
