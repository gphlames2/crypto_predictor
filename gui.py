import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime
from datetime import timedelta
import joblib as jb
from sklearn.preprocessing import MinMaxScaler
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

selected_coins_array = ['BTC-USD','ETH-USD','LTC-USD','USDT-USD','XMR-USD','XRP-USD','ZEC-USD','XLM-USD','BNB-USD',
                        'USDC-USD','SOL-USD','LUNA-USD','ADA-USD',
                      'UST-USD','BUSD-USD','DOGE-USD','AVAX-USD','DOT-USD','SHIB-USD','WBTC-USD']
duration = ['24h']
algorithms = ['Random Forest Regressor']

class coin_prediction:
    random_forest: None
    duration: str = '24h'
    coin: str = 'BTC'
    coins: pd.DataFrame
    investment_amount: int = 100
    target_amount: int = 500
    start_date:str = ''
    end_date:str = ''
    predicted_days = pd.DataFrame()
    predicted_low: np.array
    predicted_high: np.array
    real_prices: None
    model: str = ''
    scaler = MinMaxScaler()
    scaler2 = MinMaxScaler()

    def __init__(self):
        self.random_forest = jb.load('random_forest_model.sav')

    def determine_date(self):
        time_string = datetime.now()
        self.start_date = (time_string - timedelta(days=29)).strftime("%Y/%m/%d").replace('/','-')
        self.end_date = time_string.strftime("%Y/%m/%d").replace('/','-')


    def get_coin(self):
        coins = yf.download(coin,start=self.start_date,end=self.end_date)
        return coins

    def get_coins(self):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
            'start': '1',
            'limit': '100',
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'e98de403-7113-43b7-9ce9-c27b7686d4ad',
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            self.coins = pd.json_normalize(data['data'])

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

    def predict(self,data):
        print(data)
        self.predicted_low = np.array(self.scaler2.inverse_transform(np.array(self.random_forest.predict(self.reshape_data(data['Low'])))
                                                                     .reshape(-1,1)))
        self.predicted_high = np.array(self.scaler2
                                       .inverse_transform(np.array(self.random_forest
                                                                  .predict(self.reshape_data(data['High']))).reshape(-1,1)))
        self.formulate_dataframe()

    def formulate_dataframe(self):
        profit = []
        total_amount = []
        for i in range(0,len(self.predicted_high)):
            difference = self.predicted_high[i] - self.predicted_low[i]
            percentage_difference = (difference * 100)/self.predicted_low[i]
            profit.append(percentage_difference * investment_amount)
            total_amount.append(investment_amount + (percentage_difference * investment_amount))
        pandas_dictionary = {'Highs/Sells': self.predicted_high.reshape(-1), 'Lows/Buy-ins':self.predicted_low.reshape(-1),
                             'Profits':np.array(profit).reshape(-1), 'Total return with investment':np.array(total_amount).reshape(-1)}
        self.predicted_days = pd.DataFrame(pandas_dictionary).astype(str)

    def reshape_data(self, data):
        if self.duration == '24h':
            pass
        else:
            pass
        if self.model == 'Random Forest Regressor':
            data_array = []
            for i in range(30, len(data)+1):
                data_array.append(data[i - 30:i])
            data = np.array(data_array).reshape(len(data_array),30)
            data = np.array(self.scaler.fit_transform(data))
            self.scaler2.fit_transform(np.array(data_array.pop()).reshape(-1,1))
            return data
        else:
            scaler = MinMaxScaler()
            data_array = []
            for i in range(30, len(data)):
                data_array.append(data[i - 30:i])
            data = np.array(data).reshape((len(data), 30,1))
            data = np.array(scaler.fit_transform(data))
            return data


coin_pred = coin_prediction()
coin_pred.get_coins()
coin_pred.determine_date()

st.set_page_config(
    page_title='SOLigence intelligent coin trading platform',
    layout='wide'
)
st.title('SOLigence intelligent coin trading platform')
placeholder = st.empty()
prediction_table: st.table
with placeholder.container():
    with st.expander('Pick your configuration'):
        coin = st.selectbox('Select crypto asset',selected_coins_array)
        length = st.selectbox('Select duration',duration)
        algorithm = st.selectbox('Select algorithm',algorithms)
        investment_amount = int(st.number_input('Enter investment amount'))
        target_amount = int(st.number_input('Enter target amount'))
        if st.button('Predict'):
            with st.spinner('Prediction in progress..........'):
                coin_pred.duration = length
                coin_pred.target_amount = target_amount
                coin_pred.investment_amount = investment_amount
                coin_pred.model = algorithm
                coin_pred.coin = coin
                coin_pred.predict(coin_pred.get_coin())
    st.text('estimated profit table')
    prediction_table = st.dataframe(coin_pred.predicted_days)
    st.text('Daily crypto statistics data from coinmarketcap.com')
    st.dataframe(coin_pred.coins.drop(['date_added','tags',
                                       'platform','self_reported_circulating_supply','self_reported_market_cap',
                                       'last_updated','quote.USD.market_cap','quote.USD.market_cap_dominance',
                                       'quote.USD.fully_diluted_market_cap','platform.name','platform.symbol',
                                       'platform.slug','platform.token_address','platform.id','platform.token_address','slug'],
                                      axis=1).astype(str))
    print(coin_pred.coins)


