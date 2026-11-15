import asyncio
import edge_tts
from moviepy.editor import AudioFileClip, ColorClip, CompositeVideoClip

TEXT = "What if the Earth stopped spinning for one second?"
AUDIO_FILE = "voice.mp3"
OUTPUT_FILE = "output.mp4"

async def generate_audio():
    communicate = edge_tts.Communicate(TEXT, "en-US-ChristopherNeural")
    await communicate.save(AUDIO_FILE)

if __name__ == "__main__":
    asyncio.run(generate_audio())
    audio_clip = AudioFileClip(AUDIO_FILE)
    duration = audio_clip.duration
    video_clip = ColorClip(size=(1080, 1920), color=(30, 30, 30), duration=duration)
    video_clip = video_clip.set_audio(audio_clip)
    video_clip.write_videofile(OUTPUT_FILE, fps=24)
  z
