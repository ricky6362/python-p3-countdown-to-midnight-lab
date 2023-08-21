# your code goes here!
def countdown(number):
    while number >= 1:
        print(f'{number} SECOND(S)!')
        number -= 1
        if number == 0:
            print("HAPPY NEW YEAR!")

countdown(30)