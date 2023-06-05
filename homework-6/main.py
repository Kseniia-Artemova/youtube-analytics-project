from src.video import Video
from pprint import pprint

if __name__ == '__main__':
    broken_video = Video('broken_video_id')
    video = Video('AWX4JnAnjBE')
    assert broken_video.title is None
    assert broken_video.like_count is None
