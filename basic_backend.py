import mvc_exceptions as mvc_exc

tickers = list()


def create_ticker(StockSym, Type, LastDiv, FixedDivPer, ParValue):
    global tickers
    results = list(filter(lambda x: x['StockSym'] == StockSym, tickers))
    if results:
        raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(StockSym))
    else:
        items.append({'StockSym': StockSym, 'Type': Type, 'LastDiv': LastDiv, 'FixedDivPer': FixedDivPer, 'ParValue':ParValue})


def create_tickers(app_tickers):
    global tickers
    tickers = app_tickers


def read_ticker(StockSym):
    global tickers
    myitems = list(filter(lambda x: x['StockSym'] == StockSym, tickers))
    if myitems:
        return myitems[0]
    else:
        raise mvc_exc.ItemNotStored(
            'Can\'t read "{}" because it\'s not stored'.format(StockSym))


def read_tickers():
    global tickers
    return [ticker for ticker in tickers]

def update_item(name, price, quantity):
    global items
    # Python 3.x removed tuple parameters unpacking (PEP 3113), so we have to do it manually (i_x is a tuple, idxs_items is a list of tuples)
    idxs_items = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, item_to_update = idxs_items[0][0], idxs_items[0][1]
        items[i] = {'name': name, 'price': price, 'quantity': quantity}
    else:
        raise mvc_exc.ItemNotStored(
            'Can\'t update "{}" because it\'s not stored'.format(name))


def delete_item(name):
    global items
    # Python 3.x removed tuple parameters unpacking (PEP 3113), so we have to do it manually (i_x is a tuple, idxs_items is a list of tuples)
    idxs_items = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
        del items[i]
    else:
        raise mvc_exc.ItemNotStored(
            'Can\'t delete "{}" because it\'s not stored'.format(name))

def main():

    my_tickers = [
        {'StockSym': 'TEA', 'Type': 'Common', 'LastDiv': 0, 'FixedDivPer': '', 'ParValue':100},
        {'StockSym': 'POP', 'Type': 'Common', 'LastDiv': 8, 'FixedDivPer': '', 'ParValue':100},
        {'StockSym': 'ALE', 'Type': 'Common', 'LastDiv': 23, 'FixedDivPer': '', 'ParValue':100},
        {'StockSym': 'GIN', 'Type': 'Preferred', 'LastDiv': 8, 'FixedDivPer': '2', 'ParValue':100},
        {'StockSym': 'JOE', 'Type': 'Common', 'LastDiv': 13, 'FixedDivPer': '', 'ParValue':100},
    ]

    # CREATE
    create_tickers(my_tickers)
    create_ticker('VON', 'Common', 3,'7',150)
    # if we try to re-create an object we get an ItemAlreadyStored exception
    # create_item('beer', price=2.0, quantity=10)

    # READ
    print('READ tickers')
    print(read_tickers())
    # if we try to read an object not stored we get an ItemNotStored exception
    # print('READ chocolate')
    # print(read_item('chocolate'))
    print('READ TEA')
    print(read_ticker('TEA'))

    # UPDATE
    print('UPDATE TEA')
    update_item('bread', price=2.0, quantity=30)
    print(read_item('bread'))
    # if we try to update an object not stored we get an ItemNotStored exception
    # print('UPDATE chocolate')
    # update_item('chocolate', price=10.0, quantity=20)

    # DELETE
    print('DELETE beer')
    delete_item('beer')
    # if we try to delete an object not stored we get an ItemNotStored exception
    # print('DELETE chocolate')
    # delete_item('chocolate')

    print('READ items')
    print(read_items())

if __name__ == '__main__':
    main()