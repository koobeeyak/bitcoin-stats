# project
from models.bitcoin_stat_serializer import BitcoinStatSerializer


class BitcoinStat(object):
    def __init__(self, date, btc_price, output_volume, unique_addresses):
        self.date = date
        self.btc_price = btc_price
        self.output_volume = output_volume
        self.unique_addresses = unique_addresses

    def to_json(self):
        return BitcoinStatSerializer(self).data
