from moviepy.editor import VideoFileClip

def split_video(input_file, output_prefix, segments):
    # Load the video file
    video = VideoFileClip(input_file)
    
    # Split the video into clips based on specified segments
    for i, (start_time, end_time) in enumerate(segments):
        clip = video.subclip(start_time, end_time)
        output_file = f"{output_prefix}_{i+13}.mp4"
        clip.write_videofile(output_file)
        
    # Close the video
    video.close()

# Example usage
input_file = "input_video.mp4"  # Path to the input video file
output_prefix = "output_clip"    # Prefix for output clip names
segments = [(0, 10), (15, 25), (30, 40)]  # List of (start_time, end_time) for each segment in seconds

split_video(input_file, output_prefix, segments)
