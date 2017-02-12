from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit
from passwords import *
from queryhelper import *

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
            'publish_date' : '31/12/2016',
            'title' : 'How to build a nice triangle in 30 secs',
        },
    },
}

article_metadata = {
    'status': 'NEW'
}


# prepare creation
prepared = bdb.transactions.prepare(
    operation='CREATE',
    signers=madscientistpublic,
    asset=article,
    metadata=article_metadata,
)

# sign with user private key --> fullfilled
madscientistpassword = madscientistpassword
vupassword = vupassword
uclpassword = uclpassword

fullfilled = bdb.transactions.fulfill(
    prepared,madscientistpassword
)

#at this stage we know the transaction id
txid = fullfilled['id']

# send to big chain
sent = bdb.transactions.send(fullfilled)


# display results
print("CREATION Transaction finished : Article Uploaded from Mad Scientist, review requested to UCL and VU ")
print("Transaction ID = ",
    txid)
print("madscientist password :",madscientistpassword)
print("VU password :",vupassword)
print("UCL password :",uclpassword)
print("Status of transaction : ", bdb.transactions.status(txid))


print("madscientist public :",madscientistpublic)
print("VU public :",vupublic)
print("UCL public :",uclpublic)

print("Article Title  = ",getTitle(article))
print("Author         = ",getAuthor(article))
print("Link           = ",getLink(article))
print("Date           = ",getDate(article))
print("Domain         = ",getAuthor(article))
print("SubDomain      = ",getSubDomain(article))






