# 3p
from flask_restful import Resource, reqparse

# project
from process.bitcoin_stats_scraper import BitcoinStatsScraper


class BitcoinStats(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('start_date')
        parser.add_argument('end_date')
        args = parser.parse_args()
        start_date = args.get('start_date')
        end_date = args.get('end_date')
        bitcoin_stats = BitcoinStatsScraper('2015-11-01', '2015-12-20').run()
        return {
            "start_date": start_date,
            "end_date": end_date,
            "statistics": [b.to_json() for b in bitcoin_stats],
        }
