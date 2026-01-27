def validate_recharge(mobile, amount):

        if not mobile.isdigit():
            raise ValueError('Mobile number must contain only digits.')
        
        if len(mobile) != 10:
            raise ValueError('Mobile number must be exactly 10 digits.')
        
        try:
            amount = int(amount)

        except ValueError:
            raise ValueError('Recharge amount must be numeric.')
        
        if amount < 10 :
            raise ValueError ('Recharge amount must be higher than 10')
        
        return f'Recharge successfull for {mobile} of amount ₹{amount}.'
    

try :
    mobile = input('Enter mobile number: ').strip()
    amount = input('Enter recharge amount: ').strip()
    
    result = validate_recharge(mobile, amount)
    print(result)

except ValueError as e:
    print('Recharge failed: ', e) 



