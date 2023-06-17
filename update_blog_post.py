import feedparser

blog_url = "https://medium.com/feed/@heeee"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 5

latest_posts = ""

for idx, entrie in enumerate(rss_feed['entries']):
  if idx > MAX_NUM:
     break;
  feed_date = entrie['published_parsed']
  latest_posts += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {entrie['title']}]({entrie['link']})\n"

preREADME = """

</br>

### 🙇🏻‍♀️ Introduce.
프로그래밍이란 적절한 도구를 이용하여 문제를 해결 할 수 있는 능력이라고 생각합니다.
하나의 기능을 만들 수 있는 여러 가지 방법에 대해 고민하고 탐구하는 편입니다.

</br>

### 🎓 Education.
Chemical Engineering at Hongik University.

</br>

### 📫 Contact.
song.heee.1@gmail.com

</br>

✍️ Tech Blog.
https://medium.com/@heeee

</br>

✨ Interest.
Python, Django, Swift, PostgreSQL, Azure, Vim

</br>
"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)
