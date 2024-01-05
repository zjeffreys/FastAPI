class Config:
    def __init__(self):
        self.pre_processed_videos = './data/videos/pre_processed_clips/'
        self.post_processed_clips = './data/videos/post_processed_clips/'
        self.audio_directory = './data/audio/'
        self.output_directory = './output/'
        self.clips_duration = 5
        self.testingMode = True
        self.codec="libx264"
        self.audio_codec="aac"
        self.fps=30
        self.threads = 8   
        self.audio_start_time = 0
        self.final_video_duration = 12
        self.output_path = 'output_video.mp4'
        self.video_editing_algo = "beat"
        self.output_video_name = "./output/output_video.mp4"
        self.minimum_clip_duration = 0.75 # seconds