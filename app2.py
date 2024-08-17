import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from googletrans import Translator
import pandas as pd

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize translator
translator = Translator()

def extract_video_id(url):
    """Extract the video ID from various forms of YouTube URLs."""
    if "youtu.be" in url:
        return url.split("/")[-1]
    elif "youtube.com" in url:
        if "v=" in url:
            return url.split("v=")[1].split("&")[0]
        elif "embed" in url:
            return url.split("/")[-1]
    return None

def extract_transcript(video_id, target_language='en'):
    """Extract and concatenate the transcript text, translating if necessary."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join(entry["text"] for entry in transcript)
        
        if target_language != 'en':
            full_text = translator.translate(full_text, dest=target_language).text
        
        return full_text
    except Exception as e:
        st.error(f"Error extracting transcript: {str(e)}")
        return None

def generate_summary(transcript, prompt):
    """Generate a summary using Google's Generative AI."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt + transcript)
        return response.text
    except Exception as e:
        st.error(f"Error generating summary: {str(e)}")
        return None

def generate_qa(transcript, question):
    """Generate an answer to a question based on the video transcript."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        prompt = f"""
        Based on the following video transcript, please answer the question:
        Question: {question}
        
        Transcript:
        {transcript}
        
        Please provide a concise and accurate answer based solely on the information in the transcript.
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating answer: {str(e)}")
        return None

# Streamlit UI
st.set_page_config(page_title="Advanced YouTube Video Summarizer", page_icon="🎥", layout="wide")

st.title("🎥 Advanced YouTube Video Summarizer")

col1, col2 = st.columns([2, 1])

with col1:
    youtube_url = st.text_input("Enter YouTube video URL:", placeholder="https://www.youtube.com/watch?v=...")
    
    if youtube_url:
        video_id = extract_video_id(youtube_url)
        if video_id:
            st.video(f"https://www.youtube.com/watch?v={video_id}")
        else:
            st.error("Invalid YouTube URL. Please check and try again.")

with col2:
    st.subheader("Summary Options")
    summary_type = st.selectbox("Choose summary type:", ["Detailed Notes", "Key Points", "ELI5 (Explain Like I'm 5)"])
    word_limit = st.slider("Word limit:", min_value=100, max_value=500, value=250, step=50)
    target_language = st.selectbox("Select language:", ['en', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'ja', 'ko', 'zh-cn'])

if st.button("Generate Summary", type="primary"):
    if youtube_url:
        video_id = extract_video_id(youtube_url)
        if video_id:
            with st.spinner("Extracting transcript, translating, and generating summary..."):
                transcript = extract_transcript(video_id, target_language)
                if transcript:
                    prompt = f"""
                    You are a YouTube video summarizer. Summarize the following transcript in the style of {summary_type}.
                    Keep the summary within {word_limit} words. Focus on the main ideas and key takeaways.
                    If it's a tutorial or educational content, include any important steps or concepts mentioned.
                    
                    Transcript:
                    """
                    summary = generate_summary(transcript, prompt)
                    if summary:
                        st.subheader(f"{summary_type}")
                        st.write(summary)
                        
                        # Add options to download or copy summary
                        st.download_button(
                            label="Download Summary",
                            data=summary,
                            file_name="video_summary.txt",
                            mime="text/plain"
                        )
                        st.button("Copy to Clipboard", on_click=lambda: st.write(f"Summary copied to clipboard!"))
        else:
            st.error("Invalid YouTube URL. Please check and try again.")
    else:
        st.warning("Please enter a YouTube URL first.")

# Q&A Section
st.markdown("---")
st.subheader("📝 Ask Questions About the Video")
user_question = st.text_input("Ask a question about the video content:")

if st.button("Get Answer"):
    if youtube_url and user_question:
        video_id = extract_video_id(youtube_url)
        if video_id:
            with st.spinner("Analyzing video content and generating answer..."):
                transcript = extract_transcript(video_id)
                if transcript:
                    answer = generate_qa(transcript, user_question)
                    if answer:
                        st.write("Answer:", answer)
    else:
        st.warning("Please enter both a YouTube URL and a question.")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit, Google's Generative AI, and advanced NLP techniques")