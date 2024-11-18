def letter_occurrence(input_string):
    # complete function implementation...
    count = 0
    for char in input_string:
        if char.lower() == 'a':
            count += 1
    return count
print(letter_occurrence("Amazing"))
print(letter_occurrence("Always aim ambitiously"))