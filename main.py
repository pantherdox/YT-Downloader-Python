import os
import subprocess

def download_youtube_video(video_url, save_path="downloads"):
    try:
        # Ensure the directory exists
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # yt-dlp command to download and merge video/audio
        command = [
            "yt-dlp",
            video_url,
            "-f", "bestvideo[height=1080]+bestaudio/best",
            "--merge-output-format", "mp4",  # Merge into a single MP4 file
            "-o", os.path.join(save_path, "%(title)s.%(ext)s")
        ]

        # Run the yt-dlp command
        print("Downloading and merging video/audio...")
        subprocess.run(command, check=True)
        print(f"Download and merge completed. File saved to {save_path}.")      

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Input YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Call the function
download_youtube_video(video_url)
