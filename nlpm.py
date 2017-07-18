from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')
NN=[]
PRP=[]
JJ=[]
WP=[]
res = nlp.annotate("What is my current status? What is status of issue EX1? What is issue Ex2 status? What is jira issue EX3 status?",
                   properties={
                       'annotators': 'depparse',
                       'outputFormat': 'json',
                       'timeout': 1000,
                   })
sentences=res.get("sentences")
for s in sentences:
    tokens=s.get("tokens")
    for item in tokens:
        #print(item.get("word") +"|"+ item.get("pos"))
        if("NN" == item.get("pos")):
            NN.append(item.get("word"))
        elif("PRP$" == item.get("pos")):
            PRP.append(item.get("word"))
        elif("JJ" == item.get("pos")):
            JJ.append(item.get("word"))
        elif("WP" == item.get("pos")):
            WP.append(item.get("word"))
print("all NN")
for i in NN:
    print(i)
print("----------------------------------------")
print("all PRP")
for i in PRP:
    print(i)
print("----------------------------------------")
print("all JJ")
for i in JJ:
    print(i)
print("----------------------------------------")
print("all WP")
for i in WP:
    print(i)
print("----------------------------------------")

ROOT=[]
nmodposs=[]
amod=[]
nsubj=[]

for s in sentences:
    enhancedDependencies=s.get("enhancedDependencies")
    for item in enhancedDependencies:
        #print(item.get("word") +"|"+ item.get("pos"))
        if("ROOT" == item.get("dep")):
            ROOT.append(item.get("dependentGloss"))
        elif("nmod:poss" == item.get("dep")):
            nmodposs.append(item.get("dependentGloss"))
        elif("amod" == item.get("dep")):
            amod.append(item.get("dependentGloss"))
        elif("nsubj" == item.get("dep")):
            nsubj.append(item.get("dependentGloss"))
print("all ROOT")
for i in ROOT:
    print(i)
print("----------------------------------------")
print("all nmod:poss")
for i in nmodposs:
    print(i)
print("----------------------------------------")
print("all amod")
for i in amod:
    print(i)
print("----------------------------------------")
print("all nsubj")
for i in nsubj:
    print(i)
print("----------------------------------------")
