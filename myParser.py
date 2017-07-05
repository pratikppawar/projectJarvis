import json
import re
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
parsed_html = BeautifulSoup(open("sampleTable.html"),"lxml")
table = parsed_html.body.find('table', attrs={'class':'details'})

heading_data = []
heading = table.findAll("th")
for item in heading:
	heading_data.append(item.text.lower())
#heading_data consists of the table headings
#print(heading_data)

data = []
for row in table.findAll("tr")[1:]:
	cells = row.findAll("td")
	data_item=[]
	for item in cells:
		data_item.append(item.text)
	data.append(data_item)

#data consists of the table values
#print (data)
json_data=[]
for rows in data:
	que = "can you tell me about "+rows[0]+"?"
	ans = rows[0]+" is lead by "+rows[2]+" and uses "+rows[1];
	json_item=[que,ans]
	json_data.append(json_item)
	#team and lead rel
	que = "Who leads "+rows[0]+"?"
	ans = rows[0]+" is lead by "+rows[2];
	json_item=[que,ans]
	json_data.append(json_item)
	#tech and lead rel
	que = "Which technology does "+rows[2]+" work on?"
	ans = rows[2]+" work on "+rows[1];
	json_item=[que,ans]
	json_data.append(json_item)
	#tech and team rel
	que = "Which technology does "+rows[0]+" uses?"
	ans = rows[0]+" uses "+rows[1];
	json_item=[que,ans]
	json_data.append(json_item)
	#team lead
	que = "Who is "+rows[2]+"?"
	ans = rows[2]+" is a FTL";
	json_item=[que,ans]
	json_data.append(json_item)
	
to_dump={
	'statements': json_data
}
json_str=json.dumps(to_dump)
with open('data.json', 'w') as f:
  json.dump(to_dump, f, ensure_ascii=False)

 #parseQnA is the function called using REST on sendFormat button click with msg as data
def parseQnA(msg):
	send_format_json_data = []
	for data_item in data:
		new_str = msg.lower()
		for head_item in heading_data:
			#print(data_item[heading_data.index(head_item)])
			new_str = str.replace(new_str,'<'+head_item+'>',data_item[heading_data.index(head_item)])
		send_format_json_data.append(new_str)
		#print(new_str)
	return(send_format_json_data)
	#you can add this json in this file or back in app.py
	