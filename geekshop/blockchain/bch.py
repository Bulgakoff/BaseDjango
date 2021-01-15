import hashlib

block = hashlib.sha1(b'Fkred').hexdigest()
print(block)
