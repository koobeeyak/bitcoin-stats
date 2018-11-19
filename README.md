## bitcoin-stats

Web app opening an endpoint aggregating basic Bitcoin performance.

Queries the [QUANDL API](https://www.quandl.com/data/BCHAIN-Blockchain) for Bitcoin price, volume, and number of unique addresses.



### Setup
- Create your free account on quandl.com
- Paste your api credentials to environment variable QUANDL_API_KEY in Dockerfile

### Running
Run the app using docker-compose

`$ docker-compose up`

### Example queries
Exposes port `5000` in development environment.

Pass dates as YYYY-MM-DD string.

> http://localhost:5000/api/v1/bitcoin_stats?start_date=2017-12-20&end_date=2018-03-15