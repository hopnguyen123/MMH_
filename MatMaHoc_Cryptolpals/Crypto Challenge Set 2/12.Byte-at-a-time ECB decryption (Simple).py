def cookie2dict(s: str) -> dict:
    return dict(map(lambda x: x.split('='), s.strip('&').split('&')))

assert cookie2dict('foo=bar&baz=qux&zap=zazzle') == {
    'foo': 'bar',
    'baz': 'qux',
    'zap': 'zazzle'
}
def dict2cookie(d: dict) -> str:
    # assume all k-v are strings
    return '&'.join(map('='.join, d.items()))

assert dict2cookie({
    'foo': 'bar',
    'baz': 'qux',
    'zap': 'zazzle',
}) == 'foo=bar&baz=qux&zap=zazzle'
def profile_for(email: str):
    return dict2cookie({
        'email': email.replace('&', '').replace('=', ''),
        'uid': str(10),
        'role': 'user'
    })

assert profile_for("foo@bar.com") == 'email=foo@bar.com&uid=10&role=user'
def pkcs7_unpad(s: bytes) -> bytes:
    return s[:-s[-1]]

random_key = generate_key()
# for the attacker
def encrypt_profile(email: str) -> bytes:
    s = profile_for(email).encode()
    s = pkcs7(s, len(s) + 16 - (len(s) % 16))
    return AES_encrypt(random_key, s, 'ecb')

def decrypt_profile(s: bytes) -> dict:
    return cookie2dict(pkcs7_unpad(AES_decrypt(random_key, s, 'ecb')).decode())
