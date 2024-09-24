from youtube_transcript_api import YouTubeTranscriptApi
import requests

# Gemini API Setup
GEMINI_API_URL = "https://api.gemini.ai/v1/summarize"
GEMINI_API_KEY = "AIzaSyBW3mNQtDfFAdx6PqQZr5A9IBQVLmhUdiQ"  # Replace with your Gemini API key

# Function to extract video ID from a YouTube URL
def get_video_id(youtube_url):
    if "v=" in youtube_url:
        return youtube_url.split("v=")[-1].split("&")[0]
    elif "youtu.be/" in youtube_url:
        return youtube_url.split("youtu.be/")[-1]
    else:
        raise ValueError("Invalid YouTube URL")

# Fetch the transcript from the YouTube video
def get_video_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([item['text'] for item in transcript_list])
        return transcript
    except Exception as e:
        return f"Error retrieving transcript: {str(e)}"

# Summarize the Video Transcript using Gemini API
def summarize_video(video_transcript):
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "text": video_transcript,
        "summary_length": "short"  # Options: short, medium, long
    }
    
    response = requests.post(GEMINI_API_URL, json=data, headers=headers)
    
    if response.status_code == 200:
        summary = response.json().get('summary', 'No summary found')
        return summary
    else:
        return f"Error: {response.status_code}, {response.text}"

# Example usage:
youtube_url = ""  # Replace with actual video URL
video_id = get_video_id(youtube_url)
video_transcript = get_video_transcript(video_id)

if "Error" not in video_transcript:
    summary = summarize_video(video_transcript)
    print("Video Summary:")
    print(summary)
else:
    print(video_transcript)
