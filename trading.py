
import pandas as pd
import csv
import time
import datetime

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

def vws(dict_mem,ticker):
    vws_time=time.time()
    numrator=0
    denominator=0
    numrator_arr=[]
    for i in dict_mem[ticker]:
        if i[2]-vws_time<=600:
            numrator_arr.append(i[1]*i[4])
            denominator=denominator+i[4]
    numrator=sum(numrator_arr)
    vwsp=numrator/denominator
    return vwsp

def trade(trade_type,price,ticker,dict_mem,quantity):
    trade_arr=[]
    main_arr=[]
    if trade_type=="B" or trade_type=="S":
        if ticker in dict_mem:
            main_arr=dict_mem[ticker]

        trade_arr.append(trade_type)
        trade_arr.append(price)
        trade_arr.append(time.time())
        trade_arr.append(datetime.datetime.fromtimestamp(trade_arr[1]).strftime('%Y-%m-%d %H:%M:%S'))
        trade_arr.append(quantity)

        main_arr.append(trade_arr)
        dict_mem[ticker]=main_arr
        print("wait in mem")
    else:
        print("INFO: Please choose the correct option")



if __name__ == '__main__':

    #keeping the process ivoked for an hour
    t_end=time.time()+60*60

    dict_mem={}
    while time.time()<t_end:
        ticker = input("INFO: Enter the ticker you want to investigate.")
        price = int(input("INFO: At what per unit price of " + ticker + " you are planning to book the trade."))
        calc(ticker,price)
        trade_type = input("INFO: Do you wish to buy or sell at this moment. Type B to buy and S to sell the commodity selected")
        quantity = int(input("INFO: Input the quantity you wish to purchase."))

        trade(trade_type,price,ticker,dict_mem,quantity)
        vws_ans=input("Do you wish to calculate Volume Weighted stock price of " + ticker + " .Answer Y/N" )
        if vws_ans=="Y":
            vwsp=vws(dict_mem,ticker)
            print("INFO: ")
        else:
            print("WARN: Answer is not appropriate.")