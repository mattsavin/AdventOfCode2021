def get_depths():
    with open("resources/input.txt", "r") as file:
        return file.read().split("\n")


def part_one():
    depths = get_depths()
    count = 1

    for i, depth in enumerate(depths):
        if depth > depths[i-1]:
            count += 1

    print(count)


def part_two():
    depths = get_depths()


if __name__ == "__main__":
    part_one()
    part_two()
