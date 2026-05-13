import math


def get_player_pos() -> tuple:
    flag: bool = False
    coord: tuple
    arg: str
    lenght: int = 0
    while (not flag):
        try:
            lenght = 0
            arg = input("Enter new coordinates as floats in format ’x,y,z’: ")
            splited = arg.split(",")
            for elem in splited:
                lenght += 1
            if lenght < 3 or lenght > 3:
                raise Exception("Invalid syntax")
            for elem in splited:
                float(elem)
            coord = (float(splited[0]), float(splited[1]), float(splited[2]))
            flag = True
        except ValueError as e:
            print("Error on parameter '", elem, "': ", e, sep="")
        except Exception:
            print("Invalid syntax")
    return coord


def get_euclidian_dist(point1: tuple, point2: tuple):
    value1 = point2[0] - point1[0]
    value2 = point2[1] - point1[1]
    value3 = point2[2] - point1[2]
    return (math.sqrt(value1 * value1 + value2 * value2 + value3 * value3))


if __name__ == "__main__":
    coord: tuple
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    coord1 = get_player_pos()
    print("Got a first tuple:", coord1)
    print("It includes: X=", coord1[0], ", Y=", coord1[1],
          ", Z=", coord1[2], sep="")
    print("Distance to center: ",
          round(get_euclidian_dist((0, 0, 0), coord1), 4))
    print("\nGet a second set of coordinates")
    coord2 = get_player_pos()
    print("Distance between the 2 sets of coordinates:",
          round(get_euclidian_dist(coord1, coord2), 4))
