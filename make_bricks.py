def make_bricks(small, big, goal):
  #small bricks 1 inch
  #big bricks 5 inches
  #find out how may big bricks can fit 
  #top up with little bricks
  
  big_needed = min(big, goal // 5) #double // divides by and then rounds down to floor of number
  if goal - (big_needed * 5) <= small:
    return "Success!"
  else:
    return "Failed."

num1 = int(input("Enter number of small bricks: "))
num2 = int(input("Enter number of big bricks: "))
numgoal = int(input("Enter goal: "))

success = make_bricks(num1,num2,numgoal)
print(success)