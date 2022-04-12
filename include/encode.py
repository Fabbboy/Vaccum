import hashlib


def encode(msg, algo):
    if algo == "md5":
        return hashlib.md5(msg.encode()).hexdigest()
    elif algo == "sha1":
        return hashlib.sha1(msg.encode()).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(msg.encode()).hexdigest()
    elif algo == "sha512":
        return hashlib.sha512(msg.encode()).hexdigest()
    else:
        return "Invalid algorithm"
