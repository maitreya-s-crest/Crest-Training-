# Owner: Maitreya Sapariya
# Project: Crest Training

import gradio as gr
import requests
from chatbot import Chatbot

chatbot = Chatbot()

gr.ChatInterface(chatbot.chat, type="messages").launch()
