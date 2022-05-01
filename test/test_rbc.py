import random

import gevent
from gevent import Greenlet
from gevent.queue import Queue
from pytest import mark, raises
import uuid


from ctypes import cdll
import ctypes
import datetime
import time

from honeybadgerbft.core.reliablebroadcast import reliablebroadcast, reliablebroadcast_change,reliablebroadcast1, encode, decode
from honeybadgerbft.core.reliablebroadcast import hash, merkleTree, getMerkleBranch, merkleVerify

from ctypes import cdll

### Merkle tree
def test_merkletree0():
    mt = merkleTree(["hello"])
    assert mt == [b'', hash("hello")]

def test_merkletree1():
    strList = ["hello","hi","ok"]
    mt = merkleTree(strList)
    roothash = mt[1]
    assert len(mt) == 8
    for i in range(3):
        val = strList[i]
        branch = getMerkleBranch(i, mt)
        assert merkleVerify(3, val, roothash, branch, i)

### Zfec
def test_zfec1():
    K = 3
    N = 10
    m = b"hello this is a test string"
    stripes = encode(K, N, m)
    assert decode(K, N, stripes) == m
    _s = list(stripes)
    # Test by setting some to None
    _s[0] = _s[1] = _s[4] = _s[5] = _s[6] = None
    assert decode(K, N, _s) == m
    _s[3] = _s[7] = None
    assert decode(K, N, _s) == m
    _s[8] = None
    with raises(ValueError) as exc:
        decode(K, N, _s)
    assert exc.value.args[0] == 'Too few to recover'

### RBC
def simple_router(N, maxdelay=0.01, seed=None):
    """Builds a set of connected channels, with random delay
    @return (receives, sends)
    """
    rnd = random.Random(seed)
    #if seed is not None: print 'ROUTER SEED: %f' % (seed,)

    queues = [Queue() for _ in range(N)]

    def makeSend(i):
        def _send(j, o):
            delay = rnd.random() * maxdelay
            #print 'SEND %8s [%2d -> %2d] %.2f' % (o[0], i, j, delay)
            gevent.spawn_later(delay, queues[j].put, (i,o))
            #queues[j].put((i, o))
        return _send

    def makeRecv(j):
        def _recv():
            (i,o) = queues[j].get()
            #print 'RECV %8s [%2d -> %2d]' % (o[0], i, j)
            return (i,o)
        return _recv

    return ([makeSend(i) for i in range(N)],
            [makeRecv(j) for j in range(N)])


def byzantine_router(N, maxdelay=0.01, seed=None, **byzargs):
    """Builds a set of connected channels, with random delay,
    and possibly byzantine behavior.
    """
    rnd = random.Random(seed)
    queues = [Queue() for _ in range(N)]

    def makeSend(i):
        def _send(j, o):
            delay = rnd.random() * maxdelay
            if i == byzargs.get('byznode'):
                if o[0] == byzargs.get('message_type'):
                    screwed_up = list(o)
                    if o[0] in ('VAL', 'ECHO'):
                        screwed_up[3] = 'screw it'
                    o = tuple(screwed_up)
            if byzargs.get('invalid_message_type'):
                byz_o = list(o)
                byz_o[0] = byzargs.get('invalid_message_type')
                o = tuple(byz_o)
            if (byzargs.get('fake_sender') and
                    o[0] == 'VAL' and i == byzargs.get('byznode')):
                gevent.spawn_later(delay, queues[j].put, ((i + 1) % 4, o))
            elif byzargs.get('slow_echo') and i != 2:
                if o[0] == 'READY':
                    gevent.spawn_later(delay*0.001, queues[j].put, (i, o))
                elif o[0] == 'ECHO':
                    gevent.spawn_later(delay*10, queues[j].put, (i, o))
                else:
                    gevent.spawn_later(delay, queues[j].put, (i, o))
            else:
                gevent.spawn_later(delay, queues[j].put, (i, o))
            if byzargs.get('redundant_message_type') == o[0]:
                gevent.spawn_later(delay, queues[j].put, (i, o))

        return _send

    def makeRecv(j):
        def _recv():
            i, o = queues[j].get()
            return i ,o
        return _recv

    return ([makeSend(i) for i in range(N)],
            [makeRecv(j) for j in range(N)])



