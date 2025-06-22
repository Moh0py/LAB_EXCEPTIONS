def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    user_input = input('Enter temperature and unit (e.g. "25 C" or "77 F"): ')
    parts = user_input.split()

    if len(parts) != 2:
        print("Invalid input format. Please enter like: 25 C or 77 F")
        continue

    temp_str, unit = parts

    try:
        temp = float(temp_str)
        unit = unit.upper()
        if unit == 'C':
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C is {result:.2f}°F")
        elif unit == 'F':
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F is {result:.2f}°C")
        else:
            raise TypeError("Invalid unit")
    except ValueError:
        print("Invalid temperature value. Please enter a number.")
        continue
    except TypeError:
        print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        continue

    again = input("Do you want to convert another temperature? (y/n): ").lower()
    if again != 'y':
        print("Goodbye!")
        break
