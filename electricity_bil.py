def electricity_bill(units):

    try:
        units = int(units)
    except ValueError:
        raise ValueError('Units must be numeric.')
    

    if units <= 0:
        raise ValueError('Please enter valid units.')
    
    if 0 < units <= 100:
        unit_rate = 5
    elif 100 < units <= 300:
        unit_rate = 7
    else:
        unit_rate = 10

    total = units * unit_rate

    return f'Total units {units} unit rate is ₹{unit_rate}, electricity bill is ₹{total}.'

    

try:
    units = input('Enter units: ').strip()
    result = electricity_bill(units)
    print(result)

except ValueError as e:
    print(e)