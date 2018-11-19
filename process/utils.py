import os


def get_full_endpoint(partial_endpoint, start_date, end_date):
    return 'https://www.quandl.com' \
           '/api/v3/datasets/BCHAIN/{partial_endpoint}.json' \
           '?start_date={start_date}' \
           '&end_date={end_date}' \
           '&api_key={api_key}'\
        .format(
            partial_endpoint=partial_endpoint,
            start_date=start_date,
            end_date=end_date,
            api_key=os.environ['QUANDL_API_KEY']
        )
