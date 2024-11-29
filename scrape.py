import time as t
from seleniumbase import SB
from bs4 import BeautifulSoup
import traceback

proxy= 'pmzeuqsa:1xhaurrbes2z@207.244.217.160:6712'
proxy = "pmzeuqsa-9:1xhaurrbes2z@191.228.216.36:80"
#proxy='scraperapi:21abcd3d2600b56cf5d89666f02326b1@proxy-server.scraperapi.com:8001'

with SB(uc=True) as sb:
    iterations = 0
    while(True):
      try:
            start = t.time()
            url = "https://visas-fr.tlscontact.com/country/tn/vac/tnTUN2fr"
            sb.activate_cdp_mode(url)
            sb.sleep(15)
            #sb.cdp.flash('button.osano-cm-dialog__close', duration=2)
            #sb.cdp.click('button.osano-cm-dialog__close')  # closes the cookies banner to make the next button visible on my laptop
            #sb.cdp.highlight('button#btn-navigation-login')
            # sb.cdp.flash("SE CONNECTER",duration=4,pause=2)
            sb.cdp.click("SE CONNECTER")
            # sb.cdp.flash('button.tls-button',duration=4,pause=2)
            # sb.cdp.click('button.tls-button')
            sb.cdp.type('#email-input-field', 'contact@visas.tn')
            sb.cdp.type('input[id=password-input-field]', 'Spirospiro22!')
            sb.cdp.click('#btn-login')  # logs in
            sb.cdp.click_if_visible('button#refresh-button')  # sometimes a 'server is overworked' button needed to be clicked to refresh
            sb.sleep(6)
            sb.cdp.open('https://visas-fr.tlscontact.com/17601423/workflow/appointment-booking?location=tnSFA2fr')
            sb.sleep(6)
            #sb.cdp.open('https://citizen.visas-fr.tlscontact.com/groups/17601423/bookings/available-slots?start=20241126&labels=pta,premium,walkin,pv,spv,ptaw&location=tnSFA2fr')
            sb.sleep(10)
            if sb.cdp.is_element_present('p:contains("Aucun rendez-vous disponible. Veuillez réessayer ultérieurement.")'):
                  sb.cdp.click('span:contains("décembre 2024")') 
                  table = sb.cdp.find_element('div.snap-x.overflow-auto.whitespace-nowrap.pb-4.pt-6') # get the table 
            #sb.cdp.click('button:contains("Sélectionner")')
            table = BeautifulSoup(table.get_html(),'lxml')
            #print(table.prettify())  
            print('test done')
            days = table.find_all('div',{'class':['group', 'inline-block']})
            print(days)
            for day in days:
                  day_number = day.find('span',class_="font-bold")
                  available_appointments = [apoint.text for apoint in day.find_all('button',{'disabled':False}) ]
                  print(available_appointments)
                  print(day_number)
            sb.cdp.click('div[role=listitem')
            sb.cdp.click('Se déconnecter')
            print('successful disconnection')
            print(f'took {start - t.time()}')
            iterations+=1
            print(iterations)
      except Exception:
          print(traceback.format_exc()) 
      #'p:contains("Aucun rendez-vous disponible. Veuillez réessayer ultérieurement.")'
      #'span:contains("décembre 2024")'
      #'div[class=snap-x overflow-auto whitespace-nowrap pb-4 pt-6]'
