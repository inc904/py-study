# 读取books.txt文件内容

with open('books.txt', 'r', encoding='utf-8') as file:
    books = file.read().splitlines('\r\n')



classics = ['西游记', '水浒传', '三国演义', '红楼梦']
# missing = [classics for classic in classics if classics not in books]
missing = [classics for classic in classics if classics not in books]
print(missing)

# if len(missing) == 0:
#     print('没有缺书')
# else:
#     print('缺书：', missing)
#     with open('missing.txt', 'a', encoding='utf-8') as file:
#         file.write('\n'+ '/n'.join(missing))
#     print(f'已补充缺失的名著到文件中',{", ".join(missing)}"})



# # 读取books.txt文件内容
# with open('books.txt', 'r', encoding='utf-8') as file:
#     books = file.read().splitlines()
#
# # 检查是否包含中国四大名著
# classics = ['红楼梦', '西游记', '水浒传', '三国演义']
# missing_classics = [classic for classic in classics if classic not in books]
#
# if len(missing_classics) == 0:
#     print('文件中已包含中国四大名著。')
# else:
#     # 补充缺失的名著到文件中
#     with open('books.txt', 'a', encoding='utf-8') as file:
#         file.write('\n' + '\n'.join(missing_classics))
#     print(f'已补充缺失的名著到文件中: {", ".join(missing_classics)}')