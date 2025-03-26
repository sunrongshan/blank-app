import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from gtts import gTTS
import os

# 初始化 GPT 对话模型
# api_key=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
llm = ChatOpenAI(model_name="gpt-4o", temperature=0.7, openai_api_key="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")

memory = ConversationBufferMemory()

# Streamlit 页面标题
st.title("AI 智能多语言学习平台")

# =============== 语法分析 ===============
st.subheader("📖 AI 语法分析")

text_input = st.text_area("输入要分析的文本", placeholder="输入一段文本，AI 将解析语法")
if st.button("分析文本"):
    if text_input:
        prompt = f"请分析以下文本的语法结构，并列出涉及的语法点和解释：{text_input}"
        response = llm.predict(text=prompt)
        st.write("📚 语法解析结果：")
        st.write(response)

# =============== 文字朗读 ===============
st.subheader("🔊 AI 语音朗读")

text_to_speak = st.text_area("输入要朗读的文本", placeholder="输入文本，AI 将朗读")
if st.button("播放语音"):
    if text_to_speak:
        tts = gTTS(text=text_to_speak, lang="en")
        tts.save("output.mp3")
        st.audio("output.mp3", format="audio/mp3")

# =============== AI 角色扮演对话 ===============
st.subheader("🗣 AI 角色扮演对话")

# 创建对话链（带记忆）
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=False  # 设为 True 可查看详细对话日志
)


user_input = st.text_input("你：", placeholder="输入你想和 AI 交谈的内容")
if st.button("发送"):
    if user_input:
        # response = llm.predict(text=user_input, memory=memory)
        response = conversation.predict(input=user_input)
        st.write(f"🤖 AI：{response}")