# Asks for an input from the user as a mark.
# If the mark is greater that 85 print "distinction"
# If the mark is between 65 and 85 "pass"
# Anything else print "Fail"
# Try to do it both with and without elif statements.

userMark = int(input("Please enter your mark: "))

# if userMark > 85:
#     print("distinction")

# if userMark >= 65 and userMark <= 85:
#     print("pass")

# if userMark < 65:
#     print("fail")


if userMark > 85:
    print("distinction")
elif userMark >= 65 and userMark <= 85:
    print("pass")
else:
    print("fail")