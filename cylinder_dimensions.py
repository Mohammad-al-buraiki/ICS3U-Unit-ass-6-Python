# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is a circle area program

import math


def surface_area(radius, height):
    # this function calculates the surface area of the cylinder

    # process
    surface_area = (2*math.pi*radius**2)+(2*math.pi*radius*height)

    return surface_area


def volume(radius, height):
    # this function calculates the volume of the cylinder

    # process
    volume = math.pi*radius**2*height

    return volume


def perimeter(radius):
    # this function calculates the perimeter of the cylinder

    # process
    perimeter = 2*math.pi*radius

    return perimeter


def main():
    # input
    while True:
        user_radius_str = input("Enter the radius (mm): ")
        user_height_str = input("Enter the height (mm): ")

        try:
            user_radius_int = int(user_radius_str)
            user_height_int = int(user_height_str)

            # calling functions
            surface_area_calculated = surface_area(user_radius_int,
                                                   user_height_int)
            volume_calculated = volume(user_radius_int,
                                       user_height_int)
            perimeter_calculated = perimeter(user_radius_int)
            print("the surface area is {0:.2f}mm².".
                  format(surface_area_calculated))
            print("the volume of the cylinder {0:.2f}mm³.".
                  format(volume_calculated))
            print("the perimeter of the cylinder {0:.2f}mm.".
                  format(perimeter_calculated))

            break
        except Exception:
            print("that is invalid input")
            print("try again")


if __name__ == "__main__":
    main()
