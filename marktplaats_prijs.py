import bs4, requests

def vindMarktplaatsPrijs(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#vip-ad-price-container > span')
    return elems[0].text.strip()




prijs = vindMarktplaatsPrijs('https://www.marktplaats.nl/a/kleding-heren/schoenen/m1275796521-meindl-jungle-panama-maat-46-nieuw.html?c=3c1f5dcc18d02a99040ca8de656940d2&previousPage=lr')
print('De prijs is ' + prijs)
                    
