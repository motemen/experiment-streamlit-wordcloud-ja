import streamlit as st
from wordcloud import WordCloud
from janome.tokenfilter import POSKeepFilter, TokenCountFilter
from janome.analyzer import Analyzer

st.title("日本語 WordCloud")

sample = open("sample.txt").read()
text = st.text_area("Text", sample)

if len(text) > 0:
    analyzer = Analyzer(
        token_filters=[POSKeepFilter(["名詞", "動詞"]), TokenCountFilter()])
    freq = dict(filter(lambda p: len(p[0]) >= 3, analyzer.analyze(text)))
    wordcloud = WordCloud(
        font_path="./fonts/NotoSansJP-Regular.otf", width=1200, height=800).generate_from_frequencies(freq)
    st.image(wordcloud.to_image())

st.markdown("[Open Font License](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL) の下、[Noto Sans Japanese](https://fonts.google.com/noto/specimen/Noto+Sans+JP/about) フォントを利用しています")
