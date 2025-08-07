import datetime

current_date = datetime.date.today()

print('current_date', current_date)
birthday = datetime.date(1995, 1, 28)

# age = current_date.year - birthday.year - ((current_date.month, current_date.day) < (birthday.month, birthday.day))
age = current_date.year - birthday.year

isBeforeBirthday = (current_date.month, current_date.day) < (birthday.month, birthday.day)

print('isAfterBirthday: ', isBeforeBirthday)

if isBeforeBirthday:
    age -= 1

print('age: ', age)

nextBirthdayYear = current_date.year if isBeforeBirthday else current_date.year + 1
nextBirthday = datetime.date(nextBirthdayYear, birthday.month, birthday.day)

# 计算下次生日还有几天
days_until_next_birthday = (nextBirthday - current_date).days

print(f'距离下次生日还有: {days_until_next_birthday}天')
