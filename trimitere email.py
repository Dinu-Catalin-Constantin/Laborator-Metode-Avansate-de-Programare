import requests
from bs4 import BeautifulSoup
import smtplib
from apscheduler.schedulers.blocking import BlockingScheduler
from hashlib import new

def data_scraping():
    req = requests.get(r"https://www.emag.ro/monitor-curbat-gaming-led-va-samsung-27-wqhd-displayport-1ms-144hz-freesync-negru-lc27g55tqwrxen/pd/DCV19TMBM/?")
    soup=BeautifulSoup(req.text, "html-parser")
    price=soup.find('p', attrs={"class": "product-new-price"}).text
    new_price=price[0:5]
    new_price=new_price.replace(".", "")
    print(new_price)

sender='data_scraping@coneasorin.ro'
subject='Pretul a scazut la:'
to_addr_list = ['coneasorin@outlook.com']
cc_addr_list = ['']
def sendemail(sender,message, subject,to_addr_list, cc_addr_list=[]):
    try:
        smtpserver='mail.x-it.ro:26'
 
        header = 'From: %s\n' % sender
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header + message
 
        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(sender,"stiinte217_2022")
        problems = server.sendmail(sender, to_addr_list, message)
        server.quit()
        return True
    except:
        return False

sendemail(sender, "Schimbare de pret", subject, to_addr_list, cc_addr_list)