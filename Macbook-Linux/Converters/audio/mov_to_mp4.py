#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ranger (Dec 2024) 😎
# Version 2.0.0

# pip install moviepy 

# Import necessary libraries
# --- Imports ---
from moviepy.editor import VideoFileClip

def convert_mov_to_mp4(input_file_path, output_file_path):
    # Load your .mov video file
    video_clip = VideoFileClip(input_file_path)
    
    # Write the video clip to the new .mp4 file format
    # The parameters ensure maximum quality by avoiding re-encoding
    video_clip.write_videofile(output_file_path, codec='libx264', audio_codec='aac', bitrate='high')

    # Close the video clip to release the resources
    video_clip.close()

# Example usage:
convert_mov_to_mp4("input_video.mov", "output_video.mp4")

