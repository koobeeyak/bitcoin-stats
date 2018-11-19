# std
import asyncio

# 3p
import aiohttp

# project
from models.bitcoin_stat import BitcoinStat
from process.utils import get_full_endpoint

ENDPOINTS_TO_VALUES = {
    'MKPRU': 'btc_price',
    'TOUTV': 'output_volume',
    'NADDU': 'unique_addresses',
}


class BitcoinStatsScraper(object):
    stats_by_date = {}

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    @asyncio.coroutine
    def get_bitcoin_stats(self, endpoint):
        url = get_full_endpoint(endpoint, self.start_date, self.end_date)
        response = yield from aiohttp.request('get', url)
        json = (yield from response.json())
        for date, value in json.get('dataset', {}).get('data'):
            if not self.stats_by_date[date]:
                self.stats_by_date[date] = BitcoinStat(date=date)
            setattr(self.stats_by_date[date], ENDPOINTS_TO_VALUES[endpoint], value)

    def run(self):
        loop = asyncio.get_event_loop()
        tasks = [asyncio.ensure_future(self.get_bitcoin_stats(endpoint)) for endpoint in ENDPOINTS_TO_VALUES.keys()]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()
        return self.stats_by_date.values()
