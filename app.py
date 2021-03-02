# app.py
from flask import Flask, request, jsonify
import robin_stocks as rs


app = Flask(__name__)


@app.route('/')
def index():

    rs.robinhood.login(username='bsavelli66@gmail.com', password='Canyon6687', 
                          expiresIn=86400, scope='internal', by_sms=True,
                          store_session=True)
    return rs.robinhood.order_buy_crypto_by_price('BTC',5)['price']
    



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run()