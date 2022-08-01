"""
There is string s = "Python Bootcamp". Write the code that hashes string.
"""

import hashlib
from typing import Hashable

s = "Python Bootcamp"

hashed_s = hashlib.sha256(s.encode())
assert isinstance(hashed_s, Hashable)
assert isinstance(s, Hashable)

print(s.__hash__() or hash(s))
print(hashed_s.hexdigest())
