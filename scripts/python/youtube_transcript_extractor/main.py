import re
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound


def get_transcript_pytube(youtube_url):
    print("Trying Pytube...")

    # Get YouTube video
    yt = YouTube(youtube_url)

    # Try to get English caption using pytube
    try:
        return yt.captions['en'].generate_srt_captions()
    except KeyError:
        return None


def get_transcript_yt_api(youtube_url):
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
        print(transcript_data)

        transcript = "\n".join([entry['text'] for entry in transcript_data])

        # transcript = "\n".join(
        #    [f"{entry['start']} - {entry['start'] + entry['duration']}: {entry['text']}" for entry in transcript_data])
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
    # url = "https://www.youtube.com/watch?v=HVLKaCVJUwI"
    transcript_content = get_transcript(url)
    if transcript_content:
        save_to_txt(transcript_content)
        print(f"Transcript saved to {filename}")
    else:
        print("Failed to fetch transcript.")


if __name__ == "__main__":
    main()


# https://www.youtube.com/watch?v=HVLKaCVJUwI
