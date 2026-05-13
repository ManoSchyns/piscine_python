import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    args: list[str] = sys.argv
    len: int = len(args)
    i: int = 1

    print("Program name: " + args[0])
    if (len == 1):
        print("No arguments provided!")
    else:
        print("Arguments received:", len-1)
        while (i < len):
            print("Argument ", i, ": " + args[i], sep="")
            i += 1
    print("Total arguments:", len)
