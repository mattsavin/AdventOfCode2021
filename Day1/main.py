def main():
    with open("resources/input.txt", "r") as file:
        depths = file.read()
        depths = depths.split("\n")

        count = 1

        for i, depth in enumerate(depths):
            if depth > depths[i-1]:
                count += 1

        print(count)


if __name__ == "__main__":
    main()