def _test_rbc1_org(N=4, f=1, leader=None, seed=None):
    # Test everything when runs are OK
    # if seed is not None: print 'SEED:', seed
    sid = 'sidA'
    rnd = random.Random(seed)
    router_seed = rnd.random()
    if leader is None: leader = rnd.randint(0, N - 1)
    sends, recvs = simple_router(N, seed=seed)
    threads = []
    leader_input = Queue(1)
    print("leader is ",leader)
    for i in range(N):
        input = leader_input.get if i == leader else None
        t = Greenlet(reliablebroadcast, sid, i, N, f, leader, input, recvs[i], sends[i])
        t.start()
        threads.append(t)

    m = b"{\"N\":\"ab77b9c6bf5adc7868eba8cb1ce5b4c425017454526b526422416fd4bca638abeafef0565d255295851aa5eb63d65fc02e95c4df9e77ebd5602a05f6d6f907ce61c3364c5795f65a6d0723e7d2073925633e3a392df4aef7ac347aba3ed31ffc44faa2ddd78818050a5f70af5bbbebe1619788779eee2dad256c0366e7eec79d01a3e20992ce742e35b0a49dd35bcc4219d6b7ec3dc6e044746703264d6070fad6f074af7b46f578682e4a058c53606c18826edbf903c4cafa4c511eeec6d8f9d6bd15d43f9ff41ac98e07dcdceaf4b2ad1fdb6d02e8e628aa46f1da0b3eb8c6cf715abcb5cc5bbd60ceaa458df95c121323e9e3c1a3683bcff28187c731df2b748fe48843bc80c57d7db0aaef906d27da6be1ce80a4f7d49da37fe709c3d68a65f40612f07ae693311ffc1424b68bd6600cedaf257aee8b60c3a1b8faaaee40bb4326a64912a9618265b5f8c8cd4efe9ab11a6f296caa4ef7d8ad2315294a3436fbb22a4712ebfdb301391f1a99f5defbcc65e7aba3764fe9c8718b1755113dd4fe350e204654db91653c76b5e9c06a5592cc30e6f5129aa9432880bd46c239a81e8f5e6992476a796354b47438d81e5541cece4b309e5f29a51329c4b98b9752033a99a4c9d7081930765afd81f7b5764c37bcd988dee66763897e24ec1f3577f7228b3e86a011018d34b1abeb09db971fbccef8b0c1e5ad4c70f560339e9b\",\"T\":300,\"pi\":\"a711952a00efe110ed6615bc2f4ae38435d9fa77a20a4bff8f2fa709ad3d16373ece52851901e926d0cb89b151fd1faea5cbad42274179ea268ccc4ad8bd142ac9c7ede4869ed36c7c0b59c30ec7c93d681cac7c85701adf75b89a708c5ce36816cde2113b9434f9003ecbb69fbd601510cfcfd6199c92aadbfc8859ac944b979e1df9daa558505f8e3cd3b4136d8ca52a944f8cb7ff4a6c4651f3404b322ae3a143a96a0ba111e25c11c9bd9a22a041e6be3db3ab0bae00cec607712578004a472c523826e47c6dbd773f88bb9e3afe038aeb1c2cbd4277ec7e581a69208ae5618c63f19959867beb257ca13197e3acc87b7b0ae4f175e4fd2150d2179bc8e60ee373a39d472f1732e09f76e13faa26fc1470ac54b59acf73afc16877a1b3046af0b31ca5c7e9796b04bd96474a2575caa5217c5614988c4e2aaa5bbc388c02ef4d02f8bd93df800f2218874292a5702b123bdaafcbba449a08ffbc15ffb871b5e1d73b09e39466ed399d3bb53cc24f89f1d4f7713b8fe2e6fa359fb35985c29eb5983349eb1300a9c37ade7d1f260653321a439176e9912aadc4a15a04c79d9a1d9bc8180aa84c4649b427181eaa95117c699d4bf4898c3ef5fb248c81f3d4564813786ae03b0de0abd11d074f3c935e2afd3f2df3d6cc5aedfadcb67f699cc8cc0e3a0c4632932e9d61cec73d69fceaf4e35f72d6ea42082c2eb27a674636\",\"nextprime_l\":\"d747a852e9f4d35b5c1eb76609e8a93e7a9aaab2d2082c4af6209a2be1474d19\",\"identity\":\"6a4e569f05ae9c604012b146cbd16e3f1402dcdc28391538428325480418c84c\"\"N\":\"ab77b9c6bf5adc7868eba8cb1ce5b4c425017454526b526422416fd4bca638abeafef0565d255295851aa5eb63d65fc02e95c4df9e77ebd5602a05f6d6f907ce61c3364c5795f65a6d0723e7d2073925633e3a392df4aef7ac347aba3ed31ffc44faa2ddd78818050a5f70af5bbbebe1619788779eee2dad256c0366e7eec79d01a3e20992ce742e35b0a49dd35bcc4219d6b7ec3dc6e044746703264d6070fad6f074af7b46f578682e4a058c53606c18826edbf903c4cafa4c511eeec6d8f9d6bd15d43f9ff41ac98e07dcdceaf4b2ad1fdb6d02e8e628aa46f1da0b3eb8c6cf715abcb5cc5bbd60ceaa458df95c121323e9e3c1a3683bcff28187c731df2b748fe48843bc80c57d7db0aaef906d27da6be1ce80a4f7d49da37fe709c3d68a65f40612f07ae693311ffc1424b68bd6600cedaf257aee8b60c3a1b8faaaee40bb4326a64912a9618265b5f8c8cd4efe9ab11a6f296caa4ef7d8ad2315294a3436fbb22a4712ebfdb301391f1a99f5defbcc65e7aba3764fe9c8718b1755113dd4fe350e204654db91653c76b5e9c06a5592cc30e6f5129aa9432880bd46c239a81e8f5e6992476a796354b47438d81e5541cece4b309e5f29a51329c4b98b9752033a99a4c9d7081930765afd81f7b5764c37bcd988dee66763897e24ec1f3577f7228b3e86a011018d34b1abeb09db971fbccef8b0c1e5ad4c70f560339e9b\",\"T\":300,\"pi\":\"a711952a00efe110ed6615bc2f4ae38435d9fa77a20a4bff8f2fa709ad3d16373ece52851901e926d0cb89b151fd1faea5cbad42274179ea268ccc4ad8bd142ac9c7ede4869ed36c7c0b59c30ec7c93d681cac7c85701adf75b89a708c5ce36816cde2113b9434f9003ecbb69fbd601510cfcfd6199c92aadbfc8859ac944b979e1df9daa558505f8e3cd3b4136d8ca52a944f8cb7ff4a6c4651f3404b322ae3a143a96a0ba111e25c11c9bd9a22a041e6be3db3ab0bae00cec607712578004a472c523826e47c6dbd773f88bb9e3afe038aeb1c2cbd4277ec7e581a69208ae5618c63f19959867beb257ca13197e3acc87b7b0ae4f175e4fd2150d2179bc8e60ee373a39d472f1732e09f76e13faa26fc1470ac54b59acf73afc16877a1b3046af0b31ca5c7e9796b04bd96474a2575caa5217c5614988c4e2aaa5bbc388c02ef4d02f8bd93df800f2218874292a5702b123bdaafcbba449a08ffbc15ffb871b5e1d73b09e39466ed399d3bb53cc24f89f1d4f7713b8fe2e6fa359fb35985c29eb5983349eb1300a9c37ade7d1f260653321a439176e9912aadc4a15a04c79d9a1d9bc8180aa84c4649b427181eaa95117c699d4bf4898c3ef5fb248c81f3d4564813786ae03b0de0abd11d074f3c935e2afd3f2df3d6cc5aedfadcb67f699cc8cc0e3a0c4632932e9d61cec73d69fceaf4e35f72d6ea42082c2eb27a674636\",\"nextprime_l\":\"d747a852e9f4d35b5c1eb76609e8a93e7a9aaab2d2082c4af6209a2be1474d19\",\"identity\":\"6a4e569f05ae9c604012b146cbd16e3f1402dcdc28391538428325480418c84c\}{\"N\":\"ab77b9c6bf5adc7868eba8cb1ce5b4c425017454526b526422416fd4bca638abeafef0565d255295851aa5eb63d65fc02e95c4df9e77ebd5602a05f6d6f907ce61c3364c5795f65a6d0723e7d2073925633e3a392df4aef7ac347aba3ed31ffc44faa2ddd78818050a5f70af5bbbebe1619788779eee2dad256c0366e7eec79d01a3e20992ce742e35b0a49dd35bcc4219d6b7ec3dc6e044746703264d6070fad6f074af7b46f578682e4a058c53606c18826edbf903c4cafa4c511eeec6d8f9d6bd15d43f9ff41ac98e07dcdceaf4b2ad1fdb6d02e8e628aa46f1da0b3eb8c6cf715abcb5cc5bbd60ceaa458df95c121323e9e3c1a3683bcff28187c731df2b748fe48843bc80c57d7db0aaef906d27da6be1ce80a4f7d49da37fe709c3d68a65f40612f07ae693311ffc1424b68bd6600cedaf257aee8b60c3a1b8faaaee40bb4326a64912a9618265b5f8c8cd4efe9ab11a6f296caa4ef7d8ad2315294a3436fbb22a4712ebfdb301391f1a99f5defbcc65e7aba3764fe9c8718b1755113dd4fe350e204654db91653c76b5e9c06a5592cc30e6f5129aa9432880bd46c239a81e8f5e6992476a796354b47438d81e5541cece4b309e5f29a51329c4b98b9752033a99a4c9d7081930765afd81f7b5764c37bcd988dee66763897e24ec1f3577f7228b3e86a011018d34b1abeb09db971fbccef8b0c1e5ad4c70f560339e9b\",\"T\":300,\"pi\":\"a711952a00efe110ed6615bc2f4ae38435d9fa77a20a4bff8f2fa709ad3d16373ece52851901e926d0cb89b151fd1faea5cbad42274179ea268ccc4ad8bd142ac9c7ede4869ed36c7c0b59c30ec7c93d681cac7c85701adf75b89a708c5ce36816cde2113b9434f9003ecbb69fbd601510cfcfd6199c92aadbfc8859ac944b979e1df9daa558505f8e3cd3b4136d8ca52a944f8cb7ff4a6c4651f3404b322ae3a143a96a0ba111e25c11c9bd9a22a041e6be3db3ab0bae00cec607712578004a472c523826e47c6dbd773f88bb9e3afe038aeb1c2cbd4277ec7e581a69208ae5618c63f19959867beb257ca13197e3acc87b7b0ae4f175e4fd2150d2179bc8e60ee373a39d472f1732e09f76e13faa26fc1470ac54b59acf73afc16877a1b3046af0b31ca5c7e9796b04bd96474a2575caa5217c5614988c4e2aaa5bbc388c02ef4d02f8bd93df800f2218874292a5702b123bdaafcbba449a08ffbc15ffb871b5e1d73b09e39466ed399d3bb53cc24f89f1d4f7713b8fe2e6fa359fb35985c29eb5983349eb1300a9c37ade7d1f260653321a439176e9912aadc4a15a04c79d9a1d9bc8180aa84c4649b427181eaa95117c699d4bf4898c3ef5fb248c81f3d4564813786ae03b0de0abd11d074f3c935e2afd3f2df3d6cc5aedfadcb67f699cc8cc0e3a0c4632932e9d61cec73d69fceaf4e35f72d6ea42082c2eb27a674636\",\"nextprime_l\":\"d747a852e9f4d35b5c1eb76609e8a93e7a9aaab2d2082c4af6209a2be1474d19\",\"identity\":\"6a4e569f05ae9c604012b146cbd16e3f1402dcdc28391538428325480418c84c\"\"N\":\"ab77b9c6bf5adc7868eba8cb1ce5b4c425017454526b526422416fd4bca638abeafef0565d255295851aa5eb63d65fc02e95c4df9e77ebd5602a05f6d6f907ce61c3364c5795f65a6d0723e7d2073925633e3a392df4aef7ac347aba3ed31ffc44faa2ddd78818050a5f70af5bbbebe1619788779eee2dad256c0366e7eec79d01a3e20992ce742e35b0a49dd35bcc4219d6b7ec3dc6e044746703264d6070fad6f074af7b46f578682e4a058c53606c18826edbf903c4cafa4c511eeec6d8f9d6bd15d43f9ff41ac98e07dcdceaf4b2ad1fdb6d02e8e628aa46f1da0b3eb8c6cf715abcb5cc5bbd60ceaa458df95c121323e9e3c1a3683bcff28187c731df2b748fe48843bc80c57d7db0aaef906d27da6be1ce80a4f7d49da37fe709c3d68a65f40612f07ae693311ffc1424b68bd6600cedaf257aee8b60c3a1b8faaaee40bb4326a64912a9618265b5f8c8cd4efe9ab11a6f296caa4ef7d8ad2315294a3436fbb22a4712ebfdb301391f1a99f5defbcc65e7aba3764fe9c8718b1755113dd4fe350e204654db91653c76b5e9c06a5592cc30e6f5129aa9432880bd46c239a81e8f5e6992476a796354b47438d81e5541cece4b309e5f29a51329c4b98b9752033a99a4c9d7081930765afd81f7b5764c37bcd988dee66763897e24ec1f3577f7228b3e86a011018d34b1abeb09db971fbccef8b0c1e5ad4c70f560339e9b\",\"T\":300,\"pi\":\"a711952a00efe110ed6615bc2f4ae38435d9fa77a20a4bff8f2fa709ad3d16373ece52851901e926d0cb89b151fd1faea5cbad42274179ea268ccc4ad8bd142ac9c7ede4869ed36c7c0b59c30ec7c93d681cac7c85701adf75b89a708c5ce36816cde2113b9434f9003ecbb69fbd601510cfcfd6199c92aadbfc8859ac944b979e1df9daa558505f8e3cd3b4136d8ca52a944f8cb7ff4a6c4651f3404b322ae3a143a96a0ba111e25c11c9bd9a22a041e6be3db3ab0bae00cec607712578004a472c523826e47c6dbd773f88bb9e3afe038aeb1c2cbd4277ec7e581a69208ae5618c63f19959867beb257ca13197e3acc87b7b0ae4f175e4fd2150d2179bc8e60ee373a39d472f1732e09f76e13faa26fc1470ac54b59acf73afc16877a1b3046af0b31ca5c7e9796b04bd96474a2575caa5217c5614988c4e2aaa5bbc388c02ef4d02f8bd93df800f2218874292a5702b123bdaafcbba449a08ffbc15ffb871b5e1d73b09e39466ed399d3bb53cc24f89f1d4f7713b8fe2e6fa359fb35985c29eb5983349eb1300a9c37ade7d1f260653321a439176e9912aadc4a15a04c79d9a1d9bc8180aa84c4649b427181eaa95117c699d4bf4898c3ef5fb248c81f3d4564813786ae03b0de0abd11d074f3c935e2afd3f2df3d6cc5aedfadcb67f699cc8cc0e3a0c4632932e9d61cec73d69fceaf4e35f72d6ea42082c2eb27a674636\",\"nextprime_l\":\"d747a852e9f4d35b5c1eb76609e8a93e7a9aaab2d2082c4af6209a2be1474d19\",\"identity\":\"6a4e569f05ae9c604012b146cbd16e3f1402dcdc28391538428325480418c84c\}{\"N\":\"ab77b9c6bf5adc7868eba8cb1ce5b4c425017454526b526422416fd4bca638abeafef0565d255295851aa5eb63d65fc02e95c4df9e77ebd5602a05f6d6f907ce61c3364c5795f65a6d0723e7d2073925633e3a392df4aef7ac347aba3ed31ffc44faa2ddd78818050a5f70af5bbbebe1619788779eee2dad256c0366e7eec79d01a3e20992ce742e35b0a49dd35bcc4219d6b7ec3dc6e044746703264d6070fad6f074af7b46f578682e4a058c53606c18826edbf903c4cafa4c511eeec6d8f9d6bd15d43f9ff41ac98e07dcdceaf4b2ad1fdb6d02e8e628aa46f1da0b3eb8c6cf715abcb5cc5bbd60ceaa458df95c121323e9e3c1a3683bcff28187c731df2b748fe48843bc80c57d7db0aaef906d27da6be1ce80a4f7d49da37fe709c3d68a65f40612f07ae693311ffc1424b68bd6600cedaf257aee8b60c3a1b8faaaee40bb4326a64912a9618265b5f8c8cd4efe9ab11a6f296caa4ef7d8ad2315294a3436fbb22a4712ebfdb301391f1a99f5defbcc65e7aba3764fe9c8718b1755113dd4fe350e204654db91653c76b5e9c06a5592cc30e6f5129aa9432880bd46c239a81e8f5e6992476a796354b47438d81e5541cece4b309e5f29a51329c4b98b9752033a99a4c9d7081930765afd81f7b5764c37bcd988dee66763897e24ec1f3577f7228b3e86a011018d34b1abeb09db971fbccef8b0c1e5ad4c70f560339e9b\",\"T\":300,\"pi\":\"a711952a00efe110ed6615bc2f4ae38435d9fa77a20a4bff8f2fa709ad3d16373ece52851901e926d0cb89b151fd1faea5cbad42274179ea268ccc4ad8bd142ac9c7ede4869ed36c7c0b59c30ec7c93d681cac7c85701adf75b89a708c5ce36816cde2113b9434f9003ecbb69fbd601510cfcfd6199c92aadbfc8859ac944b979e1df9daa558505f8e3cd3b4136d8ca52a944f8cb7ff4a6c4651f3404b322ae3a143a96a0ba111e25c11c9bd9a22a041e6be3db3ab0bae00cec607712578004a472c523826e47c6dbd773f88bb9e3afe038aeb1c2cbd4277ec7e581a69208ae5618c63f19959867beb257ca13197e3acc87b7b0ae4f175e4fd2150d2179bc8e60ee373a39d472f1732e09f76e13faa26fc1470ac54b59acf73afc16877a1b3046af0b31ca5c7e9796b04bd96474a2575caa5217c5614988c4e2aaa5bbc388c02ef4d02f8bd93df800f2218874292a5702b123bdaafcbba449a08ffbc15ffb871b5e1d73b09e39466ed399d3bb53cc24f89f1d4f7713b8fe2e6fa359fb35985c29eb5983349eb1300a9c37ade7d1f260653321a439176e9912aadc4a15a04c79d9a1d9bc8180aa84c4649b427181eaa95117c699d4bf4898c3ef5fb248c81f3d4564813786ae03b0de0abd11d074f3c935e2afd3f2df3d6cc5aedfadcb67f699cc8cc0e3a0c4632932e9d61cec73d69fceaf4e35f72d6ea42082c2eb27a674636\",\"nextprime_l\":\"d747a852e9f4d35b5c1eb76609e8a93e7a9aaab2d2082c4af6209a2be1474d19\",\"identity\":\"6a4e569f05ae9c604012b146cbd16e3f1402dcdc28391538428325480418c84c\"\"N\":\"ab77b9c6bf5adc7868eba8cb1ce5b4c425017454526b526422416fd4bca638abeafef0565d255295851aa5eb63d65fc02e95c4df9e77ebd5602a05f6d6f907ce61c3364c5795f65a6d0723e7d2073925633e3a392df4aef7ac347aba3ed31ffc44faa2ddd78818050a5f70af5bbbebe1619788779eee2dad256c0366e7eec79d01a3e20992ce742e35b0a49dd35bcc4219d6b7ec3dc6e044746703264d6070fad6f074af7b46f578682e4a058c53606c18826edbf903c4cafa4c511eeec6d8f9d6bd15d43f9ff41ac98e07dcdceaf4b2ad1fdb6d02e8e628aa46f1da0b3eb8c6cf715abcb5cc5bbd60ceaa458df95c121323e9e3c1a3683bcff28187c731df2b748fe48843bc80c57d7db0aaef906d27da6be1ce80a4f7d49da37fe709c3d68a65f40612f07ae693311ffc1424b68bd6600cedaf257aee8b60c3a1b8faaaee40bb4326a64912a9618265b5f8c8cd4efe9ab11a6f296caa4ef7d8ad2315294a3436fbb22a4712ebfdb301391f1a99f5defbcc65e7aba3764fe9c8718b1755113dd4fe350e204654db91653c76b5e9c06a5592cc30e6f5129aa9432880bd46c239a81e8f5e6992476a796354b47438d81e5541cece4b309e5f29a51329c4b98b9752033a99a4c9d7081930765afd81f7b5764c37bcd988dee66763897e24ec1f3577f7228b3e86a011018d34b1abeb09db971fbccef8b0c1e5ad4c70f560339e9b\",\"T\":300,\"pi\":\"a711952a00efe110ed6615bc2f4ae38435d9fa77a20a4bff8f2fa709ad3d16373ece52851901e926d0cb89b151fd1faea5cbad42274179ea268ccc4ad8bd142ac9c7ede4869ed36c7c0b59c30ec7c93d681cac7c85701adf75b89a708c5ce36816cde2113b9434f9003ecbb69fbd601510cfcfd6199c92aadbfc8859ac944b979e1df9daa558505f8e3cd3b4136d8ca52a944f8cb7ff4a6c4651f3404b322ae3a143a96a0ba111e25c11c9bd9a22a041e6be3db3ab0bae00cec607712578004a472c523826e47c6dbd773f88bb9e3afe038aeb1c2cbd4277ec7e581a69208ae5618c63f19959867beb257ca13197e3acc87b7b0ae4f175e4fd2150d2179bc8e60ee373a39d472f1732e09f76e13faa26fc1470ac54b59acf73afc16877a1b3046af0b31ca5c7e9796b04bd96474a2575caa5217c5614988c4e2aaa5bbc388c02ef4d02f8bd93df800f2218874292a5702b123bdaafcbba449a08ffbc15ffb871b5e1d73b09e39466ed399d3bb53cc24f89f1d4f7713b8fe2e6fa359fb35985c29eb5983349eb1300a9c37ade7d1f260653321a439176e9912aadc4a15a04c79d9a1d9bc8180aa84c4649b427181eaa95117c699d4bf4898c3ef5fb248c81f3d4564813786ae03b0de0abd11d074f3c935e2afd3f2df3d6cc5aedfadcb67f699cc8cc0e3a0c4632932e9d61cec73d69fceaf4e35f72d6ea42082c2eb27a674636\",\"nextprime_l\":\"d747a852e9f4d35b5c1eb76609e8a93e7a9aaab2d2082c4af6209a2be1474d19\",\"identity\":\"6a4e569f05ae9c604012b146cbd16e3f1402dcdc28391538428325480418c84c\}{\"N\":\"ab77b9c6bf5adc7868eba8cb1ce5b4c425017454526b526422416fd4bca638abeafef0565d255295851aa5eb63d65fc02e95c4df9e77ebd5602a05f6d6f907ce61c3364c5795f65a6d0723e7d2073925633e3a392df4aef7ac347aba3ed31ffc44faa2ddd78818050a5f70af5bbbebe1619788779eee2dad256c0366e7eec79d01a3e20992ce742e35b0a49dd35bcc4219d6b7ec3dc6e044746703264d6070fad6f074af7b46f578682e4a058c53606c18826edbf903c4cafa4c511eeec6d8f9d6bd15d43f9ff41ac98e07dcdceaf4b2ad1fdb6d02e8e628aa46f1da0b3eb8c6cf715abcb5cc5bbd60ceaa458df95c121323e9e3c1a3683bcff28187c731df2b748fe48843bc80c57d7db0aaef906d27da6be1ce80a4f7d49da37fe709c3d68a65f40612f07ae693311ffc1424b68bd6600cedaf257aee8b60c3a1b8faaaee40bb4326a64912a9618265b5f8c8cd4efe9ab11a6f296caa4ef7d8ad2315294a3436fbb22a4712ebfdb301391f1a99f5defbcc65e7aba3764fe9c8718b1755113dd4fe350e204654db91653c76b5e9c06a5592cc30e6f5129aa9432880bd46c239a81e8f5e6992476a796354b47438d81e5541cece4b309e5f29a51329c4b98b9752033a99a4c9d7081930765afd81f7b5764c37bcd988dee66763897e24ec1f3577f7228b3e86a011018d34b1abeb09db971fbccef8b0c1e5ad4c70f560339e9b\",\"T\":300,\"pi\":\"a711952a00efe110ed6615bc2f4ae38435d9fa77a20a4bff8f2fa709ad3d16373ece52851901e926d0cb89b151fd1faea5cbad42274179ea268ccc4ad8bd142ac9c7ede4869ed36c7c0b59c30ec7c93d681cac7c85701adf75b89a708c5ce36816cde2113b9434f9003ecbb69fbd601510cfcfd6199c92aadbfc8859ac944b979e1df9daa558505f8e3cd3b4136d8ca52a944f8cb7ff4a6c4651f3404b322ae3a143a96a0ba111e25c11c9bd9a22a041e6be3db3ab0bae00cec607712578004a472c523826e47c6dbd773f88bb9e3afe038aeb1c2cbd4277ec7e581a69208ae5618c63f19959867beb257ca13197e3acc87b7b0ae4f175e4fd2150d2179bc8e60ee373a39d472f1732e09f76e13faa26fc1470ac54b59acf73afc16877a1b3046af0b31ca5c7e9796b04bd96474a2575caa5217c5614988c4e2aaa5bbc388c02ef4d02f8bd93df800f2218874292a5702b123bdaafcbba449a08ffbc15ffb871b5e1d73b09e39466ed399d3bb53cc24f89f1d4f7713b8fe2e6fa359fb35985c29eb5983349eb1300a9c37ade7d1f260653321a439176e9912aadc4a15a04c79d9a1d9bc8180aa84c4649b427181eaa95117c699d4bf4898c3ef5fb248c81f3d4564813786ae03b0de0abd11d074f3c935e2afd3f2df3d6cc5aedfadcb67f699cc8cc0e3a0c4632932e9d61cec73d69fceaf4e35f72d6ea42082c2eb27a674636\",\"nextprime_l\":\"d747a852e9f4d35b5c1eb76609e8a93e7a9aaab2d2082c4af6209a2be1474d19\",\"identity\":\"6a4e569f05ae9c604012b146cbd16e3f1402dcdc28391538428325480418c84c\"\"N\":\"ab77b9c6bf5adc7868eba8cb1ce5b4c425017454526b526422416fd4bca638abeafef0565d255295851aa5eb63d65fc02e95c4df9e77ebd5602a05f6d6f907ce61c3364c5795f65a6d0723e7d2073925633e3a392df4aef7ac347aba3ed31ffc44faa2ddd78818050a5f70af5bbbebe1619788779eee2dad256c0366e7eec79d01a3e20992ce742e35b0a49dd35bcc4219d6b7ec3dc6e044746703264d6070fad6f074af7b46f578682e4a058c53606c18826edbf903c4cafa4c511eeec6d8f9d6bd15d43f9ff41ac98e07dcdceaf4b2ad1fdb6d02e8e628aa46f1da0b3eb8c6cf715abcb5cc5bbd60ceaa458df95c121323e9e3c1a3683bcff28187c731df2b748fe48843bc80c57d7db0aaef906d27da6be1ce80a4f7d49da37fe709c3d68a65f40612f07ae693311ffc1424b68bd6600cedaf257aee8b60c3a1b8faaaee40bb4326a64912a9618265b5f8c8cd4efe9ab11a6f296caa4ef7d8ad2315294a3436fbb22a4712ebfdb301391f1a99f5defbcc65e7aba3764fe9c8718b1755113dd4fe350e204654db91653c76b5e9c06a5592cc30e6f5129aa9432880bd46c239a81e8f5e6992476a796354b47438d81e5541cece4b309e5f29a51329c4b98b9752033a99a4c9d7081930765afd81f7b5764c37bcd988dee66763897e24ec1f3577f7228b3e86a011018d34b1abeb09db971fbccef8b0c1e5ad4c70f560339e9b\",\"T\":300,\"pi\":\"a711952a00efe110ed6615bc2f4ae38435d9fa77a20a4bff8f2fa709ad3d16373ece52851901e926d0cb89b151fd1faea5cbad42274179ea268ccc4ad8bd142ac9c7ede4869ed36c7c0b59c30ec7c93d681cac7c85701adf75b89a708c5ce36816cde2113b9434f9003ecbb69fbd601510cfcfd6199c92aadbfc8859ac944b979e1df9daa558505f8e3cd3b4136d8ca52a944f8cb7ff4a6c4651f3404b322ae3a143a96a0ba111e25c11c9bd9a22a041e6be3db3ab0bae00cec607712578004a472c523826e47c6dbd773f88bb9e3afe038aeb1c2cbd4277ec7e581a69208ae5618c63f19959867beb257ca13197e3acc87b7b0ae4f175e4fd2150d2179bc8e60ee373a39d472f1732e09f76e13faa26fc1470ac54b59acf73afc16877a1b3046af0b31ca5c7e9796b04bd96474a2575caa5217c5614988c4e2aaa5bbc388c02ef4d02f8bd93df800f2218874292a5702b123bdaafcbba449a08ffbc15ffb871b5e1d73b09e39466ed399d3bb53cc24f89f1d4f7713b8fe2e6fa359fb35985c29eb5983349eb1300a9c37ade7d1f260653321a439176e9912aadc4a15a04c79d9a1d9bc8180aa84c4649b427181eaa95117c699d4bf4898c3ef5fb248c81f3d4564813786ae03b0de0abd11d074f3c935e2afd3f2df3d6cc5aedfadcb67f699cc8cc0e3a0c4632932e9d61cec73d69fceaf4e35f72d6ea42082c2eb27a674636\",\"nextprime_l\":\"d747a852e9f4d35b5c1eb76609e8a93e7a9aaab2d2082c4af6209a2be1474d19\",\"identity\":\"6a4e569f05ae9c604012b146cbd16e3f1402dcdc28391538428325480418c84c\}"
    leader_input.put(m)
    gevent.joinall(threads)
    assert [t.value for t in threads] == [m] * N

