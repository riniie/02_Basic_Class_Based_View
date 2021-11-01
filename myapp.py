import json
import requests

URL = 'http://127.0.0.1:8000/student/'


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data()
# get_data(1)


def post_data():
    data = {
        'name': 'Kalyan',
        'roll': 106,
        'city': 'Toronto'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data()
# post_data()
# get_data()


def put_data(id):
    data = {
        'id': id,
        'name': 'Aisha',
        'roll': 104,
        'city': 'Malaysia'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data()
# put_data(4)
# get_data()


def patch_data(id):
    data = {
        'id': id,
        'name': 'Shaina'
    }
    json_data = json.dumps(data)
    r = requests.patch(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data()
# patch_data(4)
# get_data()


def delete_data(id):
    data = {'id': id}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

# get_data()
# delete_data(6)
# get_data()
