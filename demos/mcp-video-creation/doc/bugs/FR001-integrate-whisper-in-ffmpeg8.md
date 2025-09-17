## Transcribe VIDEO into TEXT

This doc https://www.phoronix.com/news/FFmpeg-Lands-Whisper  explains how ffmpeg 8 has whisper model integrated.

This means that it can OFFLINE (no access to the internet) transcribe a video into audio, so I could do something like

```bash
$ transcribe-video.sh video.avi
Written  video_transcription.txt
```

Let's implement this feature!

## Check possibility

Now we need to first check this:

1. ffmpeg is v8 or more
2. ffmpeg was built with --enable-whisper. Not sure how to check.
