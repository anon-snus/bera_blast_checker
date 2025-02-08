import random
import config
from utils import *
from config import *
from scrapper import Scrapper
import asyncio

async def main():
    scrapper = Scrapper(proxy=PROXY if config.proxy_use else None)

    with open('wallets.txt', 'r') as f:
        wallets = f.read().splitlines()

    for wallet in wallets:
        wallet_data = await scrapper.poh(wallet)  # Получение данных для кошелька
        print(wallet_data)
        await asyncio.sleep(random.randint(2, 5))  # Ожидание между кошельками

        # Смена IP
        if config.proxy_use:
            q = await change_ip(CHANGE_IP_LINK)
            print(f'Changing IP: {q}')
    print("Обработка завершена, сессия бота закрыта.")

if __name__ == '__main__':
    asyncio.run(main())
