#Constant 1mile is equal to 1.609344 km
MILE = 1.609344

def change_between_units(unit, value):
    if(unit == 'km'):
        result = value / MILE 
        print(f"{value} km has {result} milla")
    else:
        result =  value * MILE
        print(f"{value} milla has {result} km")

def main():

    isStarted = True

    while isStarted:
        option = int(input("""
        What do you want to do?
        1) km to milla
        2) milla to km 
        3) Exit\n 
        """))
        
        

        if(option == 1):
            value = float(input("Input the value: "))
            change_between_units('km', value)
        elif(option == 2):
            value = float(input("Input the value: "))
            change_between_units('mile', value)
        elif(option == 3):
            print("Thanks to use my conversion of measurement units")
            isStarted = False
            break
        else:
            print("ERROR: Option no found")


if __name__ == '__main__':
    main()
