# 变量定义和赋值
name = 'Jack'
age = 25
isStudent = False

print(name)
print(age)
print(isStudent)

a = 'aavdsaacsdaaa2cccaa'

b = a.count('aa')
print('b:', b)

my_str = 'hello'
c = my_str.center(200, ' ')
print('mt_str:', c)

num1 = 10.5
num2 = 5
num3 = 11

print('相除', num1 / num2)
print('取余1', num1 % num2)
print('取余2', num3 % num2)
print('指数', 3 ** 3)

num2 += 1
print('自增', num2)
print('sum', sum([num3, num2, num1]))

mb = '8192MB'
int_gb = int(mb[:-2]) // 1024
print(f"该硬盘容量为: {int_gb}GB")


print('整除', num3 // num2)

person = {
    'name_1':'jack',
    'age_1': 18,
    'years': 30
}
print(person)

school = dict(name = 'Tinghua', years= 1900)
print(school)

print(len(school))
seq = ('Google', 'Runoob', 'Taobao')

# 不指定默认的键值，默认为 None
thisdict = dict.fromkeys(seq)
print("新字典为 : %s" % str(thisdict))

tinydict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}

print("字典值 : %s" % tinydict.items())

school.update(person)
print(school)

fruits = range(1,21)
print(fruits, type(fruits))



def some_fn(position_arg, *args, **kwargs):
    print(position_arg)
    print(args)
    print(kwargs)

some_fn('position_arg_value','add_to_args1','add_to_args2',a=1,b=2,c=3)