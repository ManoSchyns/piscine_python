import sys


def analyse_datas(datas: list[str]) -> list[int]:

    list_ret: list[int] = []
    for elem in datas:
        try:
            list_ret.append(int(elem))
        except Exception:
            print("Invalid parameter: '" + elem + "'")
    return (list_ret)


def print_stats(datas: list[int]) -> None:
    maxi: int
    mini: int
    total: int
    lenght: int = len(datas)
    if lenght == 0:
        print("No scores provided. Usage: python3 " +
              "ft_score_analytics.py <score1> <score2> ...")
        return
    total = sum(datas)
    maxi = max(datas)
    mini = min(datas)

    print("Scores processed:", datas)
    print("Total players:", lenght)
    print("Total score:", total)
    print("Average score:", total / lenght)
    print("High score:", maxi)
    print("Low score:", mini)
    print("Score range:", maxi - mini)


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    args: list[str] = sys.argv
    datas: list[int] = analyse_datas(args[1:])
    print_stats(datas)
