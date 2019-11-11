from bs4 import BeautifulSoup
import csv, os
import urllib.request


url = 'https://www.birmingham.ac.uk/events/index.aspx'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
req = urllib.request.Request(url=url, headers=header)
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8')
soup = BeautifulSoup(html,features="html.parser")
articles = soup.find_all('article', attrs={"class":"event media media--flipped"})
content = []
def date_parse(content):
    begin = ""
    end = ""
    bracket = False
    isbegin = True

    for word in content:
        if isbegin:
            if (not bracket) and (word == "-"):
                isbegin = False
                continue

            if word == "(":
                bracket = True
            elif word == ")":
                bracket = False
            begin += word
        else:
            end += word
    if len(end) <= 2:
        end = " N/A"
    return [begin[:-1],end[1:]]

def link_parse(content):
    if content.startswith("http"):
        return content
    else:
        return "https://www.birmingham.ac.uk" + content

for article in articles:
    a = dict()
    soup = BeautifulSoup(str(article), features="html.parser")
    a["name"] = article.a.text
    a["link"] = link_parse(str(article.a).split("\"")[1])
    detail_head = [i.text.lower() for i in soup.find_all('dt')]
    full_head = ['dates', 'location', 'category']
    details = soup.find_all('dd')
    count = 0
    for f in full_head:
        if f not in detail_head:
            if f == 'dates':
                a['start_date'] = 'N/A'
                a['end_date'] = 'N/A'
            else:
                a[f] = 'N/A'
        else:
            if f == 'dates':
                good_date = date_parse(details[count].text)
                a["start_date"] = good_date[0]
                a["end_date"] = good_date[1]
            else:
                a[f] = details[count].text
            count += 1

    content.append(a)

csv_head = ["name", "start_date", "end_date", "location", "category", "link"]
path = os.getcwd()+"/event.csv"
if os.path.exists(path):
    os.remove(path)
with open(path, mode='w', newline='') as event:
    writer = csv.writer(event)
    writer.writerow(csv_head)
    for row in content:
        row_content = []
        for column in csv_head:
            row_content.append(row[column])
        writer.writerow(row_content)
