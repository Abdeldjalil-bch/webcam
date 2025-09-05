import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title("Real-Time Video Streaming with Streamlit-WebRTC")

webrtc_streamer(key="example")
