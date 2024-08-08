"""before get to the Chapter 19,  first it's better to learn some basic concept"""
from asyncio import tasks

"""
AsyncIO : for managing many waiting tasks

Processes : for maximizing performance on cpu intensive tasks

Threading : for parallel tasks that share data with minimal cpu use
"""

import asyncio


async def say_hello():
    print(1)
    await asyncio.sleep(5)
    return "Hello"


async def say_goodbye():
    print(2)
    await asyncio.sleep(5)
    return "Goodbye"


async def main_beta():
    task_1 = say_hello()
    await task_1  # the event of the async not going to run until its gets await, and after become await its start to run
    # this is not helping us in order to become more efficient so we have to know the tasks concept
    task_2 = say_goodbye()
    await task_2


# asyncio.run(main_beta())

async def main():
    task_1 = asyncio.create_task(say_hello())
    task_2 = asyncio.create_task(say_goodbye())

    await task_1  # when we await the tasks its start running and when one of the task have to wait, its go for another
    await task_2  # one and run that one so both task acord at the same time

    # notice if the task come after the another await, its don't perform until before await complete
    task_3 = asyncio.create_task(say_hello())

    await task_3


asyncio.run(main())

# also we can instead of gathering the task and run it one by one , gather all using asyncio.gather()

async def main_ultra():
    results = await asyncio.gather(say_hello(), say_goodbye())
    # the problem with the gather is that if one of them get error it's not going to stop the other
    for result in results:
        print(result)


# asyncio.run(main_ultra())

# for also have the option that if one of the task failed and get error all task don't happen we can use async context manager

async def super_main_ultra():
    tasks = []
    async with asyncio.TaskGroup() as tg:

        task_1 = tg.create_task(say_hello())
        tasks.append(task_1)
        task_2 = tg.create_task(say_goodbye())
        tasks.append(task_2)

    results = [task.result() for task in tasks]

    for result in results:
        print(result)  # none of them going to run if we have exception in one of them


# asyncio.run(super_main_ultra())


"""
Lock:
    sometime its happen that we have some shared value, and we want to use them one at the time there is and idea
    of using async with lock to enter one at the time 
"""

shared_resource = 0
lock = asyncio.Lock()


async def modify_shared_value():
    global shared_resource
    async with lock:
        shared_resource += 1


async def lock_main():
    await asyncio.gather(modify_shared_value(), modify_shared_value())
    # there not going to change the shared_resource at the same time


"""
Semaphore:
    similar to lock but we can modify how many concurrent accesses
"""


async def access_resource(semaphore):
    async with semaphore:
        await asyncio.sleep(2)


async def semaphore_main():
    semaphore = asyncio.Semaphore(2)  # allow 2 concurrent accesses
    await asyncio.gather(*(access_resource(semaphore) for _ in range(5)))  # get into two at the time


"""
Event:
    its like the event , and its wait until its set by another func
"""


async def waiter(event):
    print("wait to set")
    await event.wait()  # its wait here until on another place its set
    print("set")


async def setter(event):
    await asyncio.sleep(2)
    event.set()
