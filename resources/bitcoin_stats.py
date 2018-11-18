# 3p
from flask_restful import Resource

# project
from models.bitcoin_stat import BitcoinStat


class BitcoinStats(Resource):
    def get(self, start_date, end_date):
        bitcoins = [
            BitcoinStat('11.12.2018', 23.54, 100.10, 98),
            BitcoinStat('11.13.2018', 22.84, 99.10, 91),
        ]
        return {
            "bitcoinStats": [b.to_json() for b in bitcoins]
        }