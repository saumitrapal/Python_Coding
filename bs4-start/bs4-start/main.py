from bs4 import BeautifulSoup

with open("website.html") as website_file:
    soup = BeautifulSoup(website_file, 'html.parser')
    
all_anchor_tag = soup.find_all('a')
# print(all_anchor_tag)

for anchor_tag in all_anchor_tag:
    # print(anchor_tag.text)
    print(anchor_tag.get('href'))
    


