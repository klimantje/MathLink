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
            'http': 'http://www.bluetrails.nl/article0001.pdf',
            'author': 'madscientist',
            'hash': 'HDFAHOFRIHBJR124937597KJLJLHLBFBJHFFLKFFKLFFNNFK',
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
print("CREATION Transaction finished : Article Uploaded Ready for Random Review")
print("-------------------------------------------------------------",)
print("Transaction ID = ",
    txid)
print("Status of transaction : ", bdb.transactions.status(txid))

print("-------------------------------------------------------------",)
print("Article Title  = ",getTitle(article))
print("Author         = ",getAuthor(article))
print("Link           = ",getLink(article))
print("Hash           = ",getHash(article))
print("Date           = ",getDate(article))
print("Domain         = ",getDomain(article))
print("SubDomain      = ",getSubDomain(article))






