# 3p
from serpy import Serializer, Field


class BitcoinStatSerializer(Serializer):
    date = Field(required=True)
    btc_price = Field(required=True, label="btcPrice")
    output_volume = Field(required=True, label="outputVolume")
    unique_addresses = Field(required=True, label="uniqueAddresses")
