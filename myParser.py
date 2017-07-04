import json
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
parsed_html = BeautifulSoup(open("new.html"),"lxml")
table = parsed_html.body.find('table', attrs={'id':'myTable'})
data = []
for row in table.findAll("tr"):
	cells = row.findAll("td")
	data_item=[]
	for item in cells:
		data_item.append(item.text)
	data.append(data_item)
json_data=[]
for rows in data:
	ans = rows[0]+" is lead by "+rows[1]+" and uses "+rows[2];
	que = "can you tell me about "+rows[0]+"?"
	json_item=[que,ans]
	json_data.append(json_item)
to_dump={
	'statements': json_data
}
json_str=json.dumps(to_dump)
print(json_str)
with open('data.json', 'w') as f:
  json.dump(json_str, f, ensure_ascii=False)