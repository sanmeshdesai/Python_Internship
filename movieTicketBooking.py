def ticketBooking(tickets):

    try:
        tickets = int(tickets)
    except ValueError:
        raise ValueError('Tickets must be numeric.')

    if tickets <= 0:
        raise ValueError('Number of tickets must be at least 1.')

    if tickets > 6:
        raise ValueError('No more than 6 tickets allowed.')

    ticket_price = 250
    total = ticket_price * tickets
    return f'Total amount for {tickets} tickets is ₹{total}.'



try :
    tickets = input('Enter number of tickets ')
    result = ticketBooking(tickets)
    print(result)
    
except ValueError as e:
    print('Booking failed:', e )


