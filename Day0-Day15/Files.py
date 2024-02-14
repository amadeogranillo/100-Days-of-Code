"""input1 = input('Please enter your file name')
file = open(input1)
sum = 0
counter = 0

for lines in file:
    if lines.startswith("X-DSPAM-Confidence:"):
        colon = lines.find(':')
        piece = lines[colon + 1:].strip()
        value = float(piece)
        sum = sum + value
        counter = counter + 1
print('Average spam confidence:', sum/counter)

"""