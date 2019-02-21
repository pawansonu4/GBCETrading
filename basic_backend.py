import mvc_exceptions as mvc_exc
tickers = list()


def create_ticker(StockSym, Type, LastDiv, FixedDivPer, ParValue):
    global tickers
    results = list(filter(lambda x: x['StockSym'] == StockSym, tickers))
    if results:
        raise mvc_exc.tickerAlreadyStored('"{}" already stored!'.format(StockSym))
    else:
        tickers.append({'StockSym': StockSym, 'Type': Type, 'LastDiv': LastDiv, 'FixedDivPer': FixedDivPer, 'ParValue':ParValue})


def create_tickers(app_tickers):
    global tickers
    tickers = app_tickers


def read_ticker(StockSym):
    global tickers
    mytickers = list(filter(lambda x: x['StockSym'] == StockSym, tickers))
    if mytickers:
        return mytickers[0]
    else:
        raise mvc_exc.tickerNotStored(
            'Can\'t read "{}" because it\'s not stored'.format(StockSym))


def read_tickers():
    global tickers
    return [ticker for ticker in tickers]

def update_ticker(StockSym, Type, LastDiv, FixedDivPer, ParValue):
    global tickers

    idxs_tickers = list(
        filter(lambda i_x: i_x[1]['StockSym'] == StockSym, enumerate(tickers)))
    if idxs_tickers:
        i, ticker_to_update = idxs_tickers[0][0], idxs_tickers[0][1]
        tickers[i] = {'StockSym': StockSym, 'Type': Type, 'LastDiv': LastDiv, 'FixedDivPer': FixedDivPer, 'ParValue':ParValue}
    else:
        raise mvc_exc.tickerNotStored(
            'Can\'t update "{}" because it\'s not stored'.format(StockSym))


def delete_ticker(StockSym):
    global tickers

    idxs_tickers = list(
        filter(lambda i_x: i_x[1]['StockSym'] == StockSym, enumerate(tickers)))
    if idxs_tickers:
        i, ticker_to_delete = idxs_tickers[0][0], idxs_tickers[0][1]
        del tickers[i]
    else:
        raise mvc_exc.tickerNotStored(
            'Can\'t delete "{}" because it\'s not stored'.format(StockSym))

def calc(StockSym, price):
    global tickers
    idxs_tickers = list(
        filter(lambda i_x: i_x[1]['StockSym'] == StockSym, enumerate(tickers)))
    if idxs_tickers:
        i, ticker_to_calc = idxs_tickers[0][0], idxs_tickers[0][1]
        if tickers["Type"]=="Common":
            dividy=int(tickers["Last Dividend"])/price
        else:
            dividy=cell.loc[t,"Fixed Dividend"]*cell.loc[t,"Par Value"]/p
    else:
        raise mvc_exc.tickerNotStored(
            'Can\'t calc "{}" because it\'s not stored'.format(StockSym))

# def main():
#
#     my_tickers = [
#         {'StockSym': 'TEA', 'Type': 'Common', 'LastDiv': 0, 'FixedDivPer': '', 'ParValue':100},
#         {'StockSym': 'POP', 'Type': 'Common', 'LastDiv': 8, 'FixedDivPer': '', 'ParValue':100},
#         {'StockSym': 'ALE', 'Type': 'Common', 'LastDiv': 23, 'FixedDivPer': '', 'ParValue':100},
#         {'StockSym': 'GIN', 'Type': 'Preferred', 'LastDiv': 8, 'FixedDivPer': '2', 'ParValue':100},
#         {'StockSym': 'JOE', 'Type': 'Common', 'LastDiv': 13, 'FixedDivPer': '', 'ParValue':100},
#     ]
#     t_end=time.time()+60*60
#     dict_mem={}
#     # CREATE
#     create_tickers(my_tickers)
#     #create_ticker('VON', 'Common', 3,'7',150)
#     # READ
#     print('READ tickers')
#     print(read_tickers())
#     # print('READ TEA')
#     # print(read_ticker('TEA'))
#     #
#     # # UPDATE
#     # print('UPDATE TEA')
#     # update_ticker('TEA', 'Common', 3,'7',150)
#     # print(read_ticker('TEA'))
#     #
#     # # DELETE
#     # print('DELETE TEA')
#     # delete_ticker('TEA')
#     #
#     # print('READ tickers')
#     # print(read_tickers())
#
#     #Loop to make process run for an hour repetatively
#     # while time.time()<t_end:
#     #     ticker = input("INFO: Enter the ticker you want to investigate.")
#     #     price = int(input("INFO: At what per unit price of " + ticker + " you are planning to book the trade."))
#     #     calc(ticker,price)
#
# if __name__ == '__main__':
#     main()