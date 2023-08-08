def date_trimmer(date_string):
    """
    Friday, August 04, 2023 03:49:39
    """
    splits= date_string.split(' ')
    number = splits[3]+'-'

    if splits[1] == 'January':
        number = number + '01'
    elif splits[1] == 'February':
        number = number + '02'
    elif splits[1] == 'March':
        number = number + '03'
    elif splits[1] == 'April':
        number = number + '04'
    elif splits[1] == 'May':
        number = number + '05'
    elif splits[1] == 'June':
        number = number + '06'
    elif splits[1] == 'July':
        number = number + '07'
    elif splits[1] == 'August':
        number = number + '08'
    elif splits[1] == 'September':
        number = number + '09'
    elif splits[1] == 'October':
        number = number + '10'
    elif splits[1] == 'November':
        number = number + '11'
    else:
        number = number + '12'

    number = number + '-' + splits[2].rstrip(',')
    return number 
    