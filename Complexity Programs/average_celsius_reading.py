"""
To determine the temperature of a city, 
we take temperature readings from across many thermometers across the city, and
we calculate the mean average of those temperatures.

We’d also like to display the temperatures in both Fahrenheit and Celsius,
but our readings are initially only provided to us in Fahrenheit.

"""
#Solution  1


def average_celsius_reading_1(fahrenheit_reading):
    # Collect Celsius numbers here:
    celsius_numbers = []

    for reading in fahrenheit_reading:
        celsius_numbers.append((reading-32)/1.8)   # n steps

    return sum(celsius_numbers) / len(celsius_numbers)  # 2n o(n)










def average_celsius_reading_2(fahrenheit_reading):
    # Collect Celsius numbers here:
    celsius_numbers = 0

    for reading in fahrenheit_reading:
        celsius_numbers += (reading-32)/1.8


    return celsius_numbers / len(fahrenheit_reading)

fahrenheit_reading = [102.07, 104.09, 106.04, 109.6, 99.35, 102.73, 101.41, 108.69, 102.09, 108.64]
print(average_celsius_reading_1(fahrenheit_reading))
#print(average_celsius_reading_2(fahrenheit_reading))



