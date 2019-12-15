import json
import requests
import os
from datetime import datetime

with open("feeds.json", "r" ) as fi: 
	feeds = json.loads(fi.read())

for k, v in feeds.items():  
	try: 
		r = requests.get(v["url"])  
		content = r.text 
		fname = v["format"] 
		fname = fname.replace("TIMESTAMP", datetime.strftime(datetime.now(), "%Y_%m_%d_%H_%M_%S")) 
		with open(os.path.join(v["output_path"], fname), "w") as fo: 
			fo.write(content) 
	except Exception as e: 
		with open("rss_feed_error.log", "a") as fo: 
			fo.write("Could not retrieve rss feed for \"" + k + "\", at" + datetime.strftime(datetime.now(), " %Y/%m/%d_%H:%M:%S ") + str(e) + "\n" )


