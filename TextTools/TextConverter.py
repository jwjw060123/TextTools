import streamlit as st
import re
from bs4 import BeautifulSoup

st.title('Text Converter')
uploaded = st.file_uploader('Upload your file here.', type=['txt','html'])

if uploaded:
    file_type = uploaded.type.lower()
    file_name = uploaded.name.lower()
    if 'txt' in file_type or file_name.endswith('.txt'):
        raw = uploaded.read().decode('utf-8')
    elif 'html' in file_type or file_name.endswith('.html'):
        html_text = uploaded.read().decode('utf-8')
        soup = BeautifulSoup(html_text, 'html.parser')
        for tag in soup.find_all(['video', 'img']):
            tag.replace_with('\n\n')
        raw = soup.get_text(separator='\n')

    lines = raw.splitlines()
    intro = '\n'.join(lines[:20])
    rest = '\n'.join(lines[20:])
    clean_intro = re.sub(r'.*?\s+to\s+([A-Z][a-z]+)\s+(\d{2}),\s+(\d{4})\s+at\s+(\d{1,2}):(\d{2})\s+(AM|PM)\s+',
                         '', intro, flags=re.DOTALL)
    text = clean_intro + '\n' + rest
    text = re.sub(r':(\d{2}) (am|pm)', r':\1 \2\n\n---', text)
    text = re.sub(r'(\n\n[A-Z][a-z]{2}) (\d{2}), (\d{4}) (\d{1,2}):(\d{2}) (am|pm)',
                  r'\n[media]\n\n\1 \2, \3 \4:\5 \6', text)
    text = text.replace('\n','\n\n')
    messages = text.split('---')
    messages.reverse()
    text = '---'.join(messages)
    st.write(text)
