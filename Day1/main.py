def get_depths():
    with open("resources/input.txt", "r") as file:
        return list(map(int, file.read().split("\n")))


def part_one():
    depths: list = get_depths()
    count: int = 0

    for i, depth in enumerate(depths):
        if depth > depths[i-1]:
            count += 1

    print("Part 1:", count)


def part_two():
    depths: list = get_depths()

    old_depths: int = 5000  # This is to avoid the first sum_depths counting as higher when
    # in reality there's no depth before it.
    count: int = 0

    for i, depth in enumerate(depths):
        if 1 < i:
            sum_depths = depth + depths[i-1] + depths[i-2]
            if sum_depths > old_depths:
                count += 1
            old_depths = sum_depths

    print("Part 2:", count)


if __name__ == "__main__":
    part_one()
    part_two()
