import json
import requests
import os
from datetime import datetime
import send_mail

with open("feeds.json", "r" ,encoding="utf-8") as fi: 
	feeds = json.loads(fi.read())

for k, v in feeds.items():  
	try: 
		if "proxy" in v.keys():
			r = requests.get(v["url"],proxies=v["proxy"])
		else:
			r = requests.get(v["url"])
		content = r.text 
		fname = v["format"] 
		fname = fname.replace("TIMESTAMP", datetime.strftime(datetime.now(), "%Y_%m_%d_%H_%M_%S")) 
		with open(os.path.join(v["output_path"], fname), "w",encoding="utf-8") as fo: 
			fo.write(content) 
	except Exception as e: 
		with open("rss_feed_error.log", "a") as fo: 
			body="Could not retrieve rss feed for \"" + k + "\", at" + datetime.strftime(datetime.now(), " %Y/%m/%d_%H:%M:%S ") + str(e)
			fo.write(body+ "\n" )
			send_mail.send_email("aalabrash18@ku.edu.tr","RSS",body+"\n")