def _test_rbc1(N=4, f=1, leader=None, seed=None):
    # Test everything when runs are OK
    #if seed is not None: print 'SEED:', seed

    ch = b"12345678901234567890123456789012"

    sid = 'sidA'
    rnd = random.Random(seed)
    router_seed = rnd.random()
    if leader is None: leader = rnd.randint(0,N-1)
    sends, recvs = simple_router(N, seed=seed)
    threads = []
    leader_input = Queue(1)
    # m = b"Hello! This is a test message.Hello! This is a test message.Hello! This is a test message.Hello! This is a test message.Hello! This is a test message.Hello! This is a test message.Hello! This is a test message.Hello! This is a test message.Hello! This is a test message.Hello! This is a test message.Hello! This is a test message.Hello! This is a test message."


    lib = cdll.LoadLibrary('./libtest-vdf.so')
    path = "/challenge-response protocol/file.txt"
    evidencefilepath = "/home/ss/HoneyBadgerBFT-Python/challenge-response protocol/evidencefile.txt"
    pathencode = path.encode()
    evidencefilepathencode = evidencefilepath.encode()
    # ret1 = lib.init_phase(path, 100)
    # data = ctypes.string_at(ret1, -1).decode("utf-8")
    #
    # print("leader is ", leader)

    ret1 = lib.init_phase(pathencode, evidencefilepathencode, 300)
    data = ctypes.string_at(ret1, -1).decode("utf-8")


    challenge = "12345678901234567890123456789012"
    challengeencode = challenge.encode()
    ret2 = lib.challenge_phase(pathencode, evidencefilepathencode, challengeencode)
    challenge_data = ctypes.string_at(ret2, -1).decode("utf-8")
    print("challenge phase output ", challenge_data)


    # lib = cdll.LoadLibrary('./libtest-vdf.so')
    # ret1 = lib.test()
    # print(ret1)


    for i in range(N):
        input = leader_input.get if i == leader else None
        # mmm = uuid.uuid4().bytes+i.to_bytes(5, 'little')
        # print("mmm is ",mmm)
        # print("type(mmm) is ", type(mmm))
        t = Greenlet(reliablebroadcast_change, sid, i, N, f, leader, input, recvs[i], sends[i]) #sid, pid, N, f, leader, input, receive, send
        # t = Greenlet(reliablebroadcast, sid, i, N, f, leader, input, recvs[i], sends[i])
        t.start()
        threads.append(t)

    leader_input.put(challenge_data)
    gevent.joinall(threads)
    # assert [t.value for t in threads] == [m]*N


