import urllib
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'http://www.aquabid.com/cgi-bin/auction/auction.cgi?liveplantsm'

# opening up connection, grabbing page
req = urllib.request.Request(my_url, headers={'User-Agent' : "Magic Browser"})
uClient = uReq(req)
page_html = uClient.read()
uClient.close()

# put everything inside page_soup
page_soup = soup(page_html, "html.parser")

# fetch the seller names
for link in page_soup.find_all('a'):
    seller = (link.get('href'))
    if seller is None:
        continue
    elif "viewseller" in seller:
        print (seller.split("viewseller&",1)[1])
