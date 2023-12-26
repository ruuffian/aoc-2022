from utils import *


def diff_2(lst: list[str]) -> list[bool]:
    out = []
    for i in range(1, len(lst)):
        out.append(int(lst[i]) - int(lst[i-1]) > 0)
    return out


def window_3(lst: list[str]) -> list[bool]:
    out = []
    i = 0
    while i < len(lst) - len(lst) % 3:
        winA = [int(x) for x in lst[i:i+3]]
        winB = [int(x) for x in lst[i+1:i+4]]
        out.append(sum(winB) - sum(winA) > 0)
        i += 1
    return out


def main() -> None:
    # Read input
    depths = read_in("day1").split("\n")
    # Part 1
    increases = sum(diff_2(depths))
    print(increases)
    # Part 2
    increases_window = sum(window_3(depths))
    print(increases_window)


if __name__ == "__main__":
    main()

