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





# import os
# import subprocess

# def download_youtube_video(video_url, save_path="downloads"):
#     try:
#         # Ensure the directory exists
#         if not os.path.exists(save_path):
#             os.makedirs(save_path)

#         # Command for yt-dlp to download 1080p video with audio
#         command = [
#             "yt-dlp",
#             video_url,
#             "-f", "bestvideo[height=1080]+bestaudio/best",
#             "-o", os.path.join(save_path, "%(title)s.%(ext)s")
#         ]

#         # Run the command
#         subprocess.run(command, check=True)
#         print(f"Download completed in {save_path}!")

#     except subprocess.CalledProcessError as e:
#         print(f"An error occurred: {e}")

# # Input YouTube video URL
# video_url = input("Enter the YouTube video URL: ")

# # Call the function
# download_youtube_video(video_url)





# from pytube import YouTube
# import os

# def download_youtube_video(video_url, save_path="/output"):
#     try:
#         # Create YouTube object
#         yt = YouTube(video_url)

#         # Get the highest resolution stream
#         video_stream = yt.streams.get_highest_resolution()

#         # Print video details
#         print(f"Downloading: {yt.title}")
#         print(f"From: {video_url}")

#         # Ensure the directory exists
#         if not os.path.exists(save_path):
#             os.makedirs(save_path)

#         # Download video
#         video_stream.download(output_path=save_path)
#         print(f"Downloaded successfully to {save_path}")

#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Input video URL
# video_url = input("Enter the YouTube video URL: ")

# # Download the video
# download_youtube_video(video_url)



# from pytube import YouTube

# def Download(link):
#     youtubeObject = YouTube(link)
#     youtubeObject = youtubeObject.streams.get_highest_resolution()
#     try:
#         youtubeObject.download()
#     except:
#         print("An error has occurred")
#     print("Download is completed successfully")


# link = input("Enter the YouTube video URL: ")
# Download(link)

# from pytube import YouTube
# YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
#  yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
#  yt.streams
#   ... .filter(progressive=True, file_extension='mp4')
#   ... .order_by('resolution')
#   ... .desc()
#   ... .first()
#   ... .download()