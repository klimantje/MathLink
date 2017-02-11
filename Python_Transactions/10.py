from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit
from CreateUsers import *

# connection
bdb = BigchainDB('http://10.4.5.2:9984')


# asset data

velo = {
    'data': {
        'bicycle': {
            'serial_number': 'abcd1234',
            'manufacturer': 'bkfab'
        },
    },
}

velo_metadata = {
    'planet': 'earth'
}


# prepare creation
prepared = bdb.transactions.prepare(
    operation='CREATE',
    signers=alice.public_key,
    asset=velo,
    metadata=velo_metadata
)

# sign with user private key --> fullfilled
alicepassword = alice.private_key

fullfilled = bdb.transactions.fulfill(
    prepared,alicepassword
)

#at this stage we know the transaction id
txid = fullfilled['id']

# send to big chain
sent = bdb.transactions.send(fullfilled)


# display results
print("CREATION Transaction finished ")
print("Transaction ID = ",
    txid)


# display the outputs:
print("Fullfilment = 1st out",
      fullfilled['outputs'][0])
