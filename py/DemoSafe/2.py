from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit
from passwords import *
from queryhelper import *


# connection
bdb = BigchainDB('http://10.4.5.2:9984')



# asset from previous
asset_id = '5abf802a57c37abefe559ba4b5ae682e902e819e76033359d7a0a2a30865a69d'



transfer_asset = {
    'id': asset_id
}


output_index = 0
prevtransaction = bdb.transactions.retrieve(asset_id)
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
    recipients=(vupublic, uclpublic),
    asset=transfer_asset,
)


# sign with user private key --> fullfilled

# fullfill transfer
fulfilled_transfer_tx = bdb.transactions.fulfill(
    prepared,
    private_keys=madscientistpassword,)




#at this stage we know the transaction id
txid = fulfilled_transfer_tx['id']

# send transfer

sent = bdb.transactions.send(fulfilled_transfer_tx)

# print

print("TRANSFER Transaction finished . Review Requested to universities : UCL and VU ")
print("Transaction ID = ",
    txid)
print("-------------------------------------------------------------",)
print("Status of transaction : ", bdb.transactions.status(txid))


