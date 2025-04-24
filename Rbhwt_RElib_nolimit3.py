import time
from rotary_irq_rp2 import RotaryIRQ

r = RotaryIRQ(
    pin_num_clk=16,
    pin_num_dt=17,
    reverse=False,
    incr=1,
    range_mode=RotaryIRQ.RANGE_UNBOUNDED,
    pull_up=True,
    half_step=False,
)

val_old = r.value()
while True:
    val_new = r.value()

    if val_old != val_new:
        val_old = val_new
        print("step =", val_new)

    time.sleep_ms(50)
