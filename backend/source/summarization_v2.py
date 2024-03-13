from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import WebBaseLoader
import gradio as gr
import openai
from openai import OpenAI
from gradio.themes.base import Base
import pandas as pd
import key_param
import requests
from bs4 import BeautifulSoup


def extract_lists_from_summary(summary):
    """获取新闻数据，并将文章内容和新闻内容分隔开"""
    # 将摘要分割为新闻内容和评论两部分
    parts = summary.split("\n\nnews_comment:")
    news_content_raw = parts[0].replace("news_content:", "")
    news_comment_raw = parts[1]

    return news_content_raw, news_comment_raw


def content_comment_div(raw_summary):
    """将文章主体内容和评论内容分隔开"""
    # print(f"raw_summary is {raw_summary}")
    client = OpenAI(api_key=key_param.openai_api_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You will be provided with a news summary, and your task is to distinguish which sentences are mainly about news comments and which are mainly about news content."},
            {"role": "user", "content": f"This is a news summary which is generated based on both news comments and news content:{
                raw_summary}, please return me with two python lists(Named after 'news_content' and 'news_comment')"}
        ],
        max_tokens=2000,
    )
    return response


def summarization_fun(url="https://www.nytimes.com/2017/03/31/opinion/and-now-the-dreaded-trump-curse.html", slider=0.4,
                      article_path=r"C:\Users\王洁\Desktop\Website_project\backend\source\Article_sample.xlsx",
                      comment_path=r"C:\Users\王洁\Desktop\Website_project\backend\source\Comment_sample.xlsx",
                      ):
    """函数返回新闻内容和评论的Summary和两个列表,一个列表[news_content_list]代表新闻内容，一个列表[news_comment_list]代表评论内容"""
    # 提取链接页面中的内容
    loader = WebBaseLoader(url)
    data = loader.load()

    raw_content = data[0].page_content
    # 获取content
    content = raw_content.replace('\n', '')
    # 获取title
    title = data[0].metadata['title']

    raw_article = pd.read_excel(article_path)
    raw_article = pd.DataFrame(raw_article)
    articleID = raw_article['articleID'][0]

    raw_comment = pd.read_excel(comment_path)
    raw_comment = pd.DataFrame(raw_comment)
    # 获取comment
    comment = raw_comment[raw_comment['articleID'] == articleID]

    llm = ChatOpenAI(model_name='gpt-3.5-turbo',
                     openai_api_key=key_param.openai_api_key)

    generic_template = '''
    Write a summary of the following news:
    the title of the news is {title}
    news : `{news}`
    comment: {comment}
    Translate the precise summary to {language}.
    Please generate the summary based on both the news and the comment.
    the expected precentage of comments in summary is {slider}.
    keep the summary within {word_num} words.
    '''
    prompt = PromptTemplate(
        input_variables=['news', 'language', 'word_num'],
        template=generic_template
    )

    complete_prompt = prompt.format(
        title=title, news=content, comment=comment, language='English', word_num=300, slider=slider)

    llm.get_num_tokens(complete_prompt)

    llm_chain = LLMChain(llm=llm, prompt=prompt)
    summary = llm_chain.invoke({'title': title, 'news': content, 'comment': comment,
                               'language': 'English', 'slider': slider, 'word_num': 300})

    raw_div = content_comment_div(summary['text'])

    news_content_list, news_comment_list = extract_lists_from_summary(
        raw_div.choices[0].message.content)

    return summary['text'], news_content_list, news_comment_list

# 测试代码
# print(summarization_fun())

# 区分摘要中内容和评论部分


# js = """
# function createGradioAnimation() {
#     var container = document.createElement('div');
#     container.id = 'gradio-animation';
#     container.style.fontSize = '2em';
#     container.style.fontWeight = 'bold';
#     container.style.textAlign = 'center';
#     container.style.marginBottom = '20px';

#     var text = 'Welcome to Pqy News Summarization!';
#     for (var i = 0; i < text.length; i++) {
#         (function(i){
#             setTimeout(function(){
#                 var letter = document.createElement('span');
#                 letter.style.opacity = '0';
#                 letter.style.transition = 'opacity 0.5s';
#                 letter.innerText = text[i];

#                 container.appendChild(letter);

#                 setTimeout(function() {
#                     letter.style.opacity = '1';
#                 }, 50);
#             }, i * 250);
#         })(i);
#     }

#     var gradioContainer = document.querySelector('.gradio-container');
#     gradioContainer.insertBefore(container, gradioContainer.firstChild);

#     return 'Animation created';
# }
# """

# slider = gr.Slider(minimum=0.2, maximum=0.8, step=0.1, value=0,
#                    label="Choose the precentage of comments")

# # 创建 Gradio 接口
# demo = gr.Interface(fn=summarization_fun,
#                     inputs=[gr.Textbox(
#                         placeholder="URL Here...", label="URL"), slider],
#                     outputs=[gr.Textbox(label="Summarization"),
#                              gr.Textbox(label="news_content_list"),
#                              gr.Textbox(label="news_comment_list")],
#                     title="Summarization based on both the news and the comment.",
#                     description="Enter URL",
#                     js=js
#                     )
# # 启动 Gradio 服务器
# demo.launch()
