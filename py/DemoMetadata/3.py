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
asset_id = '94c9b52a29034339383ce764bddb744bc1a69d3936c4793fa08f0610e49b4759'
prev_transaction_id = '9696e8a6c64ba557b0a5504708417c0d63f738ed3efabc80d2ade8191560a4d7'

transfer_asset = {
    'id': asset_id
}



output_indexoriginal = 0
creationtx = bdb.transactions.retrieve(asset_id)
article = creationtx['asset']
creationtx['metadata']['status'] = "REVIEWED --> PUBLISHED"

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
print("-------------------------------------------------------------",)
print("Article Title  = ",getTitle(article))
print("Author         = ",getAuthor(article))
print("Link           = ",getLink(article))
print("Hash           = ",getHash(article))
print("Date           = ",getDate(article))
print("Domain         = ",getDomain(article))
print("SubDomain      = ",getSubDomain(article))
print("Status Article =",getAssetStatus(creationtx))
