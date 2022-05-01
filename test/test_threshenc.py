from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
import random
from honeybadgerbft.crypto.threshenc.tpke import TPKEPublicKey, TPKEPrivateKey, dealer
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Cipher import AES
from ctypes import cdll



def threshenc1():
    PK, SKs = dealer(players=100,k=35) # one PK, 100 SKS
    
    m = SHA256.new(b'{\"N\":\"ab77b9c6bf5adc7868eba8cb1ce5b4c425017454526b526422416fd4bca638abeafef0565d255295851aa5eb63d65fc02e95c4df9e77ebd5602a05f6d6f907ce61c3364c5795f65a6d0723e7d2073925633e3a392df4aef7ac347aba3ed31ffc44faa2ddd78818050a5f70af5bbbebe1619788779eee2dad256c0366e7eec79d01a3e20992ce742e35b0a49dd35bcc4219d6b7ec3dc6e044746703264d6070fad6f074af7b46f578682e4a058c53606c18826edbf903c4cafa4c511eeec6d8f9d6bd15d43f9ff41ac98e07dcdceaf4b2ad1fdb6d02e8e628aa46f1da0b3eb8c6cf715abcb5cc5bbd60ceaa458df95c121323e9e3c1a3683bcff28187c731df2b748fe48843bc80c57d7db0aaef906d27da6be1ce80a4f7d49da37fe709c3d68a65f40612f07ae693311ffc1424b68bd6600cedaf257aee8b60c3a1b8faaaee40bb4326a64912a9618265b5f8c8cd4efe9ab11a6f296caa4ef7d8ad2315294a3436fbb22a4712ebfdb301391f1a99f5defbcc65e7aba3764fe9c8718b1755113dd4fe350e204654db91653c76b5e9c06a5592cc30e6f5129aa9432880bd46c239a81e8f5e6992476a796354b47438d81e5541cece4b309e5f29a51329c4b98b9752033a99a4c9d7081930765afd81f7b5764c37bcd988dee66763897e24ec1f3577f7228b3e86a011018d34b1abeb09db971fbccef8b0c1e5ad4c70f560339e9b\",\"T\":300,\"pi\":\"a711952a00efe110ed6615bc2f4ae38435d9fa77a20a4bff8f2fa709ad3d16373ece52851901e926d0cb89b151fd1faea5cbad42274179ea268ccc4ad8bd142ac9c7ede4869ed36c7c0b59c30ec7c93d681cac7c85701adf75b89a708c5ce36816cde2113b9434f9003ecbb69fbd601510cfcfd6199c92aadbfc8859ac944b979e1df9daa558505f8e3cd3b4136d8ca52a944f8cb7ff4a6c4651f3404b322ae3a143a96a0ba111e25c11c9bd9a22a041e6be3db3ab0bae00cec607712578004a472c523826e47c6dbd773f88bb9e3afe038aeb1c2cbd4277ec7e581a69208ae5618c63f19959867beb257ca13197e3acc87b7b0ae4f175e4fd2150d2179bc8e60ee373a39d472f1732e09f76e13faa26fc1470ac54b59acf73afc16877a1b3046af0b31ca5c7e9796b04bd96474a2575caa5217c5614988c4e2aaa5bbc388c02ef4d02f8bd93df800f2218874292a5702b123bdaafcbba449a08ffbc15ffb871b5e1d73b09e39466ed399d3bb53cc24f89f1d4f7713b8fe2e6fa359fb35985c29eb5983349eb1300a9c37ade7d1f260653321a439176e9912aadc4a15a04c79d9a1d9bc8180aa84c4649b427181eaa95117c699d4bf4898c3ef5fb248c81f3d4564813786ae03b0de0abd11d074f3c935e2afd3f2df3d6cc5aedfadcb67f699cc8cc0e3a0c4632932e9d61cec73d69fceaf4e35f72d6ea42082c2eb27a674636\",\"nextprime_l\":\"d747a852e9f4d35b5c1eb76609e8a93e7a9aaab2d2082c4af6209a2be1474d19\",\"identity\":\"6a4e569f05ae9c604012b146cbd16e3f1402dcdc28391538428325480418c84c\"}').digest()
    C = PK.encrypt(m)
    # print(C)

    assert PK.verify_ciphertext(*C)

    shares = [sk.decrypt_share(*C) for sk in SKs]
    for i,share in enumerate(shares):
        assert PK.verify_share(i, share, *C)

    SS = list(range(PK.l))
    for i in range(1):
        random.shuffle(SS)
        S = set(SS[:PK.k])
        
        m_ = PK.combine_shares(*C, dict((s,shares[s]) for s in S))
        assert m_ == m

