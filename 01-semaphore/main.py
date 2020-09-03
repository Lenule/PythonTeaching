from time import sleep
from semaphore import Semaphore

semaphore = Semaphore()
semaphore.start()

sleep(0.5)
