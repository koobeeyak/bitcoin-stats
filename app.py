# 3p
from flask import Flask
from flask_restful import Api

# project
from resources.bitcoin_stats import BitcoinStats


app = Flask(__name__)
api = Api(app)
api_version = 'v1'

api.add_resource(BitcoinStats, '/api/{}/bitcoin_stats'.format(api_version))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

