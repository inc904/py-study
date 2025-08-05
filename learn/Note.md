## 变量

### 定义和赋值

- 和JS一样使用 `=` 进行赋值
- python 不需要在语句末尾加上分号
- 不需要 `let` 或者 `var` 这样的生命变量关键字。
    - 那就没有声明变量但不赋值的写法了
- python 里没有常量的概念，默认约定使用 `全部大写字母和下划线组合命令的变量叫做常量`

| 名称  | JavaScript       | Python           |
|-----|------------------|------------------|
| 变量名 | userName         | user_name        |
| 类名  | UserName         | Username         |
| 函数名 | getById          | get_by_id        |
| 常量名 | DEFAULT_LOGO_URL | DEFAULT_LOGO_URL |

- `str` 是python的一个内置函数，所以不能像在js中那样作为变量名使用了

| 内置函数  | 	作用       |
|-------|-----------|
| str   | 将对象转换为字符串 |
| dict  | 创建字典对象    |
| list  | 创建列表对象    |
| set   | 创建集合对象    |
| tuple | 创建元组对象    |
| int   | 将对象转换为整数  |
| float | 将对象转换为浮点数 |
| bool  | 将对象转换为布尔值 |
| len   | 返回对象的长度   |
| print | 将对象打印到控制台 |

## 数据类型

### 基本数据类型

- 整数：没有小数点的数字 int
- 浮点数：带有小数点的数字 float
- 字符串：单引号双引号包裹的字符
- 布尔值： True False
- 空值：None， py中没有 undefined

- py中使用 `type()` 获取数据类型，等价于js中的 `typeof()`

### 字符串方法

| 方法         | JavaScript                                                     | Python                           |
|------------|----------------------------------------------------------------|----------------------------------|
| 获取长度       | myStr.length                                                   | len(my_str)                      |
| 拼接         | myStr1 + myStr2                                                | my_str1+my_str2                  |
| 截取         | myStr.slice(start, end)                                        | my_Str[start:end]                |
| 查找         | mtStr.indexOf(substring)                                       | my_str.index(substring)          |
| 替换         | myStr.replace(odl, new)                                        | my_str.replace(old, new)         |
| 分割         | myStr.split(separator)                                         | mt_str.split(separator)          |
| 大写转换       | myStr.toUpperCase()                                            | my_str.upper()                   |
| 小写转换       | myStr.toLowerCase()                                            | my_str.lower()                   |
| 反转         | myStr.split('').reverse().join('')                             | my_str[::-1]                     |
| 统计子串出现的次数  | myStr.split(substring).length -1                               | my_str.count(substring)          |
| 是否以指定字符开头  | myStr.startWith(prefix)                                        | my_str.startWith(prefix)         |
| 是否以指定字符结尾  | myStr.endWith(suffix)                                          | myStr.endWith(suffix)            |
| 删除两段空白字符   | myStr.trim()                                                   | my_str.strip()                   |
| 按指定宽度居中对齐  | -                                                              | my_str.center(width[, fillchar]) |
| 第一个单词首字母大写 | myStr.replace(myStr[0], myStr[0].toUpperCase())                | my_str.capitalize()              |
| 每个单词首字母大写  | `myStr.replace(/(^\w{1})\|(\s+\w{1})/g, s => s.toUpperCase())` | my_str.title()                   |

### 基本数据类型的算数运算

```python
num1 = 10
num2 = 5
num3 = 2
# 相加
sum_val = num1 + num2

# 相减
diffence = num1 - num2

# 相乘
product = num1 * num2

# 相除
quotient = num1 / num2

# 取余
remainder = num1 % num2

# 指数运算
power = num1 ** num2

# 自增
num1 += 1

# 自减
num1 -= 1

print('sum', sum([num3, num2, num1]))


```

### 类型转换

假设有一块硬盘的容量为 8192MB（字符串），请将这块硬盘的容量换算为 GB 单位，将换算结果保存到一个整数类型变量中。

```javascript
let mb = '8192MB';
let gb = parseInt(mb) / 1024
let intGb = parseInt(gb)
console.log(`该硬盘容量为: ${intGb}GB`)
```

```python
mb = '8192MB'
int_gb = int(mb[:-2]) / 1024
print(f"该硬盘容量为: {int_gb}GB")

```

| 特性     | Javascript                    | Python     |
|--------|-------------------------------|------------|
| 转换为整数  | parseInt(val) 或 Numer(val)    | int(val)   |
| 转换为浮点数 | parseFloat(val) 或 Number(val) | float(val) |
| 转换为字符串 | val.toString() 或 String(val)  | str(val)   |
| 转换为布尔值 | Boolean(val)                  | bool(val)  |
| 转换为数组  | -                             | list(val)  |
| 转换为对象  | -                             | dict(val)  |

### 列表和元组

- python 中，数组被称为列表
- js 中使用 push 向数组中添加元素，py 中使用 append 向列表中添加元素
- 元组可以理解为只读的数组，它在创建时确定元素个数和元素的值，一旦创建就不能被修改

