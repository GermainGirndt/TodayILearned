from youtube_transcript_api import YouTubeTranscriptApi


def get_transcript(video_url):
    # Extract the video ID from the URL
    video_id = video_url.split("watch?v=")[1]

    # Fetch the transcript
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        print("An error occurred while fetching the transcript:", str(e))
        return None

    # Combine all the parts of the transcript
    full_transcript = ""
    for part in transcript:
        full_transcript += part['text'] + ' '

    return full_transcript


# put the actual URL here
video_url = "https://www.youtube.com/watch?v=fJ9rUzIMcZQ"
transcript = get_transcript(video_url)

if transcript is not None:
    # Write the transcript to a text file
    with open("output/transcript.txt", "w") as f:
        f.write(transcript)
    print("Success! Transcript saved to transcript.txt")
else:
    print("Error: No transcript found")
