import base64
from itertools import cycle

message = b'GVUKFA1NFxoQTxAMEBMFABwAGgleSUQLX1pcUQMVDARJDkhJRA1DQlVRDxcdRkIOVQwFDl9EREdF\nUkNBSUccChENVF9SWAdVVUFJTxEBCg1GU11RDAZeQVQOVRwNBF9VW1EGVVVBSVwTCwEBREUXFFhS\nXhIPSBdOT0gXUF9bRVJDQUlZGwdCT00='

key = b'bryan.rich0604'

print(bytes(a ^ b for a, b in zip(base64.b64decode(message), cycle(key))))