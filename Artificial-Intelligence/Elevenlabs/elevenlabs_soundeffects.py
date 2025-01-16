
import os
from elevenlabs.client import ElevenLabs

from dotenv import load_dotenv

load_dotenv()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))


def generate_sound_effect(text: str, output_path: str):
    print("Generating sound effects...")

    result = elevenlabs.text_to_sound_effects.convert(
        text=text,
        duration_seconds=5,  # Optional, if not provided will automatically determine the correct length
        prompt_influence=0.3,  # Optional, if not provided will use the default value of 0.3
    )

    with open(output_path, "wb") as f:
        for chunk in result:
            f.write(chunk)

    print(f"Audio saved to {output_path}")


if __name__ == "__main__":
    generate_sound_effect("Typing on an old type writer ", "type_writer.mp3")

