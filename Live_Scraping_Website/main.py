import requests
from bs4 import BeautifulSoup

responce = requests.get(url="https://news.ycombinator.com/news")
website_html_content = responce.text

soup = BeautifulSoup(website_html_content, 'html.parser')
articles = soup.find_all(name="span", class_="titleline")
article_upvote = soup.find_all(name="span", class_="score")

# for article in articles:
#     print(article.getText())
    
article_headline_list = [article.get_text() for article in articles]
article_link_list = [article.find("a").get("href") for article in articles]
aricle_point_list = [point.getText() for point in article_upvote]
print(article_headline_list)

# print(article_headline_list)
# print(article_link_list)

# for article in articles:
#     print(article.find("a").get("href"))


# article_text = articles.get_text()
# article_link = articles.find_all_next(name="a", limit=1)
# print(article_upvote)



# for point in article_upvote:
#     print(point.get_text())

# for link in article_link:
#     print(link.get("href"))



# print(soup.find_all(name="a")[11].text)

# print(soup.title)
# print(soup.prettify())

# print(soup.find_all("a"))

# for a in soup.find('td'):
#     print(a)