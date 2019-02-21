import basic_backend
import mvc_exceptions as mvc_exc
import time


class ModelBasic(object):

    def __init__(self, application_tickers):
        self._ticker_type = 'product'
        self.create_tickers(application_tickers)

    @property
    def ticker_type(self):
        return self._ticker_type

    @ticker_type.setter
    def ticker_type(self, new_ticker_type):
        self._ticker_type = new_ticker_type

    def create_ticker(self, Stocksym, price, quantity):
        basic_backend.create_ticker(Stocksym, price, quantity)

    def create_tickers(self, tickers):
        basic_backend.create_tickers(tickers)

    def read_ticker(self, Stocksym):
        return basic_backend.read_ticker(Stocksym)

    def read_tickers(self):
        return basic_backend.read_tickers()

    def update_ticker(self, Stocksym, price, quantity):
        basic_backend.update_ticker(Stocksym, price, quantity)

    def delete_ticker(self, Stocksym):
        basic_backend.delete_ticker(Stocksym)

    def calc(self, Stocksym, price):
        basic_backend.calc(Stocksym,price)

class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_tickers(self, bullet_points=False):
        tickers = self.model.read_tickers()
        ticker_type = self.model.ticker_type
        if bullet_points:
            self.view.show_bullet_point_list(ticker_type, tickers)
        else:
            self.view.show_number_point_list(ticker_type, tickers)

    def show_ticker(self, ticker_Stocksym):
        try:
            ticker = self.model.read_ticker(ticker_Stocksym)
            ticker_type = self.model.ticker_type
            self.view.show_ticker(ticker_type, ticker_Stocksym, ticker)
        except mvc_exc.tickerNotStored as e:
            self.view.display_missing_ticker_error(ticker_Stocksym, e)

    def insert_ticker(self, Stocksym, price, quantity):
        assert price > 0, 'price must be greater than 0'
        assert quantity >= 0, 'quantity must be greater than or equal to 0'
        ticker_type = self.model.ticker_type
        try:
            self.model.create_ticker(Stocksym, price, quantity)
            self.view.display_ticker_stored(Stocksym, ticker_type)
        except mvc_exc.tickerAlreadyStored as e:
            self.view.display_ticker_already_stored_error(Stocksym, ticker_type, e)

    def update_ticker(self, Stocksym, price, quantity):
        assert price > 0, 'price must be greater than 0'
        assert quantity >= 0, 'quantity must be greater than or equal to 0'
        ticker_type = self.model.ticker_type

        try:
            older = self.model.read_ticker(Stocksym)
            self.model.update_ticker(Stocksym, price, quantity)
            self.view.display_ticker_updated(
                Stocksym, older['price'], older['quantity'], price, quantity)
        except mvc_exc.tickerNotStored as e:
            self.view.display_ticker_not_yet_stored_error(Stocksym, ticker_type, e)
            # if the ticker is not yet stored and we performed an update, we have
            # 2 options: do nothing or call insert_ticker to add it.
            # self.insert_ticker(Stocksym, price, quantity)

    def update_ticker_type(self, new_ticker_type):
        old_ticker_type = self.model.ticker_type
        self.model.ticker_type = new_ticker_type
        self.view.display_change_ticker_type(old_ticker_type, new_ticker_type)

    def delete_ticker(self, Stocksym):
        ticker_type = self.model.ticker_type
        try:
            self.model.delete_ticker(Stocksym)
            self.view.display_ticker_deletion(Stocksym)
        except mvc_exc.tickerNotStored as e:
            self.view.display_ticker_not_yet_stored_error(Stocksym, ticker_type, e)

    def calc(self, Stocksym, price):
        assert price > 0, 'price must be greater than 0'
        ticker_type = self.model.ticker_type
        try:
            ticker_row = self.model.read_ticker(Stocksym)
            self.model.calc(Stocksym, price)
            self.view.display_ticker_cal(
                Stocksym, price)
        except mvc_exc.tickerNotStored as e:
            self.view.display_ticker_not_yet_stored_error(Stocksym, ticker_type, e)

class View(object):

    @staticmethod
    def show_bullet_point_list(ticker_type, tickers):
        print('--- {} LIST ---'.format(ticker_type.upper()))
        for ticker in tickers:
            print('* {}'.format(ticker))

    @staticmethod
    def show_number_point_list(ticker_type, tickers):
        print('--- {} LIST ---'.format(ticker_type.upper()))
        for i, ticker in enumerate(tickers):
            print('{}. {}'.format(i+1, ticker))

    @staticmethod
    def show_ticker(ticker_type, ticker, ticker_info):
        print('//////////////////////////////////////////////////////////////')
        print('Good news, we have some {}!'.format(ticker.upper()))
        print('{} INFO: {}'.format(ticker_type.upper(), ticker_info))
        print('//////////////////////////////////////////////////////////////')

    @staticmethod
    def display_missing_ticker_error(ticker, err):
        print('**************************************************************')
        print('We are sorry, we have no {}!'.format(ticker.upper()))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_ticker_already_stored_error(ticker, ticker_type, err):
        print('**************************************************************')
        print('Hey! We already have {} in our {} list!'
              .format(ticker.upper(), ticker_type))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_ticker_not_yet_stored_error(ticker, ticker_type, err):
        print('**************************************************************')
        print('We don\'t have any {} in our {} list. Please insert it first!'
              .format(ticker.upper(), ticker_type))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_ticker_stored(ticker, ticker_type):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Hooray! We have just added some {} to our {} list!'
              .format(ticker.upper(), ticker_type))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_change_ticker_type(older, newer):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change ticker type from "{}" to "{}"'.format(older, newer))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_ticker_updated(ticker, o_price, o_quantity, n_price, n_quantity):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change {} price: {} --> {}'
              .format(ticker, o_price, n_price))
        print('Change {} quantity: {} --> {}'
              .format(ticker, o_quantity, n_quantity))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_ticker_deletion(Stocksym):
        print('--------------------------------------------------------------')
        print('We have just removed {} from our list'.format(Stocksym))
        print('--------------------------------------------------------------')

if __name__ == '__main__':
    my_tickers = [
                {'StockSym': 'TEA', 'Type': 'Common', 'LastDiv': 0, 'FixedDivPer': '', 'ParValue':100},
                {'StockSym': 'POP', 'Type': 'Common', 'LastDiv': 8, 'FixedDivPer': '', 'ParValue':100},
                {'StockSym': 'ALE', 'Type': 'Common', 'LastDiv': 23, 'FixedDivPer': '', 'ParValue':100},
                {'StockSym': 'GIN', 'Type': 'Preferred', 'LastDiv': 8, 'FixedDivPer': '2', 'ParValue':100},
                {'StockSym': 'JOE', 'Type': 'Common', 'LastDiv': 13, 'FixedDivPer': '', 'ParValue':100},
            ]
    c = Controller(ModelBasic(my_tickers), View())
    c.show_tickers()
    t_end=time.time()+60*60
    dict_mem={}
    #Running the process for an hour

    ticker = input("INFO: Enter the ticker you want to investigate.")
    price = int(input("INFO: At what per unit price of " + ticker + " you are planning to book the trade."))
    c.calc(ticker,price)