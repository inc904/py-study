const currentDate = new Date()
const birthday = new Date(1995, 1, 28)

let age = currentDate.getFullYear() - birthday.getFullYear()

// 今年是否过了生日
const isAfterBirthday = currentDate.getMonth() > birthday.getMonth() || (currentDate.getMonth() === birthday.getMonth() && currentDate.getDate() >= birthday.getDate())
console.log(isAfterBirthday)

// 计算年龄
if (!isAfterBirthday) {
    age--
    console.log(age - 1)
}


const nextBirthdayYear = isAfterBirthday ? currentDate.getFullYear() + 1 : currentDate.getFullYear()


const nextBirthday = new Date(nextBirthdayYear, birthday.getMonth(), birthday.getDate())

// 计算下次生日还有几天

const daysUntilNextBirthday = Math.ceil((nextBirthday.getTime() - currentDate.getTime()) / (1000 * 60 * 60 * 24))
console.log(daysUntilNextBirthday)

console.log('年龄：', age)
console.log('距离下次生日还有：', daysUntilNextBirthday, '天')
