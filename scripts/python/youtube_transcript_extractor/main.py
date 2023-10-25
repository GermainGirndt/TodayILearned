import re
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound


def get_title_pytube(youtube_url):
    """Get the title of the video using pytube."""
    yt = YouTube(youtube_url)
    return yt.title


def get_transcript_pytube(youtube_url):
    print("Trying Pytube...")

    # Get YouTube video
    yt = YouTube(youtube_url)

    # Try to get English caption using pytube
    try:
        return yt.captions['en'].generate_srt_captions()
    except KeyError:
        return None


def get_transcript_yt_api(youtube_url, preserve_timeranges=True):
    print("Trying YoutubeTranscriptApi...")

    # Extract video_id using regex
    video_id_match = re.search(r'v=([\w-]+)', youtube_url)
    if not video_id_match:
        return None

    video_id = video_id_match.group(1)

    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        print("Printing transcripts...")
        transcripts = transcript_list.find_transcript(['en', 'de', 'pt'])

        transcript_data = transcripts.fetch()

        if preserve_timeranges:
            transcript = ""
            for entry in transcript_data:

                start_time = entry['start']/60
                end_time = (entry['start'] + entry['duration']) / 60
                text_line = entry['text']

                text_line = f"{start_time:.2f} - {end_time:.2f}: {text_line}\n"
                transcript += text_line

        else:
            transcript = "\n".join([entry['text']
                                   for entry in transcript_data])

        return transcript
    except (TranscriptsDisabled, NoTranscriptFound) as e:
        print(f"Transcript retrieval error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def get_transcript(youtube_url):
    # Try pytube first
    transcript = get_transcript_pytube(youtube_url)
    if transcript:
        return transcript

    # If pytube fails, use youtube_transcript_api
    return get_transcript_yt_api(youtube_url)


def save_to_txt(content, filename="transcript.txt"):
    with open(filename, "w") as f:
        f.write(content)


def main():
    filename = "output.txt"
    url = input("Enter the URL of the YouTube video: ")

    video_title = get_title_pytube(url)
    transcript_content = get_transcript(url)

    # Prepend the title to the transcript
    if transcript_content:
        complete_content = f"Title: {video_title}\n\n{transcript_content}"
        save_to_txt(complete_content, filename)
        print(f"Transcript saved to {filename}")
    else:
        print("Failed to fetch transcript.")


if __name__ == "__main__":
    main()
