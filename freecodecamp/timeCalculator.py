def add_time(start, duration,day=None):
    res1 = start.split(' ')
    time1 = res1[0].split(':')

    time2 = duration.split(':')

    hrs_start = int(time1[0])
    mins_start = int(time1[1])

    hrs_add = int(time2[0])
    mins_add = int(time2[1])

    ap = res1[1]

    if ap == 'PM':
        hrs = (hrs_start) + 12
    else:
        hrs = hrs_start
    
    total_hrs = hrs + hrs_add
    total_mins = mins_add + mins_start

    if total_mins >= 60:
        total_mins = total_mins%60
        total_hrs += 1
    
    if total_hrs >= 24:
        days = total_hrs // 24
        total_hrs = total_hrs %24

        if total_hrs == 0:
            ap_now = 'AM'
            total_hrs = 12
        elif total_hrs > 12:
            ap_now = 'PM'
            total_hrs = total_hrs % 12 
        else:
            ap_now = 'AM'
    else:
        days = 0
        if total_hrs >= 12:
            ap_now = 'PM'
            total_hrs = total_hrs%12
            if total_hrs == 0:
                total_hrs = 12
        else:
            ap_now = 'AM'
    
    day_to_return = ""
    if days == 1:
        day_to_return = f'(next day)'
    elif days > 1:
        day_to_return = f'({days} days later)'

    week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    day_return = -1
    if day != None:
        if day.title() in week:
            ind = week.index(day.title())
            ind_latest = (ind + days)%7
            day_return = week[ind_latest]
    
    if days == 0:
        if day != None:
            res = f"{total_hrs}:{total_mins:02} {ap_now}, {day_return}"
        else:
            if day_return != -1:
                res = f"{total_hrs}:{total_mins:02} {ap_now}, {day_return} {day_to_return}"
            else:
                res = f"{total_hrs}:{total_mins:02} {ap_now}"
    else:
        if day != None:
            res = f"{total_hrs}:{total_mins:02} {ap_now}, {day_return} {day_to_return}"
        else:
            res = f"{total_hrs}:{total_mins:02} {ap_now} {day_to_return}"




    return res

print(add_time('8:16 PM', '466:02'))
