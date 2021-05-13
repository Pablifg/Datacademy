import math

def type_triangle(beta, alpha):
    base_location = str(input("""
    Is the height in the middle of the basis?
    y) Yes
    n) No
    """)).lower().strip()
    
    if(base_location == 'y'):

        if(beta == 60 and alpha == 60):
            print("It is an equilateral triangle")
        elif(beta == alpha):
            print("It is an isosceles triangle")
    else:
        print("It is an scalene triangle")


def area_triangle(base, height):
    area = base * height / 2
    
    beta = round( math.atan( height / (base / 2) ), 2 ) 
    alpha = round( math.atan( height / (base / 2) ), 2 ) 

    type_triangle(beta, alpha)


    print(f"The area is: {area} \n")


def menu(options):
    if(options == 'y'):
        return True
    elif(options == 'n'):
        print("Thanks for use my program")
        return False
    else:
        print("Error: BYE")

def main():

    is_finished = True
   
    while is_finished:

        while True:
            try:
                base = float(input("Input the triangule's base \n"))
                height = float(input("Input the triangule's height\n"))
                break
            except ValueError: 
                print("ValueError: Please, just numbers")
                continue

        area_triangle(base, height)

        print("=" * 50)
        options = str(input("""Do you want to calculate another triangle's area?
        y) Yes
        n) No\n""")).lower().strip()

        is_finished = menu(options)


if __name__ == '__main__':
    main()
