from utils import *

def binary_to_dec(b_digits: list[int]) -> int:
    num = 0
    i = len(b_digits) - 1
    while i >= 0:
        coeff = b_digits[i]
        digit = len(b_digits) - 1 - i
        num += coeff * 2**digit
        i -= 1
    return num

def invert(code: list[int]) -> list[int]:
    return [(x + 1) % 2 for x in code]


def _gamma_rate(report: list[str]) -> list[int]:
    # STUPID STUPID STUPID !!!!!!!!!
    return [int(sum([int(x[i]) for x in report]) > len(report) // 2) for i in range(len(report[0]))]

def gamma_rate(report: list[str]) -> list[int]:
    gamma = []
    for i in range(len(report[0])):
        column = [int(x[i]) for x in report]
        digit = sum(column) > len(report) // 2
        gamma.append(digit)
    return gamma

def main() -> None:
    diagnostic = read_in("day3").split("\n")
    c_gamma = gamma_rate(diagnostic)
    c_epsilon = invert(c_gamma)
    gamma = binary_to_dec(c_gamma)
    epsilon = binary_to_dec(c_epsilon)
    print(gamma*epsilon)



if __name__ == "__main__":
    main()