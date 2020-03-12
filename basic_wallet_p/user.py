import requests

user = input('Enter a user ID: ')

def get_data(userid):
    data = requests.get('http://127.0.0.1:4000/chain').json()
    chain = data['chain']
    runningamount = 0
    sent = []
    received = []
    for i in chain:
        for a in i['transactions']:
            if a['sender'] == user:
                runningamount -= float(a['amount'])
                sent.append((a['recipient'], float(a['amount'])))
            if a['recipient'] == user:
                runningamount += float(a['amount'])
                received.append((a['sender'], float(a['amount'])))
    return(runningamount, sent, received)

def history():
    data = get_data(user)
    print('Transaction History Sent:')
    for i in data[1]:
        print(f"{i[0]} ---- {i[1]}")
    print('\n\n')
    print('Transactions recived')
    for i in data[2]:
        print(f"{i[0]} ---- {i[1]}")

def total():
    data = get_data(user)
    print(data[0])
def chang_user():
    user = input('enter user name: ')
    return(user)


while True:
    command = input('Enter command: ')
    try:
        if command == 'change user':
            user = chang_user()
        else:
            function = eval(command)
            function()
    except:
        print('not valid command')