| 特性    | Javascript                                                                | Python                                                  |
|-------|---------------------------------------------------------------------------|---------------------------------------------------------|
| 创建    | let myArr = new Array();<br/> let myArr = [1,2]; <br/>let myTuple = [1,2] | my_list =[1,2]<br/>  my_list=list()<br/> my_tuple=(1,2) |
| 访问    | let el = myArr[index]                                                     | el= my_list[index]                                      |
| 添加    | myArr.push(el)                                                            | my_list.append(el)                                      |
| 长度    | let length = myArr.length()                                               | length = len(my_list)                                   |
| 切片    | let  someEl = myArr.slice(start, end)                                     | some_el = my_list[start:end]                            |
| 连接    | let mergeArr = myArr.concat(myArr2)                                       | merged_arr = arr1 + arr2                                |
| 复制    | let newArr = [...arr1]                                                    | new_list = list1.copy()                                 |
| 反转    | myArr.reverse()                                                           | list1.reverse()                                         |
| 删除    | arr1.splice(index,1)                                                      | del list1[index]                                        |
| 求最大值  | let maxVal = Math.max(...arr1)                                            | max_val = max(list1)                                    |
| 求最小值  | let minVal = Math.min(...arr1)                                            | min_val = min(list1)                                    |
| 求和    | let sum = arr1.reduce((a,b)=> a+b, 0)                                     | sun_val = sum(list1)                                    |
| 转换为元组 | -                                                                         | my_tuple = tuple(list1)                                 |

### 字典

```javascript
let personalInfo = {};
 
personalInfo.name = 'luckrnx09',
personalInfo.age = 18,
personalInfo.city = '成都'

console.log(personalInfo);
```

```python

personal_info = {}

personal_info['name'] = 'Jack'
personal_info['age'] = '19'
personal_info['city'] = '重庆'

```

- py 和js 都可以 使用 `{}` 创建空字典/对象
- py 中只能使用 方括号 `[_prop]`访问值

- py 中 使用 `{}` 创建字典时， 字典的 key 必须使用引号包裹

| 特性       | Javascript                                                                           | Python                                                                                            |
|----------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| 定义       | let obj1 = {};<br/> let obj2 = {key1: val1, key2: val2} <br/> let obj = new Object() | dict1 = {}<br/>dict2={"key1":val1, "key2": val2}<br/>school = dict(name = 'Tinghua', years= 1900) |
| 访问值	     | 	obj[key]; obj.key                                                                   | my_dict[key]                                                                                      |
| 访问值或默认值	 | obj[key] ?? defaultVal;                                                              | my_dict.get(key, default_value)                                                                   |
| 合并和更新    | obj={...obj,...anotherObj}                                                           | my_dict.update(another_dict)<br/>                                                                 |

### 集合

- Python 使用 set() 创建集合，JavaScript 使用 new Set() 创建集合

## 分支和循环

### if语句

```javascript
const number = 300 
if(number > 0){
  console.log('正数')
}else if(number < 0){
  console.log('负数')
}else{
  console.log('零')
}
```

```python
number = 100

if number > 0:
    print('正数')
elif number > 0:
    print('负数')
else:
    print('零')
```

- Python if 语句中的条件周围不需要加圆括号，JavaScript 需要为条件添加圆括号。
- Python 使用冒号（:）表示条件结束，并使用 缩进 来表示代码块，JavaScript 直接使用 {} 表示代码块。
- Python 使用 elif 继续匹配判断条件，而 JavaScript 中使用 else if。
- Python 使用严格的代码缩进表示代码块（一般为四个空格）,多加空格或少加空格都会引发语法错误
- 代码块中不需要执行实际的逻辑时，为了让程序能正常运行，可以使用 pass 表示什么都不做
-

| 特性    | Javascript                                 | Python                                      |
|-------|--------------------------------------------|---------------------------------------------|
| 逻辑运算符 | `&&`、` \|\|`、`!`                           | `and` `or`  `not`                           |
| 三元    | let estimation =  score >= 60 ? '及格'：'不及格' | estimation = '及格' if score >= 60 else '不及格' |

python 中判断一个值是否为空，可以使用
- is None
- is not None
- == None
- != None

python  中没有 `switch-case` 语句

### for和while语句

### 列表推导和字典推导

## 函数

```javascript
function greet(name, age, gender='保密') {
  console.log(`你好，我是${name}，今年${age}岁，性别${gender}`)
}

greet('张三', 18);
greet('李四', 18, '男');
greet(...['王五', 18, '女']);
```

```python

def greet(name, age, gender='保密'):
    print(f"你好， 我是{name}, 今年{age}岁，性别{gender}")

greet('张三', 18) # 传入位置参数
greet(age=18, name='张三') # 传入关键字参数
greet('李四', 18, '男')
greet(*['王五',18,'女'])

```

- python 使用 `def` 定义函数
- 使用 `:` 和 缩进 表示函数体
- python 除了默认值参数（上面的 gender ）之外，函数的每一个参数都是必传的，否则会出现语法错误
- python 中，按照顺序传入的参数叫 **位置参数**，必须按照星灿定义顺序传入
- 使用 `key=value`的形式向函数传入 **关键字参数**， 关键字参数不必于形参保持一致
- 位置参数和关键字参数可以一起使用，但**必须保证调用函数时提供了所有必须参数**
- python 可以使用 `my_fn(*[p1,p2,...])` 的形式传入位置参数，等价于js中的 `my_fn(...[p1,p2,...])`

获取函数入参：
