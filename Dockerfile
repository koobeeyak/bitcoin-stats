FROM python:3.4-alpine

ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt
ENV QUANDL_API_KEY=your-api-key

CMD ["python", "app.py"]
