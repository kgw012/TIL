import requests
import json


BASE_URL = ''

def start(TOKEN, problem=1):
    '''
    res = {
        "auth_key": "1fd74321-d314-4885-b5ae-3e72126e75cc",
        "problem": 1,
        "time": 0
    }
    '''
    url = BASE_URL + '/start'
    headers = {
        'X-Auth-Token': TOKEN,
        'Content-Type': 'application/json',
    }
    data = {
        'problem': problem,
    }

    res = requests.post(url, headers=headers, data=json.dumps(data)).json()
    return res


def get_waiting_line(AUTH_KEY):
    '''
    res['waiting_line'] = [
        { "id": 1, "from": 3 },
        { "id": 2, "from": 14 },
        ...
    ]
    '''
    url = BASE_URL + '/waiting_line'
    headers = {
        'Authorization': AUTH_KEY,
        'Content-Type': 'application/json',
    }

    res = requests.get(url, headers=headers).json()
    return res['waiting_line']


def get_game_result(AUTH_KEY):
    '''
    res['game_result'] = [
        {"win": 10, "lose": 2, "taken": 7 },
        {"win": 7, "lose": 12, "taken": 33 },
        ...
    ]
    '''
    url = BASE_URL + '/game_result'
    headers = {
        'Authorization': AUTH_KEY,
        'Content-Type': 'application/json',
    }

    res = requests.get(url, headers=headers).json()
    return res['game_result']

    
def get_user_info(AUTH_KEY):
    '''
    res['user_info'] = [
        { "id": 1, "grade": 2100 },
        { "id": 13, "grade": 1501 },
        ...
    ]
    '''
    url = BASE_URL + '/user_info'
    headers = {
        'Authorization': AUTH_KEY,
        'Content-Type': 'application/json',
    }

    res = requests.get(url, headers=headers).json()
    return res['user_info']


def put_match(AUTH_KEY, pairs):
    '''
    "pairs": [[1, 2], [9, 7], [11, 49]]
    '''
    url = BASE_URL + '/match'
    headers = {
        'Authorization': AUTH_KEY,
        'Content-Type': 'application/json',
    }
    data = {
        'pairs': pairs,
    }

    res = requests.put(url, headers=headers, data=json.dumps(data)).json()
    return res

    
def change_grade(AUTH_KEY, commands):
    '''
    "commands": [
        { "id": 1, "grade": 1900 }
        ...
    ]
    '''
    url = BASE_URL + '/change_grade'
    headers = {
        'Authorization': AUTH_KEY,
        'Content-Type': 'application/json',
    }
    data = {
        'commands': commands,
    }

    res = requests.put(url, headers=headers, data=json.dumps(data)).json()
    return res


def get_score(AUTH_KEY):
    '''
    res = {
        "status": "finished",
        "efficiency_score": -1.0,
        "accuracy_score1": 0.0,
        "accuracy_score2": 32.62,
        "score": 30.94
    }
    '''
    url = BASE_URL + '/score'
    headers = {
        'Authorization': AUTH_KEY,
        'Content-Type': 'application/json',
    }

    res = requests.get(url, headers=headers).json()
    return res
