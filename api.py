import yadisk
import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = "y0_AgAAAAAcSiY8AAhg4wAAAADNv1hj-ipuYPidRrWyBBruHvGQ8gszeIA"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}


def create_folder(path):
    get_status = requests.get(URL)
    print(get_status)
    res = requests.put(f'{URL}?path={path}', headers=headers)   
    if  res.status_code == 201:
      print(f'Создали папку {path}')  
    elif res.status_code == 409:
      print(f'папка {path} существует')
create_folder('test_api_ya')
