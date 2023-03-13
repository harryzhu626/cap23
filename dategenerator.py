def create_dates(yr_start, yr_end, month_start, month_end):
    if len(str(month_start)) == 1:
        month_start = '0' + str(month_start)
    if len(str(month_end)) == 1:
        month_end = '0' + str(month_end)
    date_start = f'{yr_start}-{month_start}-01'
    date_end = f'{yr_end}-{month_end}-01'
    return (date_start, date_end) 