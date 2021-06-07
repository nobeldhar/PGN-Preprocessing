import pandas as pd
from tensorflow.core.example import example_pb2

articles = []
with open("Bengali-News-Summarization-Dataset/article.txt", "r", encoding="utf-8") as f:
    for line in f:
        articles.append(line)

summaries = []
with open("Bengali-News-Summarization-Dataset/summary.txt", "r", encoding="utf-8") as f:
    for line in f:
        summaries.append(line)

'''temp = list(zip(articles, summaries))
for article, summary in zip(articles, summaries):
    story = article + '\n\n' + '@highlight'+'\n'+summary'''


for i, (article, summary) in enumerate(zip(articles, summaries)):
    story = article + '\n\n' + '@highlight'+'\n'+summary
    with open(f"stories/story{i}.story", "w", encoding="utf-8") as f:
        f.write(story)






