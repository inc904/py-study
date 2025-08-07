import json

with open('data.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)
    print(json_data)

json_data['port'] = 8000
print(json_data)
with open('data.json', 'w', ) as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)

    print('JSON 文件已经更新')
