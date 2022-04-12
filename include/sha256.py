import hashlib


def sha256(msg):
    # turn msg into a byte string
    msg = msg.encode()
    # create a hash object
    h = hashlib.sha256(msg)
    # return the hex representation of digest
    return h.hexdigest()