@mark.parametrize('seed', range(20))
@mark.parametrize('N,f', ((4, 1), (5, 1), (8, 2)))
def test_rbc1(N, f, seed):
    _test_rbc1(N=N, f=f, seed=seed)


def _test_rbc2(N=4, f=1, leader=None, seed=None):
    # Crash up to f nodes
    #if seed is not None: print 'SEED:', seed
    sid = 'sidA'
    rnd = random.Random(seed)
    router_seed = rnd.random()
    if leader is None: leader = rnd.randint(0,N-1)
    sends, recvs = simple_router(N, seed=router_seed)
    threads = []
    leader_input = Queue(1)

    for i in range(N):
        input = leader_input.get if i == leader else None
        t = Greenlet(reliablebroadcast1, sid, i, N, f, leader, input, recvs[i], sends[i])
        t.start()
        threads.append(t)

    m = b"Hello!asdfasdfasdfasdfasdfsadf"
    leader_input.put(m)
    gevent.sleep(0)  # Let the leader get out its first message

    # Crash f of the nodes
    crashed = set()
    #print 'Leader:', leader
    for _ in range(f):
        i = rnd.choice(range(N))
        crashed.add(i)
        threads[i].kill()
        threads[i].join()
    #print 'Crashed:', crashed
    gevent.joinall(threads)
    for i,t in enumerate(threads):
        if i not in crashed: assert t.value == m


