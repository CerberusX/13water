import requests
import cards_division

url = 'http://api.revth.com'
cards_list = []
max_list = []

def sign_in(username,password):
    global url
    payload = {"username": username, "password":password}
    headers = {'content-type': "application/json"}
    r = requests.post(url+'/auth/login', json=payload, headers=headers)
    print(r.text)
    if r.status_code == 200:
        data = r.json()
        status = data['status']
        if status == 0:
            token = data.get('data').get('token')
            f = open('token.txt', 'w')
            f.write(token)
            f.close()
            f = open('user_id.txt', 'w')
            user_id = data.get('data').get('user_id')
            f.write(str(user_id))
            f.close
        return status
    else:
        return r.status_code

def newgameplay():
    global url
    global cards_list
    global max_list
    f = open('token.txt')
    token = f.readline()
    f.close
    headers = {"X-Auth-Token" : token}
    r = requests.post(url+'/game/open', headers=headers)
    print(r.text)
    data = r.json()
    status = data['status']
    game_id = data.get('data').get('id')
    cards_string = data.get('data').get('card')
    cards_list = cards_string.split(' ')
    max_list = cards_division.divide_cards(cards_list)
    front = ' '.join(max_list[10:13])
    middle = ' '.join(max_list[5:10])
    rear = ' '.join(max_list[0:5])
    payload = {
        "id": game_id,
        "card": [
            front,
            middle,
            rear
        ]
    }
    headers = {
        'content-type': "application/json",
        "X-Auth-Token": token
    }
    r2 = requests.post(url+'/game/submit', json=payload, headers=headers)
    print(r2.text)
    data = r2.json()
    status2 = data.get("status")
    for i in range(0, 13):
        if max_list[i][0] == '*':
            max_list[i] = '^'+max_list[i][1:]
    return max_list

if __name__=='__main__':
    sign_in("Cerberus", "hyh990723")
    newgameplay()


