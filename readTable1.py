from bs4 import BeautifulSoup

html = """
  <table class="details">
<tr>
<th> Team Name</th>
<th>Technology</th>
<th>Team lead</th>
</tr>
<tr>
<td>Team Neo</td>
<td>Java Spring Boot</td>
<td>Peter Parkar</td>
</tr>

<tr>
<td>Team Trinity</td>
<td>Java Play</td>
<td>Peter Quil</td>
</tr>

<tr>
<td>Team Moepheus</td>
<td>Java Spring, Hibernate</td>
<td>Peter Petrelli</td>
</tr>

<tr>
<td>Team Smith</td>
<td>Java Swing</td>
<td>Peter Snow</td>
</tr>

</table>
  
  """

soup = BeautifulSoup(html, "html.parser")
table = soup.find("table", attrs={"class":"details"})

# The first tr contains the field names.
headings = [th.get_text() for th in table.find("tr").find_all("th")]

datasets = []
for row in table.find_all("tr")[1:]:
    #dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
	dataset = zip([td.get_text() for td in row.find_all("td")])
    datasets.append(dataset)
	
for dataset in datasets:
    sentanse = []
    for field in dataset:
        sentanse.append(field)
    print ("{0} uses {1} lead by {2}".format(sentanse[0], sentanse[1], sentanse[2]))
        