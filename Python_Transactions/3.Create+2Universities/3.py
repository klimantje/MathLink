from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit
from passwords import *


# connection
bdb = BigchainDB('http://10.4.5.2:9984')

#public keys

# asset from previous
asset_id = '981bca8aef582b007e2e85a6c48a739c6a89796c1f986b0ed2757f33ab2bbb72'
prev_transaction_id = '892f8d091ec2142546d776a916839810ac643c8d8308d571a60e69e08fb44c81'

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

print("TRANSFER Transaction finished : 2 votes for article from UCL and VU")
print("Transaction ID = ",
    txid)