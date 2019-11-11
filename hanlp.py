# -*- coding:utf-8 -*-
from jpype import *
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re


def main():
    startJVM(getDefaultJVMPath(), "-Djava.class.path=D:\Doc\python\hanlp\hanlp-1.7.5.jar;D:\Doc\python\hanlp\hanlp.py",
             "-Dfile.encoding=UTF-8",
             "-Xms1g",
             "-Xmx1g")

    NLP('龙族[1-3部全].txt')
    NRCount('token_龙族[1-3部全].txt')

def NLP(name):
    StandardTokenizer = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')

    f = open(name, encoding="utf-8")
    lines = f.read()
    with open('./token_' + name, 'wt', encoding='utf8') as f:
        print(StandardTokenizer.segment(lines), file=f)


def NRCount(name):
    f = open( name, encoding="utf-8")
    lines = f.read()
    wordList = lines.split(',')
    str=''
    for word in wordList:
        if ('/nr' or '/nrj' or 'nrf' )in word:
            word = re.sub(r'/.+', "", word)
            str+=word+' '
    print(str)

    wc = WordCloud(font_path='C:\Windows\Fonts\msyh.ttc',  # 设置字体
                  background_color="white",  # 背景颜色
                  max_words=2000,  # 词云显示的最大词数
                  max_font_size=100,  # 字体最大值
                  random_state=42,
                  width=1000, height=860, margin=2,  # 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
                  )
    wc.generate(str)
    # wc.generate_from_frequencies(txt_freq)
    # txt_freq例子为[('词a', 100),('词b', 90),('词c', 80)]
    # 从背景图片生成颜色值

    plt.figure()
    # 以下代码显示图片
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    # 绘制词云


if __name__ == '__main__':
    main()
