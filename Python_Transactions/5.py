from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit

alice, bob, amit = generate_keypair(), generate_keypair(), generate_keypair()

bdb = BigchainDB('http://10.4.5.2:9984')

article_asset = {
    'data': {
        'article1': {
            'http': 'http://www.bluetrails.nl',
            'author': 'An de Rijdt'
        },
    },
}

article_asset_metadata = {
    'planet': 'earth'
}

prepared_creation_tx = bdb.transactions.prepare(
    operation='CREATE',
    signers=amit.public_key,
    asset=article_asset,
    metadata=article_asset_metadata
)

fulfilled_creation_tx = bdb.transactions.fulfill(
    prepared_creation_tx,
    private_keys=amit.private_key
)

sent_creation_tx = bdb.transactions.send(fulfilled_creation_tx)

txid = fulfilled_creation_tx['id']

trials = 0
while trials < 60:
    try:
        if bdb.transactions.status(txid).get('status') == 'valid':
            print('Tx valid in:', trials, 'secs')
            break
    except bigchaindb_driver.exceptions.NotFoundError:
        trials += 1
        sleep(1)

if trials == 60:
    print('Tx is still being processed... Bye!')
    exit(0)

asset_id = txid

transfer_asset = {
    'id': asset_id
}

output_index = 0
output = fulfilled_creation_tx['outputs'][output_index]

transfer_input = {
    'fulfillment': output['condition']['details'],
    'fulfills': {
        'output': output_index,
        'txid': fulfilled_creation_tx['id']
    },
    'owners_before': output['public_keys']
}

prepared_transfer_tx = bdb.transactions.prepare(
    operation='TRANSFER',
    asset=transfer_asset,
    inputs=transfer_input,
    recipients=bob.public_key,
)

fulfilled_transfer_tx = bdb.transactions.fulfill(
    prepared_transfer_tx,
    private_keys=amit.private_key,
)

sent_transfer_tx = bdb.transactions.send(fulfilled_transfer_tx)

print("Is Bob the new owner 2222?",
    sent_transfer_tx['outputs'][0]['public_keys'][0] == bob.public_key)

print("was alice before ???",
    fulfilled_transfer_tx['inputs'][0]['owners_before'][0] == amit.public_key)