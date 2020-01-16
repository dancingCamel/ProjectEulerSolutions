
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

number_of_letters = {"0": 0,
            "1": len('one'),
           "2": len('two'),
           "3": len('three'),
           "4": len('four'),
           "5": len('five'),
           "6": len('six'),
           "7": len('seven'),
           "8": len('eight'),
           "9": len('nine'),
            "10": len('ten'),
            "11": len('eleven'),
             "12": len('twelve'),
             "13": len('thirteen'),
             "14": len('fourteen'),
             "15": len('fifteen'),
             "16": len('sixteen'),
             "17": len('seventeen'),
             "18": len('eighteen'),
             "19": len('nineteen')}

number_of_letters_tens = {"0": 0,
                            "2": len('twenty'),
                          "3": len('thirty'),
                          "4": len('forty'),
                          "5":len('fifty'),
                          "6":len('sixty'),
                          "7": len('seventy'),
                          "8": len('eighty'),
                          "9": len('ninety')}

number_of_letters_others = {
           "and": len("and"),
         "100": len('hundred'),
            "1000": len('thousand')}

total_letters = 0


for num in range(1, 1001):
    string = str(num)
    if num%1000 == 0:
        total_letters += number_of_letters['1']
        total_letters += number_of_letters_others['1000']
        continue

    if num%100 == 0:
        total_letters += number_of_letters[string[0]] + number_of_letters_others['100']
        continue

    if len(string) == 1:
        total_letters += number_of_letters[string]
        continue

    if num in range(10, 20):
        total_letters += number_of_letters[string]
        continue

    if len(string) == 2 and num > 19:
        total_letters += number_of_letters_tens[string[0]]
        total_letters += number_of_letters[string[1]]
        continue
    if len(string) == 3 and string[1] != '1':
        total_letters += number_of_letters[string[0]] + number_of_letters_others['100'] + number_of_letters_others['and'] + number_of_letters_tens[string[1]] + number_of_letters[string[2]]
        continue
    if len(string) == 3 and string[1] == '1':
        last_two_digits = string[1] + string[2]
        total_letters += number_of_letters[string[0]] + number_of_letters_others['100'] + number_of_letters_others['and'] + number_of_letters[last_two_digits]



print(total_letters)