@mark.parametrize('seed', range(20))
@mark.parametrize('N,f', ((4, 1), (5, 1), (8, 2)))
def test_rbc2(N, f, seed):
    _test_rbc2(N=N, f=f, seed=seed)


@mark.parametrize('seed', range(20))
@mark.parametrize('tag', ('VAL', 'ECHO'))
@mark.parametrize('N,f', ((4, 1), (5, 1), (8, 2)))
def test_rbc_when_merkle_verify_fails(N, f, tag, seed):
    rnd = random.Random(seed)
    leader = rnd.randint(0, N-1)
    byznode = 1
    sends, recvs = byzantine_router(
        N, seed=seed, byznode=byznode, message_type=tag)
    threads = []
    leader_input = Queue(1)
    for pid in range(N):
        sid = 'sid{}'.format(leader)
        input = leader_input.get if pid == leader else None
        t = Greenlet(reliablebroadcast, sid, pid, N, f, leader, input, recvs[pid], sends[pid])
        t.start()
        threads.append(t)

    m = b"Hello! This is a test message."
    leader_input.put(m)
    completed_greenlets = gevent.joinall(threads, timeout=0.5)
    expected_rbc_result = None if leader == byznode and tag == 'VAL' else m
    assert all([t.value == expected_rbc_result for t in threads])


