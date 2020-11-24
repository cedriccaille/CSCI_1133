import math

#TODO: Fill out the Purpose, Input Parameter(s), and Return Value
# for each of the two functions below in the docstrings, and then write
# additional functions for parts B and C, and fill out the same information
# for those functions as well.

# Example function for background reading

def nickels_to_cents(nickels):
    '''
    Purpose: Converts from a certain number of nickels to
            how many cents we have

    Input Parameter(s):
        nickels: The number of nickels we have

    Return Value:
        the amount of cents we have
    '''
    total = nickels * 5
    return total

# Part A: Two functions that you should add documentation to
def fahrenheit_to_celsius(fahrenheit):
    '''
    Purpose:
        Converts temperature in fahrenheit to celsius
    Input Parameter(s):
        fahrenheit: temperature written in degrees fahrenheit
    Return Value:
        cels: temperature converted to degrees celsius
    '''
    tmp = fahrenheit - 32
    cels = tmp * 5.0 / 9.0
    return cels

def volume_sphere(radius):
    '''
    Purpose:
        To calculate the volume of a sphere from a radius
    Input Parameter(s):
        radius: length of the radius of the sphere
    Return Value:
        volume: value for the volume of the sphere
    '''
    pi = 3.14159
    rcubed = radius * radius * radius
    volume = pi * 4.0 * rcubed / 3.0
    return volume

# Part B: Write out a few simple conversions

def pounds_to_kilograms(pounds):
    #print("TODO: Document and write this function")
    '''
    Purpose:
        To convert weight in pounds to kilograms
    Input Parameter(s):
        pounds: measurement of weight in pounds
    Return Value:
        kilograms: measurement of weight in kilograms
    '''
    kilograms = pounds * 0.4535924
    return kilograms

def area_circle(radius):
    #print("TODO: Document and write this function")
    '''
    Purpose:
        To calculate the area of a circle given the radius
    Input Parameter(s):
        radius: measurement of the radius of the circle
    Return Value:
        area: calculation of the area of the circle
    '''
    pi = 3.1415926535
    rsquared = radius*radius
    area = pi * rsquared
    return area

def surface_area_sphere(radius):
    #print("TODO: Document and write this function")
    '''
    Purpose:
        To calculate the surface area of a sphere given a radius
    Input Parameter(s):
        Radius: the measured radius of the sphere
    Return Value:
        Surface_area: Calculated surface area of a sphere
    '''
    pi = 3.1415926535
    rsquared = radius*radius
    Surface_area = 4 * pi * rsquared
    return Surface_area

# Part C: Compute miles per gallon

def miles_per_gallon(start, end, gas):
    #print("TODO: Document and write this function")
    '''
    Purpose:
        To calculate the efficiency of the vehicle
    Input Parameter(s):
        Start: Initial odometer reading (miles)
        End: Final odometer reading (miles)
        Gas: amount of gas used in total (gallons)
    Return Value:
        efficiency: calculated efficiency of the vehicle using number of
        miles traveled per gallon of gas used (miles/gallon)
    '''
    miles_traveled = end - start
    efficiency = miles_traveled / gas
    return efficiency
