if __name__ == "__main__":
    f = open("input.txt", "r")
    line = f.readline()
    sum = 0

    while line != "":
        linelen = len(line) - 1
        digits = []
        for i in range(linelen):
            char = line[i]
            if char.isdigit():
                digits.append(char)
        if len(digits) > 0:
            first = digits[0]
            last = digits[-1]
            value = int(first + last)
            sum += value
        line = f.readline()
    print(sum)
