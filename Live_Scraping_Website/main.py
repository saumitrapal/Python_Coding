import requests
from bs4 import BeautifulSoup

responce = requests.get(url="https://news.ycombinator.com/news")
website_html_content = responce.text

soup = BeautifulSoup(website_html_content, 'html.parser')
articles = soup.find_all(name="span", class_="titleline")
article_upvote = soup.find_all(name="span", class_="score")

article_headline_list = [article.get_text() for article in articles]
article_link_list = [article.find("a").get("href") for article in articles]
article_point_list = [int(point.getText().split(" ")[0]) for point in article_upvote]

article_point = max(article_point_list)
article_index = article_point_list.index(article_point)

article_heading = article_headline_list[article_index]
article_link = article_link_list[article_index]

print(f"Article Headline: {article_heading}")
print(f"Article Link: {article_link}")
print(f"Article Point: {article_point}")





# print(article_headline_list)
# point_list = []

# for point in aricle_point_list:
#     point_list.append(int(point.split(" ")[0]))
    
# print(point_list)
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