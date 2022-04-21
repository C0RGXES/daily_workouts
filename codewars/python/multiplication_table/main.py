

def multiplication_table(size):
    x_arr = []
    for x in range(0, size, 1):
        y_arr = []
        for y in range(1, size + 1, 1):
            y_arr.append(y)
        x_arr.append(y_arr)
    return print(x_arr)


def main():
    size = 3
    multiplication_table(size)


if __name__ == "__main__":
    main()











