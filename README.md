---
title: Social Reelz
description: Use this software to generate exciting short-form videos 
---

# Initial Setup
1. Create venv (python3 -m venv myenv)
2. Source venv (source myenv/bin/activate)
3. Install requirments (pip install -r requirements.txt)


# Generate Short Form Videos - v0
1. Navigate to SocialReelz/video_editor/v0/data 
2. upload videos (.mov or .mp4) to ./data/videos/pre_processed_clips
3. upload a song (.wav or .mp3) to ./data/audio
4. Navigate to SocialReelz/video_editor/v0 
5. Update config.py to your preferences 
    - sync video transitions with audio beat (default)
    - sync video transitions with audio onset 
6. run "python main.py" in the terminal
7. View your final short video in v0/output/DATETIME

# Generate Short Form Videos - v1 coming soon... 
