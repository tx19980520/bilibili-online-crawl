import time
import os
while True:
    cmd = "scrapy crawl bilibiliOnline -t json -o ./data/%s.json"%(str(int(time.time())))
    if(time.localtime().tm_hour>6 and time.localtime().tm_hour<23):
        os.system(cmd)
    time.sleep(300)
