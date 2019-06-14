from tronapi import Tron
from tronapi import HttpProvider

from time import time
from time import gmtime
from time import sleep
from time import strftime
from time import localtime

from sys import exc_info

full_node = HttpProvider('https://api.trongrid.io')
solidity_node = HttpProvider('https://api.trongrid.io')
event_server = HttpProvider('https://api.trongrid.io')

tron = Tron(full_node=full_node, solidity_node=solidity_node, event_server=event_server)

tron.private_key = 'someprivatekey'
tron.default_address = 'someaddr'


# tron.fromSun(tron.trx.get_balance('someaddr2'))
#print(tron.trx.get_balance())
#print(tron.trx.get_account())
#print(tron.trx.get_account_resource())

Acc = tron.trx.get_account()

SendAddr = 'someaddr3'

UnfreezeEpoch = int(Acc['frozen'][0]['expire_time']/1000)
FrozenBalance = float(tron.fromSun(Acc['frozen'][0]['frozen_balance']))

print(FrozenBalance - 10)
print(strftime('%Y-%m-%d %H:%M:%S', localtime(UnfreezeEpoch)))
print(strftime('%H:%M:%S', gmtime(UnfreezeEpoch - time())))

sleep(UnfreezeEpoch - (time() + 1.0))
#sleep(10 - (9 + 0.5))

x = 0
while x != 1:
    print(x)
    try:
        Ret = tron.trx.send_transaction(SendAddr,  float(FrozenBalance - 10), {'message': 'testapi'})
        print(Ret)
        x = 1
    except ValueError as e:
        #print(str(e))
        #sleep(0.01)
        x = 2
    except:
        print(exc_info())
        x = 3

# tron.trx.get_balance('someaddr4')

# tron.trx.unfreeze_balance()
# float(tron.fromSun(Acc['frozen'][0]['frozen_balance']) - 1)
# int(Acc['frozen'][0]['expire_time']/1000)
# int(Acc['frozen'][0]['expire_time']/1000 - time.time())

# print(tron.trx.send_transaction('someaddr5',  float(tron.fromSun(float(tron.trx.get_balance() - 1000000))), {'message': 'testapi'}))

#for x in range(1):
#for x in range(int(120/0.05)):
#    try:
#        s = tron.trx.send_transaction('someaddr6',  10.0, {'message': 'testapi %u' % x, 'time': strftime("%Y-%m-%d %H-%M-%S")})
#        print(s)
#    except ValueError as e:
#        print(str(e))
#    except:
#        print(exc_info())
#    print(x)
#    sleep(0.05)
