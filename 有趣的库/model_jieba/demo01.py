# coding = utf-8
# 三国演义的词频统计
# 中文分词库jieba
import jieba

content = "话说天下大势，分久必合，合久必分。"
res = jieba.lcut(content)
print(res)