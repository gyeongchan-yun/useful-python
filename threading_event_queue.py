import threading
from queue import Queue

evt_q = Queue()


def func():
    number = int(threading.currentThread().getName().split(":")[1])
    if (number < 2):
        evt = threading.Event()
        evt_q.put(evt)
        evt.wait()

    for i in range(10):
        print ("[%d] %d" % (number, i))

    if (number > 2):
        for _ in range(evt_q.qsize()):
            evt = evt_q.get()
            evt.set()


if __name__ == '__main__':
    threads = [threading.Thread(target=func,
                                name="name:%i" % i) for i in range(0, 4)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print ("exit")
