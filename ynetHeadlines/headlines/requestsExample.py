

# Installation:
## pip3 install requests
## pip3 install beatifulsoup4

import requests
from bs4 import BeautifulSoup

def executeRequests(url):
    # simple usage
    r = requests.get(url)
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)
    print(r.content)


    # executing request with a custom user agent
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    r1 = requests.get(url, headers=headers)
    print(r1.status_code)

    # executing request which disables SSL Certificate verification
    r2 = requests.get(url, headers=headers, verify=False)
    print(r2.status_code)

    # executing request with a timeout of 30 seconds - the time to wait for the server to send data before giving up
    r3 = requests.get(url, headers=headers, verify=False, timeout=30)
    print(r3.status_code)


def executeRequestsAndParseContent(url):
    r = requests.get(url)
    content = r.content

    soupContent = BeautifulSoup(content, 'html.parser')
    links = soupContent.findAll('a')
    for l in links:
        if 'href' not in l.attrs:
            continue

        print("###")

        if l.string:
            print("name", l.string)

        if 'http' in l.attrs['href']:
            print("link", l.attrs['href'])
        else:
            # handling relative links
            print("link", url + l.attrs['href'])


def executeRequestsAndParseHeadlineContent(url):
    r = requests.get(url)
    content = r.content
    titlesContent = list()
    subtitlesContent = list()

    soupContent = BeautifulSoup(content, 'html.parser')

    titles = soupContent.findAll("div", {"class": "title"})
    for t in titles:
        print(t.text + "\n")
        titlesContent.append(t.text)

    print("#####")

    subtitles = soupContent.findAll("div", {"class": "sub_title"})
    for s in subtitles:
        print(s.text + "\n")
        subtitlesContent.append(s.text)

    fullContent = list()
    for i in range(len(titlesContent)):
        if len(subtitlesContent) <= i:
            break
        fullContent.append({"title": titlesContent[i], "subtitle": subtitlesContent[i]})

    print(fullContent)
    return fullContent


if __name__ == "__main__":
    url = "https://www.ynet.co.il"
    #executeRequestsAndParseContent(url)
    #executeRequestsAndParseContent(url)
    executeRequestsAndParseHeadlineContent(url)
