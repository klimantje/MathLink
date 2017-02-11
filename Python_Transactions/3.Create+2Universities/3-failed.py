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
asset_id = '7537d4fb0be1907e676c0a9496c6e84fd3ef90cd0a940b2707948b31e224b793'
prev_transaction_id = '16ef14e747151e7f4a0860e86c32b71573e936ab588cd33d747865f0b0a560c6'

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
    prepared,private_keys=uclpassword,
)



#at this stage we know the transaction id
txid = fulfilled_transfer_tx['id']

# send transfer
sent = bdb.transactions.send(fulfilled_transfer_tx)

# print

print("TRANSFER Transaction finished : 2 votes for article from UCL and VU")
print("Transaction ID = ",
    txid)

print("Article Title  = ",getTitle(asset_id))
print("Author         = ",getAuthor(asset_id))
print("Link           = ",getLink(asset_id))
print("Date           = ",getDate(asset_id))
print("Domain         = ",getAuthor(asset_id))
print("SubDomain      = ",getSubDomain(asset_id))
print("status  ",fulfilled_transfer_tx['metadata']['status'])