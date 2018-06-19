# A function that accepts 2 single digit integers as parameters and
# returns the sum of a sequence.

def pattern_sum(a, b):
    output = 0
    sequenced_a = a
    while b > 0:
        output += sequenced_a
        sequenced_a = int(str(sequenced_a) + str(a))
        b -= 1
    return output
