from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

# declare users
madscientist = generate_keypair()
vu = generate_keypair()
ucl = generate_keypair()


print("Please update passwords.py as follows:",)


print("#public keys",)
print("madscientistpublic ='",madscientist.public_key,"'",sep='')
print("vupublic = '",vu.public_key,"'",sep='')
print("uclpublic = '",ucl.public_key,"'",sep='')

print("#private keys",)
print("madscientistpassword = '",madscientist.private_key,"'",sep='')
print("vupassword = '",vu.private_key,"'",sep='')
print("uclpassword = '",ucl.private_key,"'",sep='')







