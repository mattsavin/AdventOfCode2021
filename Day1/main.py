def get_depths():
    with open("resources/input.txt", "r") as file:
        return list(map(int, file.read().split("\n")))


def part_one():
    depths = get_depths()
    count = 0

    for i, depth in enumerate(depths):
        if depth > depths[i-1]:
            count += 1

    print("Part 1:", count)


def part_two():
    depths = get_depths()

    for i, depth in enumerate(depths):
        if 1 < i < 10:
            sum_depths = depth + depths[i-1] + depths[i-2]
            print(sum_depths)


if __name__ == "__main__":
    part_one()
    part_two()
