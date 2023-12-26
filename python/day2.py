from utils import *


def pilot(instructions: list[list[str]]) -> int:
    depth = 0
    pos = 0
    for instruction in instructions:
        match instruction[0]:
            case "forward":
                pos += int(instruction[1])
            case "down":
                depth += int(instruction[1])
            case "up":
                depth -= int(instruction[1])
    return pos * depth


def pilot_aim(instructions):
    depth = 0
    pos = 0
    aim = 0
    for instruction in instructions:
        match instruction[0]:
            case "forward":
                pos += int(instruction[1])
                depth += int(instruction[1]) * aim
            case "down":
                aim += int(instruction[1])
            case "up":
                aim -= int(instruction[1])
    return pos*depth


def main():
    # Read input
    puzzle = read_in("day2")
    instructions = [command.split(" ") for command in puzzle.split("\n")]
    # Part 1
    part1 = pilot(instructions)
    print(part1)
    # Part 2
    part2 = pilot_aim(instructions)
    print(part2)


if __name__ == "__main__":
    main()