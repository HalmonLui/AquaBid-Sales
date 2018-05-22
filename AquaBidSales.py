import urllib
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'http://www.aquabid.com/cgi-bin/auction/auction.cgi?liveplantsm'

# opening up connection, grabbing page
req = urllib.request.Request(my_url, headers={'User-Agent' : "Magic Browser"})
uClient = uReq(req)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
