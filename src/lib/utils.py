
def count(start=1, step=1):
    '''
    This function is to always yield the next count for generating Ticket numbers and Receipt numbers
    '''
    n = start
    while True:
        yield n
        n += step