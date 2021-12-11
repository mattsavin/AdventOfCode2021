def get_commands():
    with open("resources/input.txt", "r") as file:
        return file.read().split("\n")


def part_one():
    commands = get_commands()

    x = 0
    y = 0

    for command in commands:
        direction = command.split(" ")[0]
        magnitude = int(command.split(" ")[1])

        match direction:
            case "forward":
                x = x + magnitude
            case "down":
                y = y + magnitude
            case "up":
                y = y - magnitude

    return x * y


if __name__ == "__main__":
    print("Part 1:", part_one())
