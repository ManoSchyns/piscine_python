import sys


def parsing(args: list[str]) -> dict[str, int]:
    size: int = len(args)
    i: int = 1
    splited_arg: list[str]
    data: dict[str, int] = {}
    if (size == 1):
        print("Can't work with no argunents")
        return data
    while i < size:
        splited_arg = args[i].split(":")
        if len(splited_arg) != 2:
            print("Error - invalid parameter '" + args[i] + "'")
        elif(splited_arg[0] in data):
            print("Redundant item '" + splited_arg[0] + "’ - discarding")
        else:
            try:
                data[splited_arg[0]] = int(splited_arg[1])
            except Exception as e:
                print("Quantity error for '" + splited_arg[0] + "':", e)
        i += 1
    return data


# retourn la cle du maximum du dictionnaire
def get_max_dic(data: dict[str, int]) -> str | None:
    maxi: str | None = None
    for key in data:
        if (maxi is None or data[key] > data[maxi]):
            maxi = key
    return (maxi)


# retourn la cle du minimum du dictionnaire
def get_min_dic(data: dict[str, int]) -> str | None:
    mini: str | None = None
    for key in data:
        if (mini is None or data[key] < data[mini]):
            mini = key
    return (mini)


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    args: list[str] = sys.argv
    inventory: dict[str, int] = {}
    item: list[str] = []
    len_item: int = 0
    total: int = 0
    maxi: str | None
    mini: str | None
    # inventaire
    inventory = parsing(args)
    print("Got inventory:", inventory)

    # liste des item
    item = list(inventory.keys())
    len_item = len(item)
    print("Item list:", item)

    # total des item:
    for key in item:
        total += inventory[key]
    print("Total quantity of the", len_item, "items:", total)

    # pourcentage pour chaque item
    for key in item:
        print("Item " + key + " represents ",
              round(((inventory[key] / total) * 100), 1), "%", sep="")

    # maximi - mininmum
    maxi = get_max_dic(inventory)
    mini = get_min_dic(inventory)
    if (maxi is not None and mini is not None):
        print("Item most abundant: " + maxi +
              " with quantity", inventory[maxi])
        print("Item least abundant: " + mini +
              " with quantity", inventory[mini])
    else:
        print("No item is most abundant or no item is least abundant")

    # ajout d'un item
    inventory.update({"magic_item": 1})
    print("Updated inventory:", inventory)
