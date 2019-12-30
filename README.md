# rss-feed-retriever

### Crontab configuration

Getting the feeds every hour

```
crontab -e
```
Then write
```
0 * * * * /bin/sh /scratch/RSSFeed/rss-feed-retriever/rss_feed.sh
```

Verify if crontab works
```
crontab -l
```


### New rss resources can be added feeds.json file

```
{
	"scmp": {
		"url": "https://www.scmp.com/rss/2/feed",
		"output_path": "/scratch/RSSFeed/scmp",
		"format": "scmp_rss_TIMESTAMP.xml"
	}, 
	"evrensel": {
		"url": "https://www.evrensel.net/rss/haber.xml",
		"output_path": "/scratch/RSSFeed/evrensel",
		"format": "evrensel_rss_TIMESTAMP.xml"
	}
}
```

Where

- `url` is the url of rss feed
- `output_path` is the folder where the script will save the feeds (.xml files)
- `format` is the name format of this files, `scmp_rss_TIMESTAMP` for example will be saved as `scmp_rss_2019_12_13_18_00_03.xml`
