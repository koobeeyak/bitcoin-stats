# 3p
from flask_restful import Resource, reqparse

# project
from models.bitcoin_stat import BitcoinStat


class BitcoinStats(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('start_date')
        parser.add_argument('end_date')
        args = parser.parse_args()
        start_date = args.get('start_date')
        end_date = args.get('end_date')
        bitcoins = [
            BitcoinStat('11.12.2018', 23.54, 100.10, 98),
            BitcoinStat('11.13.2018', 22.84, 99.10, 92),
        ]
        # bitcoin_stats = get_bitcoin_stats(start_date, end_date)
        # bitcoin_stats = BitcoinStatsScraper(start_date, end_date).run()
        return {
            "bitcoinStats": [b.to_json() for b in bitcoins],
            "start_date": start_date,
            "end_date": end_date,
        }
