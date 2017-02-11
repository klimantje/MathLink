from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit



# connection
bdb = BigchainDB('http://10.4.5.2:9984')

#public keys

madscientistpublic = 'an7hnPLnS2yFbdsUaske42eFG4h9a9pxNskg6jPqRa8'
vupublic = '26mChkVgbcV1TJ58Gff3K9LaMnPkUzcrrtYu78SnjGB1'
uclpublic = 'GuAVXyBCRK9J8gN3EjQ7hS9h8MWtJcQ3kQhzLRQBSHmd'

# sign with user private key --> fullfilled
madscientistpassword = '37c5jPgf9ZiMaVvHMADNKPnNgMy7rB5hFqrWGQUjQZeC'
vupassword = '6CHWDPUSjjuWLGbcnfDx3YPMBT3cLAoR8Fw2zDcXRD5s'
uclpassword = 'CUJGQQeE7PMn1w2TNsXFNtw1HVChsWRSEhchif8JoP7S'

# asset from previous
asset_id = 'f457f5e967de3e7fcc8e38f3c8c89937ae85ead53d37b9e37034339acc625f23'

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
    recipients=vupublic,
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
