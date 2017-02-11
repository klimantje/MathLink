from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit


# connection
bdb = BigchainDB('http://10.4.5.2:9984')

# declare users
bob = generate_keypair()
alice = generate_keypair()

# asset from previous
asset_id = '292e267c6bef70acd616618f800e2f14758e00f807f6d8c67412e1d92f7e15'

# transfer input UNCLEAR UNCLEAR UNCLEAR


# prepare transfer
transfer_input = {
    'fulfillment': None,
    'fulfills': {
        'output': 0,
        'txid': asset_id
    },
    'owners_before': alice.public_key
}


prepared = bdb.transactions.prepare(
    operation='TRANSFER',
    asset=asset_id,
    inputs=transfer_input,
    recipients=bob.public_key)


# sign with user private key --> fullfilled

# fullfill transfer
alicepassword = alice.private_key

fullfilled = bdb.transactions.fulfill(
    prepared,alice.privatechain)

#at this stage we know the transaction id
txid = fullfilled['id']

# send transfer

sent = bdb.transactions.send(fullfilled)

# print

print("TRANSFER Transaction finished ")
print("Transaction ID = ",
    txid)