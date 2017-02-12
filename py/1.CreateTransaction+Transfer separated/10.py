from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit
from CreateUsers import *

# connection
bdb = BigchainDB('http://10.4.5.2:9984')


# asset data

article = {
    'data': {
        'article': {
            'http': 'http://www.bluetrails.nl/article0001',
            'author': 'madscientist',
            'domain': 'math',
            'subdomain': 'geometry',
        },
    },
}

article_metadata = {
    'status': 'NEW'
}


# prepare creation
prepared = bdb.transactions.prepare(
    operation='CREATE',
    signers=madscientist.public_key,
    asset=article,
    metadata=article_metadata
)

# sign with user private key --> fullfilled
madscientistpassword = madscientist.private_key
uniamsterdampassword = uniamsterdam.private_key
uclpassword = ucl.private_key

fullfilled = bdb.transactions.fulfill(
    prepared,madscientistpassword
)

#at this stage we know the transaction id
txid = fullfilled['id']

# send to big chain
sent = bdb.transactions.send(fullfilled)


# display results
print("CREATION Transaction finished ")
print("Transaction ID = ",
    txid)
print("madscientist password :",madscientistpassword)
print("uniamsterdam password :",uniamsterdampassword)
print("ucl password :",uclpassword)


