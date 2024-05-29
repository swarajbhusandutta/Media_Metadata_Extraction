import argparse

from Audio.dynamic_audio_metadata_extraction import DynamicAudioMetaExtraction
from Video.dynamic_video_metadata_extraction import DynamicVideoMetaExtraction

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Media file (Audio & Video) metadata extractor.'
    )
    parser.add_argument(
        '-audio', '--audio', action='store_true', help='Extract from Audio file'
    )
    parser.add_argument(
        '-video', '--video', action='store_true', help='Extract from Video file'
    )

    args = parser.parse_args()

    a_f = args.audio
    v_f = args.video

    if a_f:
        audio_meta = DynamicAudioMetaExtraction()
        audio_meta.extract()

    if v_f:
        video_meta = DynamicVideoMetaExtraction()
        video_meta.extract()
