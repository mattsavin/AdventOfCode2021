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


def part_two():
    commands = get_commands()

    aim = 0
    x = 0
    y = 0

    for command in commands:
        direction = command.split(" ")[0]
        magnitude = int(command.split(" ")[1])

        match direction:
            case "down":
                aim += magnitude
            case "up":
                aim -= magnitude
            case "forward":
                x += magnitude
                y += aim * magnitude

    return x * y


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())
