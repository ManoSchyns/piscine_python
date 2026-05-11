def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if(unit != "packets" and unit != "grams" and unit != "area"):
        print("Unknown unit type")
        return
    elif(unit == "packets" or unit == "grams"):
        print(seed_type.capitalize() + " seeds: ", quantity, unit + " ",
              end="")
        if(unit == "packets"):
            print("available")
        elif(unit == "grams"):
            print("total")
    elif(unit == "area"):
        print(seed_type.capitalize() + " seeds:  covers", quantity,
              "square meters", end="")
