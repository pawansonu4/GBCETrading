
import pandas as pd

def readxls():

    df1=pd.read_excel("C:/Users/Pawan/IdeaProjects/GBCETrading/GBCEdata.xlsx")
    df2=df1.set_index("Stock Symbol", drop=False)
    return df2

def calc(t,p):
    cell=readxls()
    #Check if the product type is common or preferred
    if cell.loc[t,"Type"]=="Common":
        dividy=int(cell.loc[t,"Last Dividend"])/p
    else:
        dividy=cell.loc[t,"Fixed Dividend"]*cell.loc[t,"Par Value"]/p
    print("INFO: Divident yeild is " + str(dividy))

    try:
        peratio=p/dividy
    except ZeroDivisionError:
        print("WARN: Divident yield is zero, hence P/E rato cant be calculated.")
    else:
        print("INFO: P/E Ratio is " + str(peratio))

def trade_entry():

def trade(trade):
    if trade=="B":



if __name__ == '__main__':
    ticker = input("INFO: Enter the ticker you want to investigate.")
    price = int(input("INFO: Enter the Price"))
    calc(ticker,price)
    trade = input("INFO: Do you wish to buy or sell at this moment. Type B to buy and S to sell the commodity selected")

