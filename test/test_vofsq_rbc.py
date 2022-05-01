import random
import gevent
from gevent import Greenlet
from gevent.queue import Queue
from pytest import mark, raises
from honeybadgerbft.core.reliablebroadcast import reliablebroadcast, reliablebroadcast_change, encode, decode
from honeybadgerbft.core.reliablebroadcast import hash, merkleTree, getMerkleBranch, merkleVerify



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
            print ('SEND %8s [%2d -> %2d] %.2f' % (o[0], i, j, delay))
            gevent.spawn_later(delay, queues[j].put, (i,o))
            #queues[j].put((i, o))
        return _send

    def makeRecv(j):
        def _recv():
            (i,o) = queues[j].get()
            print ('RECV %8s [%2d -> %2d]' % (o[0], i, j))
            return (i,o)
        return _recv

    return ([makeSend(i) for i in range(N)],
            [makeRecv(j) for j in range(N)])

def test_vofsq_rbc1(sid, i, N, f, leader, input, recvs, sends):
    # Test everything when runs are OK
    #if seed is not None: print 'SEED:', seed

    leader_input = Queue(1)
    for i in range(N):
        input = leader_input.get if i == leader else None
        t = Greenlet(reliablebroadcast_change, sid, i, N, f, leader, input, recvs[i], sends[i])
        t.start()
        threads.append(t)

    # m = b"Hello! This is a test message."
    leader_input.put(ch)
    gevent.joinall(threads)
    # assert [t.value for t in threads] == [ch]*N




def test_challenge(N=4, f=1, leader=None, seed=None, ch = b"12345678901234567890123456789012"):
    sid = 'sidA'
    rnd = random.Random(seed)
    router_seed = rnd.random()
    if leader is None: leader = rnd.randint(0, N - 1)
    sends, recvs = simple_router(N, seed=seed)
    threads = []
    leader_input = Queue(1)

    for i in range(N):
        sends(i, ch)

    while True:  # main receive loop
        sender, msg = receive()
        if msg[0] == 'challenge' and fromLeader is None:
            print("challenge")

    # for i in range(N):
    #     input = leader_input.get if i == leader else None
    #     t = Greenlet(test_vofsq_rbc1, sid, i, N, f, leader, input, recvs[i], sends[i])
    #     t.start()
    #     threads.append(t)
    #
    # leader_input.put(ch)
    # gevent.joinall(threads)
    # assert [t.value for t in threads] == [ch]*N






if __name__ == "__main__":
    print("main")
    seed = range(20)
    test_challenge(10, 1, None, seed)