def threshenc2():
    # Failure cases
    PK, SKs = dealer(players=100,k=35)

    m = SHA256.new(b'{\"N\":\"ab77b9c6bf5adc7868eba8cb1ce5b4c425017454526b526422416fd4bca638abeafef0565d255295851aa5eb63d65fc02e95c4df9e77ebd5602a05f6d6f907ce61c3364c5795f65a6d0723e7d2073925633e3a392df4aef7ac347aba3ed31ffc44faa2ddd78818050a5f70af5bbbebe1619788779eee2dad256c0366e7eec79d01a3e20992ce742e35b0a49dd35bcc4219d6b7ec3dc6e044746703264d6070fad6f074af7b46f578682e4a058c53606c18826edbf903c4cafa4c511eeec6d8f9d6bd15d43f9ff41ac98e07dcdceaf4b2ad1fdb6d02e8e628aa46f1da0b3eb8c6cf715abcb5cc5bbd60ceaa458df95c121323e9e3c1a3683bcff28187c731df2b748fe48843bc80c57d7db0aaef906d27da6be1ce80a4f7d49da37fe709c3d68a65f40612f07ae693311ffc1424b68bd6600cedaf257aee8b60c3a1b8faaaee40bb4326a64912a9618265b5f8c8cd4efe9ab11a6f296caa4ef7d8ad2315294a3436fbb22a4712ebfdb301391f1a99f5defbcc65e7aba3764fe9c8718b1755113dd4fe350e204654db91653c76b5e9c06a5592cc30e6f5129aa9432880bd46c239a81e8f5e6992476a796354b47438d81e5541cece4b309e5f29a51329c4b98b9752033a99a4c9d7081930765afd81f7b5764c37bcd988dee66763897e24ec1f3577f7228b3e86a011018d34b1abeb09db971fbccef8b0c1e5ad4c70f560339e9b\",\"T\":300,\"pi\":\"a711952a00efe110ed6615bc2f4ae38435d9fa77a20a4bff8f2fa709ad3d16373ece52851901e926d0cb89b151fd1faea5cbad42274179ea268ccc4ad8bd142ac9c7ede4869ed36c7c0b59c30ec7c93d681cac7c85701adf75b89a708c5ce36816cde2113b9434f9003ecbb69fbd601510cfcfd6199c92aadbfc8859ac944b979e1df9daa558505f8e3cd3b4136d8ca52a944f8cb7ff4a6c4651f3404b322ae3a143a96a0ba111e25c11c9bd9a22a041e6be3db3ab0bae00cec607712578004a472c523826e47c6dbd773f88bb9e3afe038aeb1c2cbd4277ec7e581a69208ae5618c63f19959867beb257ca13197e3acc87b7b0ae4f175e4fd2150d2179bc8e60ee373a39d472f1732e09f76e13faa26fc1470ac54b59acf73afc16877a1b3046af0b31ca5c7e9796b04bd96474a2575caa5217c5614988c4e2aaa5bbc388c02ef4d02f8bd93df800f2218874292a5702b123bdaafcbba449a08ffbc15ffb871b5e1d73b09e39466ed399d3bb53cc24f89f1d4f7713b8fe2e6fa359fb35985c29eb5983349eb1300a9c37ade7d1f260653321a439176e9912aadc4a15a04c79d9a1d9bc8180aa84c4649b427181eaa95117c699d4bf4898c3ef5fb248c81f3d4564813786ae03b0de0abd11d074f3c935e2afd3f2df3d6cc5aedfadcb67f699cc8cc0e3a0c4632932e9d61cec73d69fceaf4e35f72d6ea42082c2eb27a674636\",\"nextprime_l\":\"d747a852e9f4d35b5c1eb76609e8a93e7a9aaab2d2082c4af6209a2be1474d19\",\"identity\":\"6a4e569f05ae9c604012b146cbd16e3f1402dcdc28391538428325480418c84c\"}').digest()
    C = PK.encrypt(m)

    assert PK.verify_ciphertext(*C)

    shares = [sk.decrypt_share(*C) for sk in SKs]
    for i,share in enumerate(shares):
        assert PK.verify_share(i, share, *C)

    SS = list(range(PK.l))
    random.shuffle(SS)
    # Perturb one of the keys
    shares[SS[0]] += shares[SS[0]]
    S = set(SS[:PK.k])
    # print(S)
    try:
        m_ = PK.combine_shares(*C, dict((s,shares[s]) for s in S))
        assert m_ == m
    except AssertionError: pass
    else: assert False, "Combine shares should have raised an error"


import time
if __name__ == "__main__":
            # print("main")
            T1 = time.time()
            threshenc1()
            T2 = time.time()
            print('testthreshec1 running time:%sms' % ((T2 - T1) * 1000))
            T1 = time.time()
            threshenc2()
            T2 = time.time()
            print('testthreshec2 running time:%sms' % ((T2 - T1) * 1000))
