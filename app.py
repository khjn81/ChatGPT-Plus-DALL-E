import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]

st.title("ChatGPT Plus DALL-E")

with st.form("form"):
    user_input = st.text_input("Prompt")
    submit = st.form_submit_button("Submit")
    size = st.selectbox("Size",["1024x1024","512x512","256x256"])

if submit and user_input:
    gpt_prompt = [{
        "role":"system",
        "content":"Imagine the deail appearance of the input. Response it shortly in 30 words"
    }]

    gpt_prompt.append({
        "role":"user",
        "content":user_input
    })
    with st.spinner("Watting for ChatGPT..."):
        gpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=gpt_prompt
        )
    
    prompt = gpt_response["choices"][0]["message"]["content"]
    st.write(prompt)

    with st.spinner("Watting for Dalle..."):
        dalle_reponse = openai.Image.create(
            prompt=prompt,
            size=size
        )

    st.image(dalle_reponse["data"][0]["url"])

