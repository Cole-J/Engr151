import _thread
from time import sleep

global th
th = True

def s1():
    while th:
        print("s1")
        sleep(1)
_thread.start_new_thread(s1, ())
def s2():
    while th:
        print("s2")
        sleep(1)
_thread.start_new_thread(s2, ())
def s3():
    while th:
        print("s3")
        sleep(1)
_thread.start_new_thread(s3, ())
def s4():
    while th:
        print("s4")
        sleep(1)
_thread.start_new_thread(s4, ())

for x in range(10):
    print(x)
    sleep(2)
th = False
sleep(2)
print("stopped")