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


# fetch the seller
sellerList = []
for link in page_soup.find_all('a'):
    seller = (link.get('href'))
    if seller is None:
        continue
    elif "viewseller" in seller:
        sellerList.append(seller.split("viewseller&",1)[1])


# fetch the listing items
itemList = []
for num, link in enumerate(page_soup.find_all('a')):
    title = (link.getText('href'))
    itemList.append(title)
    if itemList[num] in sellerList:
        print ("Item: " + itemList[num-1])
        print ("Seller: " + itemList[num])
        print ()
