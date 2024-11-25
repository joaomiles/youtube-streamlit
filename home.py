import streamlit as st
import yt_dlp

def get_audio_link(video_url):
    """
    Fetches the audio-only stream URL for a YouTube video using yt-dlp.

    :param video_url: The YouTube video URL.
    :return: The audio-only stream URL.
    """
    ydl_opts = {
        'format': 'bestaudio/best',  # Get the best audio format
        'quiet': True,               # Suppress output
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            return info['url']
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Streamlit app
st.title("YouTube Audio Link Extractor")

# Input field for YouTube URL
video_url = st.text_input("Enter YouTube Video URL:", "")

if st.button("Get Audio Link"):
    if video_url:
        st.write("Fetching audio link...")
        audio_link = get_audio_link(video_url)
        if audio_link:
            st.success("Audio link retrieved successfully!")
            st.write("Audio URL:")
            st.markdown(f"[{audio_link}]({audio_link})")
        else:
            st.error("Failed to retrieve audio link. Please check the URL.")
    else:
        st.error("Please enter a valid YouTube URL.")
