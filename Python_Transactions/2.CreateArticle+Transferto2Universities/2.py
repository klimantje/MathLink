from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit
from CreateUsers import *


# connection
bdb = BigchainDB('http://10.4.5.2:9984')


# sign with user private key --> fullfilled
madscientistpassword = 'FxHGH5JheWrhDsbtp13bkPmm7DLSpVk32WUVSMV9shvK'
uniamsterdampassword = 'ChC25KQybm2UhdJ2xhdc723dQ87ESZXekWxjEFF2XAHL'
uclpassword = 'Dszq4p4mnBijXo7UjXuaLd61LC9HjEen7yUG9sK7xBni'

# asset from previous
asset_id = '76837cfef8df3e91d38dcff799eefef92f426b6e06e8521bff0566271db6ff7c'

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
    recipients=(uniamsterdam.public_key, ucl.public_key),
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

print("TRANSFER Transaction finished ")
print("Transaction ID = ",
    txid)