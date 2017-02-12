from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit
from passwords import *
from queryhelper import *

# connection
bdb = BigchainDB('http://10.4.5.2:9984')

#public keys

# asset from previous
asset_id = '5abf802a57c37abefe559ba4b5ae682e902e819e76033359d7a0a2a30865a69d'
prev_transaction_id = '5e016a7a7c5debb7eb6783afa22cb18023e1bb8c8416c8cb4810855b0918e947'

transfer_asset = {
    'id': asset_id
}





output_index = 0
prevtransaction = bdb.transactions.retrieve(prev_transaction_id)
output = prevtransaction['outputs'][output_index]

transfer_input = {
    'fulfillment': output['condition']['details'],
    'fulfills': {
        'output': output_index,
        'txid': prevtransaction['id']
    },
    'owners_before': output['public_keys']
}



# prepare transfer
prepared = bdb.transactions.prepare(
    operation='TRANSFER',
    inputs=transfer_input,
    recipients=madscientistpublic,
    asset=transfer_asset,
)




# fullfill transfer
fulfilled_transfer_tx = bdb.transactions.fulfill(
    prepared,private_keys=[vupassword, uclpassword],
)



#at this stage we know the transaction id
txid = fulfilled_transfer_tx['id']

# send transfer
sent = bdb.transactions.send(fulfilled_transfer_tx)

# print

print("TRANSFER Transaction finished : 2 votes received for article from UCL and VU")
print("-------------------------------------------------------------",)
print("Transaction ID = ",
    txid)
print("Status of transaction : ", bdb.transactions.status(txid))


