from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit
from CreateUsers import *


# connection
bdb = BigchainDB('http://10.4.5.2:9984')

txid = '8947f802aa3b938f058814907858ef45f91f2da4f659a0bed68bdff226cb57f5'
print("Status of transaction : ", bdb.transactions.status(txid))
print("vu public key : ", vu.public_key)
print("ucl public key : ", ucl.public_key)
print("mad public key : ", madscientist.public_key)