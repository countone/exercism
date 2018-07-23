def on_square(integer_number):
    if integer_number<1 or integer_number>64:
    	raise ValueError('ValueError')

    return 2**(integer_number-1)


def total_after(integer_number):
    if integer_number<1 or integer_number>64:
    	raise ValueError('ValueError')
    return on_square(integer_number)+total_after(integer_number-1)
