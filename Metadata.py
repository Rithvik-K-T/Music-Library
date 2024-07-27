import os
import mutagen
from mutagen.id3 import ID3

def show_metadata(input_path):
    """
    Extracts and prints metadata for music files in the specified directory.

    Args:
        input_path (str): Path to the music directory.
    """

    for root, _, files in os.walk(input_path):
        for file in files:
            if file.endswith('.mp3'):
                file_path = os.path.join(root, file)
                audio = ID3(file_path)

                try:
                    title = audio['TIT2'].text[0]
                    artist = audio['TPE1'].text[0]
                    album = audio['TALB'].text[0]
                except KeyError:
                    print(f"Error parsing metadata for {file_path}")
                    continue

                
                print(f"File: {file_path}")
                print(f"Song: {title}")
                print(f"Artist: {artist}")
                print(f"Album: {album}")
               

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Show metadata for music files")
    parser.add_argument("--input", required=True, help="Path to the music folder")
    args = parser.parse_args()

    show_metadata(args.input)
