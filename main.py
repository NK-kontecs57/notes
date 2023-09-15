class RomanNumeral:
    def __init__(self, number):
        self._roman = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
                       'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400,
                       'D': 500, 'CM': 900, 'M': 1000}
        self.number = number

    def to_number(self, roman):
        new_num = 0
        for _ in range(len(roman)):
            if roman[0] == 'I':
                new_num -= 1
            else:
                new_num += self._roman[roman[0]]
            new_num = new_num[1:]
        return new_num
