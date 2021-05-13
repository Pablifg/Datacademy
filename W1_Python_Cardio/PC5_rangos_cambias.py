import random

def main():
    
    lower = int(input("Enter the lower number for the range: "))
    upper = int(input("Enter the upper number for the range: "))

    print("*" * 50)
    random_number = random.choice(range(lower, upper))    

    isStarted = True

    while isStarted:

        select_number = int(input("Enter a number to try guess: "))
        
        if(select_number == random_number):
            print(f"\nExcellent! The number was {random_number}")
            isStarted = False
        elif(select_number > random_number):
            print("Try to put a lower number\n")
        else:
            print("Try to put a upper number\n")


if __name__ == '__main__':
    main()
