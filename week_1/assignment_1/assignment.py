import sys

digit_string = sys.argv[1]

digits_sum = 0

for i in digit_string:
    digits_sum += int(i)

print(digits_sum)