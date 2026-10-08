# -*- coding: utf-8 -*-
"""

"""

import jieba
import imageio
from wordcloud import WordCloud

"""北京二手房数据词云"""
#基础配置数据
def main():
    filename = "ershoufang-clean-utf8-v1.1.csv"
    backpicture = "resources\\house2.jpg"
    savepicture = "picture\\北京二手房数据词云2.png"
    fontpath = "resources\\simhei.ttf"
    stopwords = ["null","暂无","数据","上传","照片","房本"]
    comment_text = open(filename,encoding="utf-8").read()
    color_mask = imageio.imread(backpicture)
    ershoufang_words = jieba.cut(comment_text)
    ershoufang_words = [word for word in ershoufang_words if word not in stopwords]
    cut_text = " ".join(ershoufang_words)
    cloud = WordCloud(
        font_path=fontpath,
        background_color='white',
        mask=color_mask,
        max_words=2000,
        max_font_size=60
       )
    word_cloud = cloud.generate(cut_text)
    #保存图片
    word_cloud.to_file(savepicture)

if __name__ == "__main__":
    main()