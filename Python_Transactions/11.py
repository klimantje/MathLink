from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit



# connection
bdb = BigchainDB('http://10.4.5.2:9984')

# declare users
alicepassword = '2CpjTxiaAbJK66xPRv7suu6PVZ49UyDnTisoniBMd6uP'
bobpassword = 'GKuWornrXzR1csgDGPqqRcak4SiZPmTDeoewXgdBik7v'
bob = generate_keypair()

# asset from previous
asset_id = '5623b9fb0485d5df44aef95938169149cd57e42ddc54651be6b7096e4d8b9200'

transfer_asset = {
    'id': asset_id
}


# transfer input UNCLEAR UNCLEAR UNCLEAR




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
    recipients=bob.public_key,
    asset=transfer_asset,
)


# sign with user private key --> fullfilled

# fullfill transfer
fulfilled_transfer_tx = bdb.transactions.fulfill(
    prepared,
    private_keys=alicepassword,)

#at this stage we know the transaction id
txid = fulfilled_transfer_tx['id']

# send transfer

sent = bdb.transactions.send(fulfilled_transfer_tx)

# print

print("TRANSFER Transaction finished ")
print("Transaction ID = ",
    txid)