import time
import asyncio

async def start_strongman(name, power):

    print(f'Силач {name} начал соревнования')
    for power in range(1,6):
        await asyncio.sleep(6-power)
        print(f'Силач {name} поднял {power}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Вася', 3))
    task2 = asyncio.create_task(start_strongman('Дима', 4))
    task3 = asyncio.create_task(start_strongman('Паша', 5))
    await task1
    await task2
    await task3

if __name__ == '__main__':
    asyncio.run(start_tournament())





