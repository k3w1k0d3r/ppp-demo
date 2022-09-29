from Crypto.Util.number import getStrongPrime, bytes_to_long
from secret import FLAG

p = getStrongPrime(1024)
q = getStrongPrime(1024)
e = 65537
N = p*q
message = bytes_to_long(FLAG.encode())
ct = pow(message, e, N)

print(f"p={p}")
print(f"q={q}")
print(f"N={N}")
print(f"e={e}")
print(f"ct={ct}")
