"""import twint

c = twint.Config()

c.Search = ['Taylor Swift']       # topic
c.Limit = 500      # number of Tweets to scrape


twint.run.Search(c)

print(c)"""

from youtube_comment_scraper_python import *
import time

youtube.open("https://www.youtube.com/watch?v=UtRMiOPrxyA")
print(youtube.video_comments())