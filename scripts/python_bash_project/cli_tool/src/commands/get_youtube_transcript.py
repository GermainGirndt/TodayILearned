# cli_tool/commands/youtube_transcript_command.py
import argparse
import re
from argparse import ArgumentParser
from urllib.parse import parse_qs, urlparse

import requests
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled

from .base_command import BaseCommand


class YouTubeTranscriptCommand(BaseCommand):
    name = "youtube-transcript"
    name_aliases = ["yt-transcript", "get-youtube-transcript"]
    help = "Fetch a YouTube video's title + transcript and save to a text file"

    @staticmethod
    def add_arguments(parser: ArgumentParser):
        parser.add_argument("url", help="URL of the YouTube video")
        parser.add_argument(
            "-o",
            "--output",
            default="output.txt",
            help="Output filename (default: output.txt)",
        )
        parser.add_argument(
            "--no-timeranges",
            action="store_true",
            help="Do not prepend time ranges to transcript lines",
        )
        parser.add_argument(
            "--languages",
            nargs="+",
            default=["en", "de", "pt"],
            help="Preferred transcript languages in priority order (default: en de pt)",
        )

    def run(self, args: argparse.Namespace):
        filename = args.output
        url = args.url
        preserve_timeranges = not args.no_timeranges

        video_title = self.get_title_oembed(url)
        transcript_content = self.get_transcript(
            url, preserve_timeranges=preserve_timeranges, languages=args.languages
        )

        if transcript_content:
            complete_content = f"Title: {video_title}\n\n{transcript_content}"
            self.save_to_txt(complete_content, filename)
            print(f"Transcript saved to {filename}")
        else:
            print("Failed to fetch transcript.")

    # -------------------------
    # Title fetching (NOT via youtube_transcript_api)
    # -------------------------

    @staticmethod
    def get_title_oembed(youtube_url: str) -> str:
        """
        Fetch the video title via YouTube's oEmbed endpoint (no API key).
        """
        try:
            resp = requests.get(
                "https://www.youtube.com/oembed",
                params={"url": youtube_url, "format": "json"},
                timeout=15,
            )
            resp.raise_for_status()
            data = resp.json()
            return data.get("title") or "Unknown title"
        except Exception as e:
            print(f"Failed to fetch title via oEmbed: {e}")
            return "Unknown title"

    # -------------------------
    # Transcript fetching (new youtube_transcript_api interface)
    # -------------------------

    @staticmethod
    def extract_video_id(youtube_url: str) -> str | None:
        """
        Supports:
          - https://www.youtube.com/watch?v=VIDEO_ID
          - https://youtu.be/VIDEO_ID
          - https://www.youtube.com/shorts/VIDEO_ID
        """
        try:
            parsed = urlparse(youtube_url)

            # youtu.be/VIDEO_ID
            if parsed.netloc in {"youtu.be"}:
                vid = parsed.path.strip("/").split("/")[0]
                return vid or None

            # youtube.com/watch?v=VIDEO_ID
            if parsed.path == "/watch":
                qs = parse_qs(parsed.query)
                vid = (qs.get("v") or [None])[0]
                return vid

            # youtube.com/shorts/VIDEO_ID
            m = re.match(r"^/shorts/([\w-]+)", parsed.path)
            if m:
                return m.group(1)

            # fallback: last resort regex for v=...
            m = re.search(r"(?:\?|&)v=([\w-]+)", youtube_url)
            if m:
                return m.group(1)

            return None
        except Exception:
            return None

    @staticmethod
    def get_transcript_yt_api(
        youtube_url: str,
        preserve_timeranges: bool = True,
        languages: list[str] | None = None,
    ) -> str | None:
        print("Trying YoutubeTranscriptApi...")

        video_id = YouTubeTranscriptCommand.extract_video_id(youtube_url)
        if not video_id:
            print("Could not extract video_id from URL.")
            return None

        languages = languages or ["en", "de", "pt"]

        try:
            ytt_api = YouTubeTranscriptApi()
            transcript_list = ytt_api.list(video_id)
            transcript = transcript_list.find_transcript(languages)

            fetched = transcript.fetch()  # returns FetchedTranscript (v1.x)

            if preserve_timeranges:
                out = []
                for snippet in fetched:
                    start_min = snippet.start / 60.0
                    end_min = (snippet.start + snippet.duration) / 60.0
                    out.append(
                        f"{start_min:.2f} - {end_min:.2f}: {snippet.text}")
                return "\n".join(out) + "\n"
            else:
                return "\n".join(snippet.text for snippet in fetched)

        except (TranscriptsDisabled, NoTranscriptFound) as e:
            print(f"Transcript retrieval error: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    @classmethod
    def get_transcript(
        cls,
        youtube_url: str,
        preserve_timeranges: bool = True,
        languages: list[str] | None = None,
    ) -> str | None:
        return cls.get_transcript_yt_api(
            youtube_url, preserve_timeranges=preserve_timeranges, languages=languages
        )

    @staticmethod
    def save_to_txt(content: str, filename: str = "transcript.txt") -> None:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
