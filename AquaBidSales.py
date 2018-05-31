import re
import urllib
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


# opening up connection, grabbing page
def getWebpage(my_url):
    req = urllib.request.Request(my_url, headers={'User-Agent' : "Magic Browser"}) # Without magic browser, we cannot read the page
    uClient = uReq(req)
    page_html = uClient.read()
    uClient.close() # close client to save processes
    return soup(page_html, "html.parser")   # returns the html for the webpage as a soup object


# fetch the sellers
def getSeller(page_soup):
    for link in page_soup.find_all('a'):    # finds all <a> tags
        seller = (link.get('href')) # get the href value
        if seller is None:  # check for a NoneType and do nothing if found
            continue
        elif "viewseller" in seller:    # check for substring in string and add to library if found
            fullListing.setdefault('seller', []).append(seller.split("viewseller&",1)[1]) # clean up string to only include seller name


# fetch the listing items
def getItem(page_soup):
    itemList = []
    for num, link in enumerate(page_soup.find_all('a')):    # finds all <a> tags and also numbers them in order
        title = (link.getText('href'))  # get the href text value (includes item name followed by seller name)
        title = title.replace('href', '')   # remove the word 'href' from the string
        itemList.append(title)  # add the string to the itemList
        if itemList[num] in fullListing['seller']: # check if the seller name is listed next to the item
            fullListing.setdefault('item', []).append(itemList[num-1])  # add only the item to the dictionary

# fetch the item prices
def getPrice(page_soup):

    for column in page_soup.find_all('td'):
        price = column.getText('font')

        lessCheapItem = re.match(r'\d\d\S\d\d', price, re.I)    # item that costs >$10
        cheaperItem = re.match(r'\d\S\d\d', price, re.I)    # item that costs <$10
        if lessCheapItem or cheaperItem:    # check if string is a price listing
            fullListing.setdefault('price', []).append(price)   # add price to dictionary

# output information
fullListing = {}
page_soup = getWebpage('http://www.aquabid.com/cgi-bin/auction/auction.cgi?liveplantsm')    # url for AquaBid's moss section
page_soups = getWebpage('http://www.aquabid.com/cgi-bin/auction/auction.cgi?liveplantsm&&&&&&&page=1&pb=0')
getSeller(page_soup)
getItem(page_soup)
getPrice(page_soup)
for num, item in enumerate(fullListing['item']):    # loop to print out dictionary listings
    print ("Listing #" + str(num+1) + ":")
    print ("Item:    " + fullListing['item'][num])
    print ("Price:   " + fullListing['price'][num])
    print ("Seller:  " + fullListing['seller'][num])
    print ()
