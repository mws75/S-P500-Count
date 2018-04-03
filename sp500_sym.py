#See test_batch variable to set a batch < 500, then you won't have to  
# wait 30 min for the application to run.

import urllib
from urllib.request import urlopen 
import sys
import time
import csv
import pandas as pd

'''Global Variables aree the list of 
S&P 500 Co, and the API call'''

co = list()
co = ['ABT', 'ABBV', 'ACN', 'ACE', 'ADBE', 'ADT', 'AAP', 'AES', 'AET', 'AFL', 'AMG', 'A', 'GAS', 'APD', 'ARG', 'AKAM', 'AA', 'AGN', 'ALXN', 'ALLE', 'ADS', 'ALL', 'ALTR', 'MO', 'AMZN', 'AEE', 'AAL', 'AEP', 'AXP', 'AIG', 'AMT', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'APC', 'ADI', 'AON', 'APA', 'AIV', 'AMAT', 'ADM', 'AIZ', 'T', 'ADSK', 'ADP', 'AN', 'AZO', 'AVGO', 'AVB', 'AVY', 'BHI', 'BLL', 'BAC', 'BK', 'BCR', 'BXLT', 'BAX', 'BBT', 'BDX', 'BBBY', 'BRK-B', 'BBY', 'BLX', 'HRB', 'BA', 'BWA', 'BXP', 'BSK', 'BMY', 'BRCM', 'BF-B', 'CHRW', 'CA', 'CVC', 'COG', 'CAM', 'CPB', 'COF', 'CAH', 'HSIC', 'KMX', 'CCL', 'CAT', 'CBG', 'CBS', 'CELG', 'CNP', 'CTL', 'CERN', 'CF', 'SCHW', 'CHK', 'CVX', 'CMG', 'CB', 'CI', 'XEC', 'CINF', 'CTAS', 'CSCO', 'C', 'CTXS', 'CLX', 'CME', 'CMS', 'COH', 'KO', 'CCE', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CSC', 'CAG', 'COP', 'CNX', 'ED', 'STZ', 'GLW', 'COST', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DE', 'DLPH', 'DAL', 'XRAY', 'DVN', 'DO', 'DTV', 'DFS', 'DISCA', 'DISCK', 'DG', 'DLTR', 'D', 'DOV', 'DOW', 'DPS', 'DTE', 'DD', 'DUK', 'DNB', 'ETFC', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMC', 'EMR', 'ENDP', 'ESV', 'ETR', 'EOG', 'EQT', 'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'ES', 'EXC', 'EXPE', 'EXPD', 'ESRX', 'XOM', 'FFIV', 'FB', 'FAST', 'FDX', 'FIS', 'FITB', 'FSLR', 'FE', 'FSIV', 'FLIR', 'FLS', 'FLR', 'FMC', 'FTI', 'F', 'FOSL', 'BEN', 'FCX', 'FTR', 'GME', 'GPS', 'GRMN', 'GD', 'GE', 'GGP', 'GIS', 'GM', 'GPC', 'GNW', 'GILD', 'GS', 'GT', 'GOOGL', 'GOOG', 'GWW', 'HAL', 'HBI', 'HOG', 'HAR', 'HRS', 'HIG', 'HAS', 'HCA', 'HCP', 'HCN', 'HP', 'HES', 'HPQ', 'HD', 'HON', 'HRL', 'HSP', 'HST', 'HCBK', 'HUM', 'HBAN', 'ITW', 'IR', 'INTC', 'ICE', 'IBM', 'IP', 'IPG', 'IFF', 'INTU', 'ISRG', 'IVZ', 'IRM', 'JEC', 'JBHT', 'JNJ', 'JCI', 'JOY', 'JPM', 'JNPR', 'KSU', 'K', 'KEY', 'GMCR', 'KMB', 'KIM', 'KMI', 'KLAC', 'KSS', 'KRFT', 'KR', 'LB', 'LLL', 'LH', 'LRCX', 'LM', 'LEG', 'LEN', 'LVLT', 'LUK', 'LLY', 'LNC', 'LLTC', 'LMT', 'L', 'LOW', 'LYB', 'MTB', 'MAC', 'M', 'MNK', 'MRO', 'MPC', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MAT', 'MKC', 'MCD', 'MHFI', 'MCK', 'MJN', 'MMV', 'MDT', 'MRK', 'MET', 'KORS', 'MCHP', 'MU', 'MSFT', 'MHK', 'TAP', 'MDLZ', 'MON', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MUR', 'MYL', 'NDAQ', 'NOV', 'NAVI', 'NTAP', 'NFLX', 'NWL', 'NFX', 'NEM', 'NWSA', 'NEE', 'NLSN', 'NKE', 'NI', 'NE', 'NBL', 'JWN', 'NSC', 'NTRS', 'NOC', 'NRG', 'NUE', 'NVDA', 'ORLY', 'OXY', 'OMC', 'OKE', 'ORCL', 'OI', 'PCAR', 'PLL', 'PH', 'PDCO', 'PAYX', 'PNR', 'PBCT', 'POM', 'PEP', 'PKI', 'PRGO', 'PFE', 'PCG', 'PM', 'PSX', 'PNW', 'PXD', 'PBI', 'PCL', 'PNC', 'RL', 'PPG', 'PPL', 'PX', 'PCP', 'PCLN', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PSA', 'PHM', 'PVH', 'QRVO', 'PWR', 'QCOM', 'DGX', 'RRC', 'RTN', 'O', 'RHT', 'REGN', 'RF', 'RSG', 'RAI', 'RHI', 'ROK', 'COL', 'ROP', 'ROST', 'RLC', 'R', 'CRM', 'SNDK', 'SCG', 'SLB', 'SNI', 'STX', 'SEE', 'SRE', 'SHW', 'SIAL', 'SPG', 'SWKS', 'SLG', 'SJM', 'SNA', 'SO', 'LUV', 'SWN', 'SE', 'STJ', 'SWK', 'SPLS', 'SBUX', 'HOT', 'STT', 'SRCL', 'SYK', 'STI', 'SYMC', 'SYY', 'TROW', 'TGT', 'TEL', 'TE', 'TGNA', 'THC', 'TDC', 'TSO', 'TXN', 'TXT', 'HSY', 'TRV', 'TMO', 'TIF', 'TWX', 'TWC', 'TJK', 'TMK', 'TSS', 'TSCO', 'RIG', 'TRIP', 'FOXA', 'TSN', 'TYC', 'UA', 'UNP', 'UNH', 'UPS', 'URI', 'UTX', 'UHS', 'UNM', 'URBN', 'VFC', 'VLO', 'VAR', 'VTR', 'VRSN', 'VZ', 'VRTX', 'VIAB', 'V', 'VNO', 'VMC', 'WMT', 'WBA', 'DIS', 'WM', 'WAT', 'ANTM', 'WFC', 'WDC', 'WU', 'WY', 'WHR', 'WFM', 'WMB', 'WEC', 'WYN', 'WYNN', 'XEL', 'XRX', 'XLNX', 'XL', 'XYL', 'YHOO', 'YUM', 'ZBH', 'ZION', 'ZTS']
single_url = '''https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=symzzqw2qe&apikey=E7Y3V4N387Y6AHNS&datatype=csv'''


def get_extract(url, sym):
    '''Get Url using the API Url and Key'''
    sym_url = url.replace("symzzqw2qe", sym)
    uClient = urlopen(sym_url)
    #print(sym_url)
    page = uClient.read()
    uClient.close()
    #print(page)
    return page

def percent_change(today, yesterday):

    #convert to float
    today_float = float(today)
    yesterday_float = float(yesterday)

    #get percent change
    pc = ((today_float - yesterday_float)/(yesterday_float))*100

    #convert to string
    
    return pc


def get_info(sym_info):
    '''Parse the page_html text to extract 
    Today_Open, Yesterday_Open, then calc
    Percent Change'''
    lines = list()
    lines = sym_info.decode().split('\n')
    
    #Get Today and Yesterday info
    today = lines[1]
    yesterday = lines[2]

    #Get today and yesterday high
    today_high = today.split(",")[1]
    yesterday_high = yesterday.split(",")[1]

    day_change = percent_change(today_high, yesterday_high)

    co_info = list()
    co_info = [today_high, yesterday_high, day_change]
    #print(today_high, yesterday_high, day_change)
    return co_info

def list_to_dict(my_list, symbol):
    '''Conver List to Dic'''
    my_dict = dict()
    my_dict = {"Name": symbol, 
                "Today_Open" : my_list[0],
                "Yesterday_Open" : my_list[1],
                "Percent_Change" : my_list[2]}

    return my_dict


def dict_to_csv(csv_name, my_dict_list):

    with open(csv_name, 'w', newline='') as f:
        dict_writer = csv.DictWriter(f, fieldnames = my_dict_list[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(my_dict_list)
    f.close()
    return csv_name


def df_to_csv(csv_name, df):
    '''Get Top Ten to CSV'''
    with open(csv_name, 'w') as f:
        df.to_csv(csv_name, header=True)
    f.close()
        
def get_top_ten(csv_file):
    '''Get top ten results'''

    df = pd.read_csv(csv_file)
    df_sym = df[["Name","Today_Open", "Yesterday_Open", "Percent_Change"]]
    result = df_sym.sort_values(by=["Percent_Change"], ascending=False)
    result_head = result.head(10)

    return result_head
    


def main(companies):
    list_of_companies = list()
    for company in companies:
        co_string = str(company)
        print("working on " + co_string)
        try:
            sym_string = get_extract(single_url,co_string)
            #Company info is a list
            company_info = get_info(sym_string)
        except:
            company_info = [co_string, "unknown", "unknown", "unknown"]
        
        co_dict = list_to_dict(company_info, co_string)
        list_of_companies.append(co_dict)
        print(co_dict)
        #dict_to_csv("stock_info.csv", list_of_companies)
        time.sleep(2)
    sp500_csv = dict_to_csv("stock_info.csv", list_of_companies)

    top_ten = get_top_ten(sp500_csv)
    df_to_csv("Todays_Top_Ten.csv", top_ten)

    print(top_ten)

        # sym_string = get_extract(single_url,str(company))
        # print(sym_string)
        # company_info = get_info(sym_string)
        # print(company_info)


if __name__ == "__main__":
    test_batch = co[:]
    print(test_batch)
    main(test_batch)
