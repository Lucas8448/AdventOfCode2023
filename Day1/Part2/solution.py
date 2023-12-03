# Function to convert word to number
def word_to_number(word):
    mapping = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    return mapping.get(word, 0)

def get_first_last_numbers(s):
    words = s.split()
    first_number = last_number = None

    for word in words:
        if word.isdigit():
            number = int(word)
        else:
            number = word_to_number(word)
        
        if number != 0:
            if first_number is None:
                first_number = number
            last_number = number

    return first_number, last_number
total_sum = 0

with open('input.txt', 'r') as file:
    for line in file:
        first, last = get_first_last_numbers(line.strip())
        if first is not None and last is not None:
            total_sum += first * 10 + last

print("Total sum of calibration values:", total_sum)

# not working, but cant figure out my mistake