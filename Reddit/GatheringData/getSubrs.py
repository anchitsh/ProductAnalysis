import requests
from time import sleep
from bs4 import BeautifulSoup as bs

url = "http://redditlist.com/all?page="

listOfSubRs = []

try:
    for i in range(1,41,1):
        print (i)
        page = requests.get(url+str(i))

        soup = bs(page.content, 'html.parser')

        #print (soup.prettify())
        subRraw = soup.find_all(class_='subreddit-url')

        """
        Example of a thing in subRraw:
        <span class="subreddit-url">
        <a class="sfw" href="http://reddit.com/r/engrish" target="_blank">engrish</a>
        </span>"""

        for spanData in subRraw:
            count = 0

            for item in spanData:

                if count == 1:
                    item = str(item)

                    _blankLOC = item.find("_blank")
                    end_aLOC = item.find("</a>")

                    subR = item[_blankLOC+8:end_aLOC]

                    if subR not in listOfSubRs:
                        print (subR, end=", ")
                        listOfSubRs.append(subR)

                count += 1
        print ("____")
        print (i, "complete")
        sleep(5)
except:
    print ("\n\n\nIncomplete\n\n\n")
    pass

print (listOfSubRs)
print (len(listOfSubRs))

fileO = open("SubRs", 'w')
fileO.write(str(listOfSubRs))
fileO.close()

print ("i's VALUE: ", i)
