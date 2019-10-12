# -*- coding: utf-8 -*-
   # @Time    : 2018/8/13 10:47
   # @Author  : wjh
   # @File    : jieba_pygal.py
   
   
import jieba
 
text = open('诛仙.txt', 'r', encoding='utf-8').read()
jieba.add_word('张小凡')   # ?????
jieba.add_word('碧瑶')
jieba.add_word('陆雪琪')
jieba.add_word('林惊羽')
jieba.add_word('道玄')
jieba.add_word('苍松')
jieba.add_word('田不易')
jieba.add_word('苏茹')
jieba.add_word('田灵儿')
jieba.add_word('大黄')
jieba.add_word('小灰')
jieba.add_word('小环')
jieba.add_word('周一仙')
jieba.add_word('兽神')
jieba.add_word('鬼王')
jieba.add_word('普智')
jieba.add_word('法相')
jieba.add_word('万人往')
jieba.add_word('万剑一')
jieba.add_word('野狗')
jieba.add_word('黑心老人')
jieba.add_word('青龙')
jieba.add_word('幽姬')
jieba.add_word('云易岚')
jieba.add_word('宋大仁')
jieba.add_word('鬼厉')
words = jieba.lcut(text)    # ????
 
counts = {}
for word in words:  # ????
    if len(word) == 1:
        continue
    counts[word] = counts.get(word, 0) + 1  # ?????
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)    # key??????,
                                     # ????????????????????
items = dict(items)
x_value = ['张小凡', '碧瑶', '陆雪琪', '林惊羽', '道玄', '苍松',
           '田不易', '苏茹', '田灵儿', '大黄', '小灰', '小环', '周一仙',
           '兽神', '鬼王','普智','法相','万人往','万剑一','野狗','黑心老人','青龙','幽姬','云易岚','宋大仁','鬼厉']
张小凡 = items['张小凡']
碧瑶 = items['碧瑶']
陆雪琪 = items['陆雪琪']
林惊羽 = items['林惊羽']
道玄 = items['道玄']
苍松 =  items['苍松']
田不易 = items['田不易']
苏茹 = items['苏茹']
田灵儿 = items['田灵儿']
大黄 = items['大黄']
小灰 = items['小灰']
小环 = items['小环']
周一仙 = items['周一仙']
兽神 = items['兽神']
鬼王 = items['鬼王']
普智 = items['普智']
法相 = items['法相']
万人往 = items['万人往']
万剑一 = items['万剑一']
野狗 = items['野狗']
黑心老人 = items['黑心老人']
青龙 = items['青龙']
幽姬 = items['幽姬']
云易岚 = items['云易岚']
宋大仁 = items['宋大仁']
鬼厉 =  items['鬼厉']

y_value = [张小凡, 碧瑶, 陆雪琪, 林惊羽, 道玄, 苍松,
           田不易, 苏茹, 田灵儿, 大黄, 小灰, 小环, 周一仙,
           兽神, 鬼王,普智,法相,万人往,万剑一,野狗,黑心老人,青龙,幽姬,云易岚,宋大仁,鬼厉]

import pygal
hist = pygal.Bar()

hist.title = '诛仙人物一览'
hist.x_labels = x_value
hist.title = '人物'
hist.y_labels = y_value
hist.title = '次数'
 
hist.add('S', y_value) # ????? ????
hist.render_to_file('诛仙人物一览表.svg')


import wordcloud
import matplotlib.pyplot as plt
text = []
for word in words:
    if len(word) == 1:
        continue
    text.append(word)
text = ' '.join(text)   # ??????????????
 
font = 'D:\Python\python_learn\jieba\Hiragino Sans GB.ttc'
wd = wordcloud.WordCloud(
                font_path=font,
                width=1000,
                height=600,
                background_color='white'
                ).generate(text)

plt.figure()
plt.axis('off') # ??x?y?
plt.imshow(wd)
plt.show()
wd.to_file('????.png')
