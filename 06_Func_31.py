def read_date():
    mname = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    date1 = input().split()
    d1 = int(date1[0])
    m1 = mname.index(date1[1][:3]) + 1
    y1 = int(date1[2])
    return [d1, m1, y1]

def zodiac(d, m):
    if d >= 22 and m == 3 or d <= 21 and m == 4:
        z = "Aries"
    elif d >= 22 and m == 4 or d <= 21 and m == 5:
        z = "Taurus"
    elif d >= 22 and m == 5 or d <= 21 and m == 6:
        z = "Gemini"
    elif d >= 22 and m == 6 or d <= 21 and m == 7:
        z = "Cancer"
    elif d >= 22 and m == 7 or d <= 21 and m == 8:
        z = "Leo"
    elif d >= 22 and m == 8 or d <= 21 and m == 9:
        z = "Virgo"
    elif d >= 22 and m == 9 or d <= 21 and m == 10:
        z = "Libra"
    elif d >= 22 and m == 10 or d <= 21 and m == 11:
        z = "Scorpio"
    elif d >= 22 and m == 11 or d <= 21 and m == 12:
        z = "Sagittarius"
    elif d >= 22 and m == 12 or d <= 20 and m == 1:
        z = "Capricorn"
    elif d >= 21 and m == 1 or d <= 20 and m == 2:
        z = "Aquarius"
    elif d >= 21 and m == 2 or d <= 21 and m == 3:
        z = "Pisces"
    return z

def days_in_feb(y):
    days = 28
    if y % 400 == 0 or y % 100 != 0 and y % 4 == 0:
        days = 29
    return days

def days_in_month(m, y):
    days = 31
    if m == 4 or m == 6 or m == 9 or m == 11:
        days = 30
    elif m == 2:
        days = days_in_feb(y)
    return days

def days_in_between(d1, m1, y1, d2, m2, y2):
    days = 0
    if m1 < 12:
        days += 31
    if m1 < 11:
        days += 30
    if m1 < 10:
        days += 31
    if m1 < 9:
        days += 30
    if m1 < 8:
        days += 31
    if m1 < 7:
        days += 31
    if m1 < 6:
        days += 30
    if m1 < 5:
        days += 31
    if m1 < 4:
        days += 30
    if m1 < 3:
        days += 31
    if m1 < 2:
        days += days_in_feb(y1)
    if m2 > 1:
        days += 31
    if m2 > 2:
        days += days_in_feb(y2)
    if m2 > 3:
        days += 31
    if m2 > 4:
        days += 30
    if m2 > 5:
        days += 31
    if m2 > 6:
        days += 30
    if m2 > 7:
        days += 31
    if m2 > 8:
        days += 31
    if m2 > 9:
        days += 30
    if m2 > 10:
        days += 31
    if m2 > 11:
        days += 30
    days += (days_in_month(m1, y1) - d1 + 1) + \
        int((y2 - y1 - 1)*365.25) + (d2 - 1)
    return days

def main():
    d1, m1, y1 = read_date()
    d2, m2, y2 = read_date()
    z1 = zodiac(d1, m1)
    z2 = zodiac(d2, m2)
    days = days_in_between(d1, m1, y1, d2, m2, y2)
    print(z1, z2)
    print(days)

exec(input().strip())