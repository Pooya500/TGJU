import requests
from bs4 import BeautifulSoup as bs


class PriceCollector:
    def __init__(self):
        self.coin_price = []
        self.coinb_price = []
        self.coinnim_price = []
        self.coinrob_price = []
        self.coingerami_price = []
        self.dollar_price = []
        self.euro_price = []
        self.pound_price = []
        self.derham_price = []
        self.lira_price = []
        self.gold_18_price = []
        self.goldons_price = []
        self.goldmesghal_price = []

        # url = 'https://www.tgju.org/'
        urlg18 = 'https://www.tgju.org/profile/geram18'
        urlgm = 'https://www.tgju.org/profile/mesghal'
        urlgo = 'https://www.tgju.org/profile/ons'
        urlcoin = 'https://www.tgju.org/profile/sekee'
        urlcoinb = 'https://www.tgju.org/profile/sekeb'
        urlnim = 'https://www.tgju.org/profile/nim'
        urlrob = 'https://www.tgju.org/profile/rob'
        urlgerami = 'https://www.tgju.org/profile/gerami'
        urldollar = 'https://www.tgju.org/profile/price_dollar_rl'
        urleuro = 'https://www.tgju.org/profile/price_eur'
        urlpound = 'https://www.tgju.org/profile/price_gbp'
        urlderham = 'https://www.tgju.org/profile/price_aed'
        urllira = 'https://www.tgju.org/profile/price_try'

        # r = requests.get(url)
        rg18 = requests.get(urlg18)
        rgm = requests.get(urlgm)
        rgo = requests.get(urlgo)
        rc = requests.get(urlcoin)
        rcb = requests.get(urlcoinb)
        rcn = requests.get(urlnim)
        rcr = requests.get(urlrob)
        rcg = requests.get(urlgerami)
        rcd = requests.get(urldollar)
        rce = requests.get(urleuro)
        rcp = requests.get(urlpound)
        rcde = requests.get(urlderham)
        rcl = requests.get(urllira)

        # self.soup = bs(r.content, features="lxml")
        self.soupg18 = bs(rg18.content, features="lxml")
        self.soupgm = bs(rgm.content, features="lxml")
        self.soupgo = bs(rgo.content, features="lxml")

        self.soupcoin = bs(rc.content, features="lxml")
        self.soupcoinb = bs(rcb.content, features="lxml")
        self.soupcoinnim = bs(rcn.content, features="lxml")
        self.soupcoinrob = bs(rcr.content, features="lxml")
        self.soupcoingerami = bs(rcg.content, features="lxml")

        self.soupdollar = bs(rcd.content, features="lxml")
        self.soupeuro = bs(rce.content, features="lxml")
        self.souppound = bs(rcp.content, features="lxml")
        self.soupderham = bs(rcde.content, features="lxml")
        self.souplira = bs(rcl.content, features="lxml")

    def coin_collector(self):
        coin_info = self.soupcoin.find('tbody', attrs={'class': 'table-padding-lg'})
        self.coin_price = coin_info.find('td', attrs={'class': 'text-left'}).text

        coinb_info = self.soupcoinb.find('tbody', attrs={'class': 'table-padding-lg'})
        self.coinb_price = coinb_info.find('td', attrs={'class': 'text-left'}).text

        coinnim_info = self.soupcoinnim.find('tbody', attrs={'class': 'table-padding-lg'})
        self.coinnim_price = coinnim_info.find('td', attrs={'class': 'text-left'}).text

        coinrob_info = self.soupcoinrob.find('tbody', attrs={'class': 'table-padding-lg'})
        self.coinrob_price = coinrob_info.find('td', attrs={'class': 'text-left'}).text

        coingerami_info = self.soupcoingerami.find('tbody', attrs={'class': 'table-padding-lg'})
        self.coingerami_price = coingerami_info.find('td', attrs={'class': 'text-left'}).text

    def currency_collector(self):
        dollar_info = self.soupdollar.find('tbody', attrs={'class': 'table-padding-lg'})
        self.dollar_price = dollar_info.find('td', attrs={'class': 'text-left'}).text

        euro_info = self.soupeuro.find('tbody', attrs={'class': 'table-padding-lg'})
        self.euro_price = euro_info.find('td', attrs={'class': 'text-left'}).text

        pound_info = self.souppound.find('tbody', attrs={'class': 'table-padding-lg'})
        self.pound_price = pound_info.find('td', attrs={'class': 'text-left'}).text

        derham_info = self.soupderham.find('tbody', attrs={'class': 'table-padding-lg'})
        self.derham_price = derham_info.find('td', attrs={'class': 'text-left'}).text

        lira_info = self.souplira.find('tbody', attrs={'class': 'table-padding-lg'})
        self.lira_price = lira_info.find('td', attrs={'class': 'text-left'}).text

    def gold_collector(self):
        # Home Page
        # gold18_info = self.soup.find('li', attrs={'id': 'l-geram18'})
        # self.gold_18_price = gold18_info.find('span', attrs={'class': 'info-price'}).text
        #
        # goldons_info = self.soup.find('li', attrs={'id': 'l-ons'})
        # self.goldons_price = goldons_info.find('span', attrs={'class': 'info-price'}).text
        #
        # goldmesghal_info = self.soup.find('li', attrs={'id': 'l-mesghal'})
        # self.goldmesghal_price = goldmesghal_info.find('span', attrs={'class': 'info-price'}).text


        gold18_info = self.soupg18.find('tbody', attrs={'class': 'table-padding-lg'})
        self.gold_18_price = gold18_info.find('td', attrs={'class': 'text-left'}).text


        goldons_info = self.soupgo.find('tbody', attrs={'class': 'table-padding-lg'})
        self.goldons_price = goldons_info.find('td', attrs={'class': 'text-left'}).text

        goldmesghal_info = self.soupgm.find('tbody', attrs={'class': 'table-padding-lg'})
        self.goldmesghal_price = goldmesghal_info.find('td', attrs={'class': 'text-left'}).text


