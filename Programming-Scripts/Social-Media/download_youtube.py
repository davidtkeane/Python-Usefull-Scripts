import pytube
import pycurl

# Specify the YouTube video URL
url = "https://www.youtube.com/watch?v=kzQ2eS7EHyw&list=PPSV"

# Create a pytube YouTube object
yt = pytube.YouTube(url)

# Get the video stream
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# Set up curl options
c = pycurl.Curl()
c.setopt(c.URL, stream.url)
c.setopt(c.WRITEDATA, open("video.mp4", "wb"))

# Download the video using curl
c.perform()
c.close()

print("Video downloaded successfully!")