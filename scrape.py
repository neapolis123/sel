import time as t
from seleniumbase import SB

with SB(uc=True) as sb:
    url = "https://visas-fr.tlscontact.com/country/tn/vac/tnTUN2fr"
    sb.activate_cdp_mode(url)
    sb.sleep(1)
    sb.cdp.flash('button.osano-cm-dialog__close', duration=2)
    sb.cdp.click('button.osano-cm-dialog__close')  # closes the cookies banner to make the next button visible on my laptop
    sb.cdp.highlight('button#btn-navigation-login')
    # sb.cdp.flash("SE CONNECTER",duration=4,pause=2)
    sb.cdp.click("SE CONNECTER")
    # sb.cdp.flash('button.tls-button',duration=4,pause=2)
    # sb.cdp.click('button.tls-button')
    sb.cdp.type('#email-input-field', 'contact@visas.tn')
    sb.cdp.type('input[id=password-input-field]', 'Spirospiro22!')
    sb.cdp.click('#btn-login')  # logs in
    sb.cdp.click_if_visible('button#refresh-button')  # sometimes a 'server is overworked' button needed to be clicked to refresh
    sb.sleep(5)
    sb.cdp.highlight('button:contains("Sélectionner")')  # keeps crashing here saying it's not visible
    sb.cdp.click('button:contains("Sélectionner")')  # keeps crashing here saying it's not visible
    sb.sleep(20)
    print('test done')
