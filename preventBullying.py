
import string
from youtube_comment_scraper_python import *
import time
import twint

"""
c = twint.Config()
c.Search = ['Taylor Swift']       # topic
c.Limit = 500      # number of Tweets to scrape
twint.run.Search(c)
print(c)
"""


def youtubeParse(url: string) -> list:
    youtube.open(url)
    dictionary = youtube.video_comments()
    list = []
    for key in dictionary["body"]:
        list.append(key["Comment"])
    print(list)

