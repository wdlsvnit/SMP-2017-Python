#python file to extract lyrics from the url

#Uses Requests module to get html
#Uses BeautifulSoup to scrape

import os,bs4,requests

def EgetLyrics(url):
    
    # http://stackoverflow.com/questions/33174804/python-requests-getting-connection-aborted-badstatusline-error
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    
    lyricSoup = bs4.BeautifulSoup(res.text,"html.parser")
    Babel = lyricSoup.find_all("div",{"class":""})
    
    lyrics = ""
    for ly in Babel:
        lyrics += ly.text
       
    return lyrics
    
    

def HgetLyrics(url):
    
    # http://stackoverflow.com/questions/33174804/python-requests-getting-connection-aborted-badstatusline-error
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    
    lyricSoup = bs4.BeautifulSoup(res.text,"html.parser")
    Babel = lyricSoup.select("#lyric > p")
    
    lyrics = ""
    for ly in Babel:
        lyrics += ly.get_text(separator=u"\n")
        lyrics += "\n\n"
     
    return lyrics
