import requests
from bs4 import BeautifulSoup
import json


def get_top_project():
    url = 'https://github.com/trending'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    print('response:',response)
    soup = BeautifulSoup(response.text, 'html.parser')
    project_list = []

    projects = soup.find_all('article', class_='Box-row')

    for project in projects:
        project_data = {}

        # 获取项目名称
        name_elem = project.select_one('.h3')
        project_data['name'] = name_elem.text.replace(' ', '').replace('\n', '').strip()

        # 获取项目描述
        desc_elem = project.select_one('p')
        if desc_elem:
            project_data['desc'] = desc_elem.text.strip()
        else:
            project_data['desc'] = None

        # 获取项目链接
        link_elem = project.select_one('.h3 a')
        project_data['link'] = 'https://github.com' + link_elem['href']

        project_list.append(project_data)

    return project_list


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    data = get_top_project()
    save_to_json(data, 'top_50_in_github.json')