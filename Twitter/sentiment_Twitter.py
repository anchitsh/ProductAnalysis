from textblob import TextBlob
from tweeterdict1 import tweetList
from tweeterdict1 import tweetListime
import numpy as np
import matplotlib.pyplot as plt


sum=0
counter = 1
List = []
List2 = []
TimeList = []
countergood=0
counterbad=0
Listpie=[]
a=0
c=0
d=0
e=0
f=0
g=0
h=0
k=0

for j in tweetListime :
    TimeList.append(j)

for i in tweetList :

  compute = TextBlob(str(i))
  if "good" in compute.words:
      a = a+1
  if "well" in compute.words:
      c = c+1
  if "nice" in compute.words:
      d = d+1
  if "great" in compute.words:
      e = e+1
  if "shit" in compute.words:
      f = f+1
  if "poor" in compute.words:
      g = g+1
  if "bad" in compute.words:
      h = h+1
  if "sad" in compute.words:
      k = k+1
  b = compute.sentiment.polarity

  List.append(b)
  List2.append(counter)


  sum = sum + b
  counter+=1
  
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)

#print("Positive Word Count : ", countergood)
#print("Negative Word Count : ", counterbad)


plt.ylim(-1,1)
plt.plot (List2,List)
plt.show()

plt.ylim(-1,1)
plt.plot(TimeList,List)
plt.show()

print ("The polarity is :", sum/counter)

if sum/counter>0 :
    print ("Positive Review")
else :
    print ("Negative Review")


print(a)
print(c)


Listpie.append(a)
Listpie.append(c)
Listpie.append(d)
Listpie.append(e)
Listpie.append(f)
Listpie.append(g)
Listpie.append(h)
Listpie.append(k)





labels = ['Good', 'well','nice','great','shit','poor','bad','sad']

plt.pie(Listpie)
plt.legend(labels)
plt.show()





