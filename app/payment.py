from flask import Flask, request, render_template

class CreditCard:
    @staticmethod
    def isValid(number):
        return (CreditCard.getSize(number) >= 13 and CreditCard.getSize(number) <= 16) and \
               (CreditCard.prefixMatched(number, 4) or CreditCard.prefixMatched(number, 5) or \
                CreditCard.prefixMatched(number, 37) or CreditCard.prefixMatched(number, 6)) and \
               ((CreditCard.sumOfDoubleEvenPlace(number) + CreditCard.sumOfOddPlace(number)) % 10 == 0)

    @staticmethod
    def sumOfDoubleEvenPlace(number):
        total_sum = 0
        number_str = str(number)
        for i in range(len(number_str) - 2, -1, -2):
            doubled_digit = int(number_str[i]) * 2
            total_sum += doubled_digit if doubled_digit < 10 else CreditCard.getDigit(doubled_digit)
        return total_sum

    @staticmethod
    def getDigit(number):
        if number < 9:
            return number
        return (number // 10) + (number % 10)

    @staticmethod
    def sumOfOddPlace(number):
        total_sum = 0
        number_str = str(number)
        for i in range(len(number_str) - 1, -1, -2):
            total_sum += int(number_str[i])
        return total_sum

    @staticmethod
    def prefixMatched(number, d):
        return CreditCard.getPrefix(number, CreditCard.getSize(d)) == d

    @staticmethod
    def getSize(d):
        return len(str(d))

    @staticmethod
    def getPrefix(number, k):
        number_str = str(number)
        if CreditCard.getSize(number) > k:
            return int(number_str[:k])
        return number
    
    @staticmethod
    def isValidDate(expiry_date):
        try:
            month, year = map(int, expiry_date.split('/'))
            return 1 <= month <= 12 and year >= 2022  # Assuming expiry date must be in MM/YYYY format and after the current year
        except ValueError:
            return False