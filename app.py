# 3p
from flask import Flask
from flask_restful import Api

# project
from resources.bitcoin_stats import BitcoinStats


app = Flask(__name__)
api = Api(app)
api_version = 'v1'

api_url = 'api/{}'.format(api_version)
api.add_resource(BitcoinStats, '/{}/bitcoin_stats/<start_date>/<end_date>'.format(api_url))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

