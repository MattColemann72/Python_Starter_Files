#whatever the user types here will create the times tables.
#eg - if 5, will print out 1-5 times tables up to 5 times x
user_input = input("Enter number of times tables: ")

#function prints out all times tables E.G. - 1*1,1*2,1*3,1*4,1*5 - 2*1,2*2,2*3,2*4,2*5 - etc.. up to 5*5
def TimesTables(num):
    i = 1
    x = 1
    answer = 0

    while i <= int(num):
        while x <= int(num):
            answer = i * x
            print(answer)
            x = x + 1
        input("")
        x = 1
        i = i + 1
        
TimesTables(user_input)