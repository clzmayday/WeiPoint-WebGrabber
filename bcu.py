from bs4 import BeautifulSoup
import csv, os
import urllib.request

class bcu:
    def run(self):

        print("Please Tell me What Year do you want to extract? (e.g. 2020)")
        year = int(input())
        print("Please Tell me What Month do you want to extract? (e.g. 2)")
        month = int(input())
        url = "https://www.bcu.ac.uk/news-events/calendar?year="+year+"&month="+month
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
        req = urllib.request.Request(url=url, headers=header)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        soup = BeautifulSoup(html, features="html.parser")
        articles = soup.find_all('article', attrs={""})
        content = []
