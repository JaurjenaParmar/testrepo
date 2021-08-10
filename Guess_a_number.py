n=11

total_guesses=int(input("Maximum number of guesses you can make:"))
print("The guessed number should be in range 1 to 100")
i=0
while i<total_guesses:
    num=int(input("\nEnter a guessed number:"))
    if num>n:
        print("Your guess is WRONG you entered a greater number from the actual number")
        print("Total guesses left=",total_guesses-i-1)
    elif num==n:
        print("You WON this game in total %d Guess"%(i+1))
        break
    else:
        print('Your guess is WRONG you entered a smaller number')
        print("Total guesses left=",total_guesses-i-1)
    print('\n')
    i=i+1
    
else:
    print("YOU LOST THIS GAME !!!! NO CHANCE LEFT!!")
    
