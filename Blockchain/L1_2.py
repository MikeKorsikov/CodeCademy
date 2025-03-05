# import sha256
from hashlib import sha256
# text to hash
text = "I am excited to learn about blockchain"
text2 = "I am excited to learn about blockchain!"

hash_result = sha256(text.encode())
hash_result2 = sha256(text2.encode())

# print result
print(hash_result)
print(hash_result2)
print(hash_result.hexdigest())
print(hash_result2.hexdigest())
