import hashlib

def generate_hash(data, algorithm='sha256'):
    if algorithm == 'sha256':
        hash_object = hashlib.sha256()
    elif algorithm == 'sha512':
        hash_object = hashlib.sha512()
    elif algorithm == 'md5':
        hash_object = hashlib.md5()
    else:
        raise ValueError("지원되지 않는 해시 알고리즘입니다.")
    
    hash_object.update(data.encode('utf-8'))
    return hash_object.hexdigest()

if __name__ == "__main__":
    text = input("해시를 생성할 문자열 입력: ")
    print("SHA-256 해시:", generate_hash(text, 'sha256'))
    print("SHA-512 해시:", generate_hash(text, 'sha512'))
    print("md5 해시:", generate_hash(text, 'md5'))