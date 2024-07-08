import bs4 as bs
import requests

response = requests.get('https://news.ycombinator.com/news')

yc_webpage = response.text

soup = bs.BeautifulSoup(yc_webpage, 'html.parser')
articles = soup.find_all(name='span', class_='titleline')

article_texts = []
article_links = []
for i in range(len(articles)):
    a_tag = articles[i].find('a')
    article_text = a_tag.get_text()
    article_link = a_tag.get('href')
    article_texts.append(article_text)
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]
giusha = max(article_upvotes)
highest_index = article_upvotes.index(giusha)
print(article_texts[highest_index], article_links[highest_index])
