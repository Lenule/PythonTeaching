from time import sleep
from semaphore import Semaphore

semaphore = Semaphore()
semaphore.start()

sleep(0.5)

# semaphore.red.set_state("on")

# sleep(2)

# semaphore.yellow.set_state("on")

# sleep (1)

# semaphore.red.set_state("off")

# semaphore.yellow.set_state ("off")

# semaphore.green.set_state ("on")

# sleep (2)

# semaphore.green.set_state ("off")

# semaphore.yellow.set_state ("on")

# sleep (1)

# semaphore.yellow.set_state ("off")

# semaphore.red.set_state ("on")

# sleep (1)

# semaphore.red.set_state ("off")


# 1) realisticky semafor (casove)
# 2) zabavna sekvence


semaphore.red.set_state("on")

sleep (4)

semaphore.yellow.set_state ("on")

sleep (3)

semaphore.red.set_state ("off")

semaphore.yellow.set_state ("off")

semaphore.green.set_state ("on")

sleep (5)

semaphore.green.set_state ("off")

semaphore.yellow.set_state ("on")

sleep (3)

semaphore.yellow.set_state ("off")

semaphore.red.set_state ("on")

sleep (4)

semaphore.red.set_state ("off")

sleep (2)

semaphore.red.set_state ("on")

sleep (1)

semaphore.yellow.set_state ("on")

sleep (0.5)

semaphore.red.set_state ("off")
semaphore.yellow.set_state ("off")

semaphore.green.set_state ("on")

sleep (1)

semaphore.green.set_state ("off")

semaphore.yellow.set_state ("on")

sleep (0.5)

semaphore.yellow.set_state ("off")

sleep (0.5)

semaphore.red.set_state ("on")

sleep (0.5)

semaphore.yellow.set_state ("on")

sleep (0.5)
# se mi to uz nechtelo dal psat. Mela to byt sekvence na Mozartovu Nocni hudbu