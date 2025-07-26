# coding: utf-8
import requests
import pandas as pd
import json
import datetime as dt
url = "https://api.cnyes.com/media/api/v1/newslist/category/headline"
payload = {
	"page":2,
	"limit":30,
	"isCategoryHeadline":1,
	"startat":int((dt.datetime.today() - dt.timedelta(days = 11)).timestamp()),
	"endAt":int(dt.datetime.today().timestamp())
}
res = requests.get(url, params = payload)
jd = json.loads(res.text)
df = pd.DataFrame(jd['items']['data'])
df = df[['newsId', 'title', 'summary']]
df['link'] = df['newsId'].apply(lambda x: 'https://m.cnyes.com/news/id/' + str(x))
df.to_csv('news.csv', encoding = 'utf-8-sig')
df