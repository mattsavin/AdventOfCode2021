from collections import Counter


def get_diagnostics():
    with open("resources/input.txt", "r") as file:
        return file.read().split("\n")


def part_one():
    diagnostic_data: list = get_diagnostics()
    gamma = []
    epsilon = []

    # 12 digits in each binary number
    for i in range(0, 12):
        # n for n in diagnostic_data separates the list into its numbers
        # n[i] takes only the ith (from 0 to 12) digit of the number
        # Counter() finds the number of occurrences of values in this digit (the value can be either 0 or 1)
        # most_common() finds the most common of these values and returns an array of tuples, with the most common
        # value occurring first.
        # [0][0] takes the first element in the array (the most common value), then only the digit (as opposed to the
        # digit and the count). This is then appended to the array gamma.
        data = Counter(n[i] for n in diagnostic_data).most_common()[0][0]
        gamma.append(data)

    for i in range(0, 12):
        # Same as above, but with the least common value for each digit
        data = Counter(n[i] for n in diagnostic_data).most_common()[1][0]
        epsilon.append(data)

    # Converts each array into a single string, then into a base 2 integer
    gamma = int(''.join(gamma), 2)
    epsilon = int(''.join(epsilon), 2)

    return gamma * epsilon


def part_two():
    diagnostic_data = get_diagnostics()

    for i in range(0, 12):
        most_common = int(Counter(n[i] for n in diagnostic_data).most_common()[0][0])
        for number in diagnostic_data:
            if int(number[i]) != most_common:
                diagnostic_data.remove(number)

    return diagnostic_data


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())