@mark.parametrize('seed', range(3))
@mark.parametrize('N,f', ((4, 1), (5, 1), (8, 2)))
def test_rbc_receives_val_from_sender_not_leader(N, f, seed):
    rnd = random.Random(seed)
    leader = rnd.randint(0, N-1)
    sends, recvs = byzantine_router(
        N, seed=seed, fake_sender=True, byznode=leader)
    threads = []
    leader_input = Queue(1)
    for pid in range(N):
        sid = 'sid{}'.format(leader)
        input = leader_input.get if pid == leader else None
        t = Greenlet(reliablebroadcast, sid, pid, N, f, leader, input, recvs[pid], sends[pid])
        t.start()
        threads.append(t)

    m = "Hello! This is a test message."
    leader_input.put(m)
    completed_greenlets = gevent.joinall(threads, timeout=0.5)
    expected_rbc_result = None
    assert all([t.value == expected_rbc_result for t in threads])


@mark.parametrize('seed', range(2))
@mark.parametrize('tag', ('ECHO', 'READY'))
@mark.parametrize('N,f', ((4, 1),))
def test_rbc_with_redundant_message(N, f, tag, seed):
    rnd = random.Random(seed)
    leader = rnd.randint(0, N-1)
    sends, recvs = byzantine_router(N, seed=seed, redundant_message_type=tag)
    threads = []
    leader_input = Queue(1)
    for pid in range(N):
        sid = 'sid{}'.format(leader)
        input = leader_input.get if pid == leader else None
        t = Greenlet(reliablebroadcast, sid, pid, N, f,
                     leader, input, recvs[pid], sends[pid])
        t.start()
        threads.append(t)

    m = b"Hello! This is a test message."
    leader_input.put(m)
    completed_greenlets = gevent.joinall(threads, timeout=0.5)
    expected_rbc_result = m
    assert all([t.value == expected_rbc_result for t in threads])


