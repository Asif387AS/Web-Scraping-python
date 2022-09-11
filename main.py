# if you want to scrape a website:
#     1- use API
#     2-HTML Web Scraping using some tool like bs4

# Step 0: install the requirments 
# pip install requests
# pip install bs4
# pip install html5lib 

from bs4 import element
from bs4.element import Comment, NavigableString, Tag
import requests
from bs4 import BeautifulSoup
url="https://www.codewithharry.com"
url2="https://www.thapatechnical.com/"



# Step 1: Get the HTML 
r=requests.get(url2)
htmlContent=r.content
# print(htmlContent)
# Step 2: Parse the HTML 
soup=BeautifulSoup(htmlContent,"html.parser")
# print(soup.prettify)
# Step 3: HTML tree Traversal 

# commonly used types of objects

 # 1-Tag
 # 2-NavigableString
# -BeautifulSoup
# 4-Comments

markup="<p><!-- this is the comment --> </p>"
soup2=BeautifulSoup(markup)
# print(soup2.p)
# print(soup2.p.string)
# print(type(soup2.p.string))
# exit()

title=soup.title
print(type(soup)) # 3-BeautifulSoup
print(type(title.string)) # 2-NavigableString
print(type(title)) # 1-Tag

# Get the title of htnl page 
title=soup.title
# print(title)

# Get all the paragraphs tags from html page 
para=soup.find_all("p")
# print(para)

# Get all the anchors tag from html page 
a=soup.find_all("a")
# print(a)

# Get the first element in the html page 
# print(soup.find('p'))

# Get the class of first p element in the html page 
# print(soup.find('p')['class'])

# Get all the elements with class lead 
# print(soup.find_all('p',class_='lead'))

# Get the text of from the tag/soup 
# print(soup.find('p').get_text())

# Get the text of whole html page 
# print(soup.get_text())

# Get all the anchors tag from html page 
anchors=soup.find_all("a")
print(a)
all_links=set()
for link in anchors:
    if(link.get('href')!='#'):
        linkText="https://www.thapatechnical.com" + link.get('href')
        all_links.add(linkText)
        # print(linkText)


widgetContent=soup.find(id="Bottom-menu")
# contents: A tag's chidren is available as list 
# children: A tag's children is available as generator 
# for elem in widgetContent.children:
#     print(elem)
# for elem in widgetContent.strings:
#     print(elem)
# for elem in widgetContent.stripped_strings:
#     print(elem)
# print(widgetContent.parent.name)
# print(widgetContent.parents)  # the element which have s at the end it is a generator and means multiple element and we loop them 

# for elem in widgetContent.parents:
    # print(elem.name)


# print(widgetContent.next_sibling)
# print(widgetContent.previous_sibling)
# print(widgetContent.next_elements)

elem=soup.select('.Bottom-menu')
elem=soup.select('#Bottom-menu')  #print the element having this id
print(elem)