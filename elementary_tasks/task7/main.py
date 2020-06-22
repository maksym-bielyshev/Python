class NumericalSequence:
    def __init__(self, length_sequence, min_number):
        self.length_sequence = length_sequence
        self.min_number = min_number
        self.sequence = list()
        for i in range(1, self.length_sequence + 1, 1):
            if i ** 2 >= self.min_number:
                self.sequence.append(i)

    def __str__(self):
        return str(self.sequence)


if __name__ == '__main__':
    sequence = NumericalSequence(15, 16)
    print(sequence)
