# Making Guess The Number
print("Guess The Number")
n = 18  #number to be guessed
g = 9  #no of guesses : 9
while 1:
    print("Total no of Guesses Available: ", g)
    g = g - 1  #decreasing g by 1
    inp = int(input("Enter a Number : "))  #Taking input from user
    if g == 0:  #number of guesses = 0
        print("Sorry You Loose ", g, " Guesses Left")
        break
    elif inp > n:  ##user value is Greater than n
        print("Go Lower than ", inp)
        continue
    elif inp < n:  #user value is Lesser than n
        print("Go Higher than ", inp)
        continue
    else:  #user value is equal to n
        print("Congrats number was ", n, "You took ", 9 - g, " guesses")
        break