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
asset_id = '039b49765c900bcf0234c26229ccf24be1a31e2116ce053cf69984515c0071fc'
prev_transaction_id = '5fc791a7f0eb5dcc5f134afa64b29e006952cbab712e886e59188802e07ee2b2'

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