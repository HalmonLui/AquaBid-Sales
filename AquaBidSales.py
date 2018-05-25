import urllib
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


# opening up connection, grabbing page
def getWebpage(my_url):
    req = urllib.request.Request(my_url, headers={'User-Agent' : "Magic Browser"})
    uClient = uReq(req)
    page_html = uClient.read()
    uClient.close()
    return soup(page_html, "html.parser")


# fetch the seller
def getSeller(page_soup):
    for link in page_soup.find_all('a'):
        seller = (link.get('href'))
        if seller is None:
            continue
        elif "viewseller" in seller:
            fullListing.setdefault('seller', []).append(seller.split("viewseller&",1)[1])


# fetch the listing items
def getItem(page_soup):
    itemList = []
    for num, link in enumerate(page_soup.find_all('a')):
        title = (link.getText('href'))
        title = title.replace('href', '')
        itemList.append(title)
        if itemList[num] in fullListing['seller']:
            fullListing.setdefault('item', []).append(itemList[num-1])


# output information
fullListing = {}

page_soup = getWebpage('http://www.aquabid.com/cgi-bin/auction/auction.cgi?liveplantsm')
getSeller(page_soup)
getItem(page_soup)
for num, item in enumerate(fullListing['item']):
    print ("Listing #" + str(num+1) + ":")
    print ("Item:    " + fullListing['item'][num])
    print ("Seller:  " + fullListing['seller'][num])
    print ()
