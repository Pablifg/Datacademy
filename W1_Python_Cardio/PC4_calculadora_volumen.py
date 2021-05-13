#Thenn implement Class. It is a topic to try a lot o things. 
import math

def sphere(radious):
    return (radious ** 3) * 4 * math.pi / 3

def cube(side):
    return side** 3

def rectangular_pyramid(base, length, height):
    return base * length * height

def cylinder(height, radious):
    return math.pi * (radious ** 2) * height


def main():
    
    isStarted = True

    while isStarted:
        menu = int(input("""
        Choose the option to calculate the volume:
        1) Sphere
        2) Cube
        3) Rectangular Pyramid
        4) Cylinder
        5) Exit\n
        """))

        if(menu == 1):
            radious = float(input("Enter the radious: "))
            print(f'The volume of a sphere is {sphere(radious)}')
        elif(menu == 2):
            side = float(input("Enter the cube's side: "))
            print(f'The volume of a cube is {cube(side)}')
        elif(menu == 3):          
            base = float(input("Enter the base: "))
            length = float(input("Enter the thick: "))
            height = float(input("Enter the height: "))
            print(f'The volume of a rectangular pyramid is {rectangular_pyramid(base, length, height)}')
        elif(menu == 4):
            height = float(input("Enter the height: "))
            radious = float(input("Enter the radious: "))
            print(f'The volume of a cylinder is {cylinder(height, radious)}')
        elif(menu == 5):
            print("Thanks for use it. Bye!!")
            isStarted = False
        else:
            print("ERROR: Option no found")

if __name__ == '__main__':
    main()
