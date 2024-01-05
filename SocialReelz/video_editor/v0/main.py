# main.py
from video_editor import * 
from config import Config
from utils.video_utils import *
from utils.audio_utils import * 

def main():

    # load config variables
    config = Config()

    # Testing Mode: load from postprocessed clips from directiory. ignores preprocessing if True. 
    clips = []
    if(config.testingMode): 
        clips = load_clips(config.post_processed_clips)
    else:
        clips = generate_clips(config.pre_processed_videos, config.clips_duration)

    print(f"after loading\n {len(clips)}")
    # load audio
    random_audio = get_random_audio_file(config.audio_directory)

    # genreate video 
    if(config.video_editing_algo == "beat"):
        final_video = synchronize_transitions_beat(clips, random_audio, config.audio_start_time, config.final_video_duration, config.minimum_clip_duration)
    elif(config.video_editing_algo == "onset"):
        final_video = synchronize_transitions_onset(clips, random_audio, config.audio_start_time, config.final_video_duration)

    # output to mp4 file
    final_video.write_videofile(config.output_video_name, codec=config.codec, audio_codec=config.audio_codec, fps=config.fps, threads = config.threads)
 
if __name__ == "__main__":
    main()
