import binascii
from multiprocessing import Pool
from challenge3 import decrypt, score

def b642hex(s):
    return binascii.hexlify(binascii.a2b_base64(s))

def repeated_key_xor_decrypt(s, max_len=40):
    """
    Decrypts a CT hex string that has been encrypted by a repeating key XOR.
    My method: For each key length from 2 to max_len, compute the best possible
               PT using all possible keys. Then, out of those max_len-1 PTs,
               take the best PT. Computing the best possible PT for a key of a
               given length is done as follows: For each k-interval substring
               of the CT offset by i, where k is the key length and
               0 <= i < len(CT), compute the score of the substring and take
               the PT with the best score.
    @param s [str]: CT (hex string)
    @param max_len [int]: Maximum repitition length of the repeating key.
    @returns [str]: PT (ASCII string)
    """

    def fixed_len_repeated_key_xor_decrypt(keylen):
        """
        Decrypts a CT hex string that has been encrypted by a repeating key
        XOR with a key of a known length
        @param keylen [int]: Repitition length of the repeating key.
        @returns [tuple]: ([int], [str], [int]) where t[0] is the score
                                                      t[1] is the PT
                                                      t[2] is the key length
        """

        p = Pool(10)
        pt_segments = p.map(decrypt, [''.join(ct_split[i::keylen])
                                      for i in range(keylen)])
        pt_score = sum([score(pt_segment) for pt_segment in pt_segments])
        # zip the segments
        pt = ''.join([pt_segments[j][i] for i in range(len(pt_segments[0]))
                                        for j in range(len(pt_segments))
                                        if i < len(pt_segments[j])])
        return (pt_score, pt, keylen)

    # Split the CT into bytes. 0-pad the front if necessary
    if len(s) % 2 == 1:
        s = '0' + s
    ct_split = [s[i:i+2] for i in range(0, len(s), 2)]

    attempts = []
    for keylen in range(2, max_len+1):
        result = fixed_len_repeated_key_xor_decrypt(keylen)
        attempts.append(result)
    return sorted(attempts, key=lambda x: x[0], reverse=True)[0]

if __name__=='__main__':
    filename = 'data06.txt'
    with open(filename, 'r') as f:
        txt = ''.join([line.strip() for line in f])
    hextxt = b642hex(txt)
    print(repeated_key_xor_decrypt(hextxt)[1])