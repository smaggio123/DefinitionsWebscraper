import requests
import bs4

#open file where definitions are written
file = open("definitions.txt","w")

#opens file with vocab list
with open("vocabList.txt") as f:
    #get the entire text
    lines=f.readlines()
    #get one line at a time
    for line in lines:
        #in the definition file, writes what the word is
        file.writelines("Word is: "+line +"\n")
        #url of dictionary.com search for vocab word
        url='https://www.dictionary.com/browse/'+line
        #get content of url
        request_result = requests.get(url)
        #parse url
        soup = bs4.BeautifulSoup(request_result.text, "html.parser")
        #get all of the span tags
        heading_object = soup.find_all('span',class_="one-click-content css-nnyc96 e1q3nk1v1")
        #for all of the span tags
        for info in heading_object:
            #in the definitions file, write the content of the span tag
            file.writelines(info.getText())
            #new line in definitions file
            file.writelines("\n")
        #new line in definitions file
        file.writelines("\n")
    #close vocab list file
    f.close()
#close definition file
file.close()