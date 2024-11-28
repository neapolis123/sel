from seleniumbase import SB
from bs4 import BeautifulSoup


url ='https://finviz.com/quote.ashx?t=DRUG&p=d'
with SB(uc=True) as sb:    
    sb.activate_cdp_mode(url)
    sb.sleep(2)
    table = sb.cdp.find('table#news-table')
    print('table')
    print(table)
    print(type(table))
    soup = BeautifulSoup(table.get_html(),'html.parser')
    #fdfd