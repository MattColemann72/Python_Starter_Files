'''
ISBN's (International Standard Book Numbers) are identifiers for books.
The ISBN is a thirteen-digit code.
The last digit is a check number calculated as follows:


The first 12 digits are taken
Starting at index 0, if the index is even - add it, and if the index is odd – multiply the digit by three then add it.


From the sum find the remainder after dividing by 10.
10 minus the remainder give us the check digit

978-0-306-40615-?

In other words the following algebra would give us the check digit:
digit_12 = 10 – (( digit_0 + (3 x digit_1) + digit_2 + (3 x digit_3) + digit_4 + (3 x digit_5) + digit_6 + (3 x digit_7) + digit_8 + (3 x digit_9) + digit_10 + (3 x digit_11) ) % 10)
'''

'''
get the string
convert to array of numbers (list)
if numbers(0) is divisible by 2, add it. Else multiyply it by 3 then add it

from the sum find the remainder after dividing by 10.
10 minus the remainder gives us the check digit
'''


def ISBN13(isbnlist):
    #print(isbnlist)
    isbn13 = 0
    for i in isbnlist:
        if isbnlist[i] % 2 != 0:
            #print("E")
            i * 3
        isbn13 = isbn13 + i
        print(isbn13)

    isbn13 = isbn13 % 10
    isbn13 = 10 - isbn13
    #print(isbn13)
    return isbn13



'''input("Please enter your 12 digit ISBN number: ")'''
#1234567892345
#978030640615
isbn12 = input("Please enter your 12 digit ISBN number: ")
isbn12_list = [int(x) for x in str(isbn12)]
#print(isbn12_list)

isbn13 = ISBN13(isbn12_list)
print(isbn13)