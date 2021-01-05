# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is a circle area program

import math
pi = math.pi


def surface_area(radius, hight):
    # this function calculates the surface area of the cylinder

    # process
    surface_area = (2*pi*radius**2)+(2*pi*radius*hight)

    # output
    print("")
    print("the surface area is {0}.". format(surface_area))


def volume(radius, hight):
    # this function calculates the volume of the cylinder

    # process
    volume = pi*radius**2*hight

    # output
    print("the volume of the cylinder {0}.".format(volume))


def perimeter(radius):
    # this function calculates the perimeter of the cylinder

    # process
    perimeter = 2*pi*radius

    # output
    print("the perimeter of the cylinder {0}.".format(perimeter))


def main():
    # input
    while True:
        user_radius_str = input("Enter the radius: ")
        user_hight_str = input("Enter the hight: ")

        try:
            user_radius_str = int(user_radius_str)
            user_hight_str = int(user_hight_str)

            # calling functions
            surface_area(user_radius_str, user_hight_str)
            volume(user_radius_str, user_hight_str)
            perimeter(user_radius_str)
            break
        except:
            print("that is invalid input")
            print("try again")


if __name__ == "__main__":
    main()
