import asyncio
import logging

async def coro1():
    while True:
        for i in range(100000):
            await asyncio.sleep(0.1)
        print('coro1')

async def coro2():
    for i in range(25):
        await asyncio.sleep(0.5)
        print(i)

    loop = asyncio.get_event_loop()
    loop.stop()


logging.getLogger('asyncio').setLevel('CRITICAL')

asyncio.ensure_future(coro1())
asyncio.ensure_future(coro2())

loop = asyncio.get_event_loop()
loop.run_forever()
loop.close()
