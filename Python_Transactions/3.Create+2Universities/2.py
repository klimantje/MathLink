from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit
from passwords import *
from queryhelper import *


# connection
bdb = BigchainDB('http://10.4.5.2:9984')



# asset from previous
asset_id = '039b49765c900bcf0234c26229ccf24be1a31e2116ce053cf69984515c0071fc'

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

print("TRANSFER Transaction finished . Review Requested to UCL and VU ")
print("Transaction ID = ",
    txid)

print("madscientist password :",madscientistpassword)
print("VU password :",vupassword)
print("UCL password :",uclpassword)
print("Status of transaction : ", bdb.transactions.status(txid))


print("Article Title  = ",getTitle(transfer_asset))
print("Author         = ",getAuthor(transfer_asset))
print("Link           = ",getLink(transfer_asset))
print("Date           = ",getDate(transfer_asset))
print("Domain         = ",getAuthor(transfer_asset))
print("SubDomain      = ",getSubDomain(transfer_asset))

