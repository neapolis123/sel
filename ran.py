from seleniumbase import SB
from bs4 import BeautifulSoup


url ='https://pixelscan.net/'
#url='https://whatismyipaddress.com/'
proxy = "pmzeuqsa:1xhaurrbes2z@154.36.110.199:6853"
#proxy='scraperapi:21abcd3d2600b56cf5d89666f02326b1@proxy-server.scraperapi.com:8001'
with SB(uc=True) as sb: 
    tz_params = {'timezoneId': 'America/New_York'}
    sb.driver.execute_cdp_cmd('Emulation.setTimezoneOverride', tz_params)
    sb.activate_cdp_mode(url)
    #sb.cdp.clear_cookies()
    sb.sleep(200)
