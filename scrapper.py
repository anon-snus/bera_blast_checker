import asyncio

from utils import async_get, change_ip

class Scrapper:
	def __init__(self, proxy):
		self.proxy = proxy

	async def poh(self, wallet:str):
		url = f'https://www.blastbera.fun/api/check-eligibility?address=${wallet}'
		for i in range(5):
			try:
				res = await async_get(url, self.proxy)
				isEligible = res.get('isEligible')
				return {'wallet': wallet, 'isEligible': isEligible,}
			except Exception as e:
				print(e)
				await asyncio.sleep(1)


