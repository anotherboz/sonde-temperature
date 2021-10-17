import machine

def is_waking_up():
    if machine.reset_cause() == machine.DEEPSLEEP_RESET:
        return True
    else:
        return False

def deep_sleep(seconds):
    # configure RTC.ALARM0 to be able to wake the device
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

    # set RTC.ALARM0 to fire after seconds (waking the device)
    rtc.alarm(rtc.ALARM0, seconds * 1000)

    # put the device to sleep
    machine.deepsleep()
