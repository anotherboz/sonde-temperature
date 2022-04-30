import uasyncio
import heartbeat

async def heartbeat_thread():
    await heartbeat.heartbeat()

async def blah_thread():
    while(1):
        print('blah');
        await uasyncio.sleep(1)

async def async_main():
    print('start task')
    t1 = uasyncio.create_task(heartbeat_thread())
    t2 = uasyncio.create_task(blah_thread())
    await uasyncio.sleep_ms(8000)
    heartbeat.set_mode(heartbeat.temp_mode)
    await uasyncio.sleep_ms(8000)
    heartbeat.set_mode(heartbeat.server_mode)
    await uasyncio.sleep_ms(4000)
    heartbeat.set_mode(heartbeat.wait_mode)
    await uasyncio.sleep_ms(4000)
    
    
    print('stop task')
    t1.cancel()
    t2.cancel()
    
uasyncio.run(async_main())

