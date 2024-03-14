import threading
import time
st=time.time()
def test(i):
    time.sleep(i)
    print("hell")
for i in range(100):
    t1 = threading.Thread(target=test, args=(i,))
    t1.start()
t1.join()
print(time.time()-st)