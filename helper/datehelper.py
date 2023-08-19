from datetime import datetime, timedelta


def date_trimmer(date_utc):
    """
    Friday, August 04, 2023 03:49:39
    """
    date_string = datetime.fromtimestamp(date_utc).strftime("%A, %B %d, %Y %H:%M:%S")

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
    

def sort_and_pad_dates(dates):
    sorted_dates = sorted(dates, key=lambda date: tuple(map(int, date.split('-'))))
    start_date = datetime.strptime(sorted_dates[0], '%Y-%m-%d')
    end_date = datetime.strptime(sorted_dates[-1], '%Y-%m-%d')

    padded_dates = []
    current_date = start_date

    while current_date <= end_date:
        padded_dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)

    return padded_dates