import hmac
from hashlib import md5

key = 'key'

h = hmac.new(key,'AAAABBBBCCCCD',md5)


## print the HMAC digest
print h.hexdigest()

#outut 922774d006bcf3fdd0b42a14a22af602

