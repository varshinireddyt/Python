import calendar
def ada(year):

    cal = calendar.monthcalendar(year, 10)
    first_week = cal[0]
    second_week = cal[1]
    third_week = cal[2]

    if first_week[calendar.TUESDAY]:
        loveLaceDay = second_week[calendar.TUESDAY]
        return loveLaceDay

    else :
        loveLaceDay = third_week[calendar.TUESDAY]
        return loveLaceDay

print(ada(1943))