@mark.parametrize('seed', range(1))
@mark.parametrize('N,f', ((4, 1),))
def test_rbc_decode_in_echo_handling_step(N, f, seed):
    """The goal of this test is to simply force the decode operation
    to take place upon rception of an ECHO message, (when other
    necessary conditions are met), as opposed to the operation taking
    place upon reception of a READY message.

    The test is perhaps hackish at best, but nevertheless does achieve
    its intent.

    The test slows down the broadcasting of ECHO messages, meanwhile
    speeding up the broadcasting of READY messages.
    """
    rnd = random.Random(seed)
    leader = rnd.randint(0, N-1)
    sends, recvs = byzantine_router(N, seed=seed, slow_echo=True)
    threads = []
    leader_input = Queue(1)
    for pid in range(N):
        sid = 'sid{}'.format(leader)
        input = leader_input.get if pid == leader else None
        t = Greenlet(reliablebroadcast, sid, pid, N, f,
                     leader, input, recvs[pid], sends[pid])
        t.start()
        threads.append(t)

    m = b"Hello! This is a test message."
    leader_input.put(m)
    completed_greenlets = gevent.joinall(threads, timeout=1)
    expected_rbc_result = m
    assert all([t.value == expected_rbc_result for t in threads])


@mark.parametrize('seed', range(2))
@mark.parametrize('tag', ('CHECKTHISOUT!', 'LETSGO!'))
@mark.parametrize('N,f', ((4, 1),))
def test_rbc_with_invalid_message(N, f, tag, seed):
    rnd = random.Random(seed)
    leader = rnd.randint(0, N-1)
    sends, recvs = byzantine_router(N, seed=seed, invalid_message_type=tag)
    threads = []
    leader_input = Queue(1)
    for pid in range(N):
        sid = 'sid{}'.format(leader)
        input = leader_input.get if pid == leader else None
        t = Greenlet(reliablebroadcast, sid, pid, N, f,
                     leader, input, recvs[pid], sends[pid])
        t.start()
        threads.append(t)

    m = "Hello! This is a test message."
    leader_input.put(m)
    completed_greenlets = gevent.joinall(threads, timeout=0.5)
    expected_rbc_result = None
    assert all([t.value == expected_rbc_result for t in threads])


# TODO: Test more edge cases, like Byzantine behavior
from collections import defaultdict

if __name__ == "__main__":
            print("main")
            # stripes = defaultdict(lambda: [None for _ in range(5)])
            # stripe = b'12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234'
            # sender = 1
            # stripes[roothash][sender] = stripe

            totalnum = 20
            fffnum=1

            T1 = time.time()
            seed = range(totalnum)

            test_rbc1(totalnum, fffnum, seed)
            T2 = time.time()
            print('testrbc1 running time:%sms' % ((T2 - T1) * 1000))


            T1 = time.time()

            _test_rbc1_org(totalnum, fffnum, None, seed)
            T2 = time.time()
            print('testrbc2 running time:%sms' % ((T2 - T1) * 1000))