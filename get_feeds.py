import json
import requests
import os
from datetime import datetime
import send_mail
from re import findall
import traceback

def get_IPs():
    r = requests.get('https://www.sslproxies.org/')                                                                                                                          
    matches = findall(r"<td>\d+.\d+.\d+.\d+</td><td>\d+</td>", r.text)                                                                                                       
    revised = [m.replace('<td>', '') for m in matches]                                                                                                                       
    sockets = [s[:-5].replace('</td>', ':') for s in revised]                                                                                                                
    return sockets


with open("feeds.json", "r" ,encoding="utf-8") as fi: 
	feeds = json.loads(fi.read())

r=None
for k, v in feeds.items():  
	try: 
		if k =="scmp":
			sockets= get_IPs()
			r_test=None
			for x in sockets: 
				try: 
					r_test=requests.request("GET",url=v["url"],proxies={"https":"https://"+x,"'http'":'http://'+x},timeout=3.0) 
					if r_test.status_code==200: 
						r=r_test
						break 
				except Exception as e: 
					pass 
		else:
			r = requests.get(v["url"])

		content = r.text 
		fname = v["format"] 
		fname = fname.replace("TIMESTAMP", datetime.strftime(datetime.now(), "%Y_%m_%d_%H_%M_%S")) 
		with open(os.path.join(v["output_path"], fname), "w",encoding="utf-8") as fo: 
			fo.write(content) 
	except Exception as e: 
		body="Could not retrieve rss feed for \"" + k + "\", at" + datetime.strftime(datetime.now(), " %Y/%m/%d_%H:%M:%S ") + str(e)
		with open("rss_feed_error.log", "a") as fo: 
			fo.write(body+ "\n" )
		send_mail.send_email("aalabrash18@ku.edu.tr","RSS",body+"\n"+traceback.format_exc())


