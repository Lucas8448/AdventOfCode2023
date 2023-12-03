def find_first_and_last_digit(s):
    first_digit = None
    last_digit = None

    for char in s:
        if char.isdigit():
            last_digit = char
            if first_digit is None:
                first_digit = char

    return first_digit, last_digit

with open('input.txt', 'r') as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        line = line.strip()
        first_digit, last_digit = find_first_and_last_digit(line)

        if first_digit is not None and last_digit is not None:
            calibration_value = int(first_digit) * 10 + int(last_digit)
            sum += calibration_value

    print(sum)