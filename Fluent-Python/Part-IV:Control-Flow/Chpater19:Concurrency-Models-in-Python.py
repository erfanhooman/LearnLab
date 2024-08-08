"""
In Python's threading module, an Event is a synchronization primitive that allows threads to communicate with each
other by signaling events. The Event class provides a way to manage the state of an internal flag that can be set,
cleared, and waited upon by multiple threads.
"""

"""
Thread
"""

import itertools
import time
import threading as th


def spin(msg, done) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(0.1):
            break
    blank = ' ' * len(status)
    print(f'\r{blank}\r', end='')


def slow() -> int:
    time.sleep(3)
    return 42


# def supervisor() -> int:  # Thread Version
#     done = th.Event()
#     spinner = th.Thread(target=spin, args=('Thinking!', done))
#     print(f'spinner object: {spinner}')
#     spinner.start()
#     result = slow()
#     done.set()
#     spinner.join()
#     return result

import multiprocessing as mp


def supervisor() -> int:  # Multiprocessing Version
    done = mp.Event()
    spinner = mp.Pipe(target=spin, args=('Thinking', done))
    print(f"spinner object: {spinner}")
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result


# if __name__ == '__main__':
#     result = supervisor()
#     print("answer:", result)


"""
Writing it using a AsyncIO library
"""

import asyncio


async def async_supervisor() -> int:
    spinner = asyncio.create_task(async_spin())

    result = await async_slow()  # call slow and block supervisor until slow return
    spinner.cancel()
    return result


async def async_spin() -> None:
    for char in itertools.cycle(r'\|/-'):
        print(f'\r{char}', end='', flush=True)
        try:
            await asyncio.sleep(0.1)  # if the async is cancelled the error will be raised
        except asyncio.CancelledError:
            break


async def async_slow() -> int:
    await asyncio.sleep(2)  # use this sleep cause the time.sleep() block all coroutine
    return 42


if __name__ == '__main__':
    result = asyncio.run(async_supervisor())  # the main function stay block until supervisor return
    print(f"Answer {result}")

