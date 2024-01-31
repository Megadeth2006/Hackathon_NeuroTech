import hashlib

def calculate_sha(input_string):
    """Calculate the SHA1 hash of the input string"""
    sha1_hash = hashlib.sha256(input_string.encode()).hexdigest()
    return sha1_hash

def compare_hash(input_string, hash_value):
    """Compare the hash of the input string with the given hash value"""
    sha1_hash = hashlib.sha256(input_string.encode()).hexdigest()
    return sha1_hash == hash_value

if __name__ == "__main__":
    k = calculate_sha("hello")
    print(len(k))
    print(compare_hash("hello", k))
    print(compare_hash("hell0", k))