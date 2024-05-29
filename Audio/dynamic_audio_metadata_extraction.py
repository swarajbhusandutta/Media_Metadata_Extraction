"""
Description:
    Extract metadata from audio file as part of Cyber Forensic Analysis

Author:
    Swaraj Bhusan Dutta

Created:
    26 May, 2024
"""

import json
import html
from mutagen import File
from pathlib import Path


class DynamicAudioMetaExtraction:

    def __init__(self):
        self.config = json.loads(Path('config.json').read_text())

    def extract(self):
        audio_metadata = self.__get_dynamic_audio_metadata(self.config['audio'].get('file_path', ''))
        print(audio_metadata)

    def is_human_readable(self, s):
        return isinstance(s, str) and all(32 <= ord(c) <= 126 for c in s)

    def sanitize_metadata_value(self, value):
        if not isinstance(value, str):
            value = str(value)
        # Escape potentially harmful characters
        return html.escape(value)

    def __get_dynamic_audio_metadata(self, file_path):
        audio = File(file_path)
        metadata = {}

        # Extract all available tags and filter unreadable strings
        if audio.tags:
            for tag in audio.tags.keys():
                value = audio.tags[tag]
                if isinstance(value, str) and self.is_human_readable(value):
                    sanitized_value = self.sanitize_metadata_value(value)
                    metadata[tag] = sanitized_value
                elif isinstance(value, list):
                    readable_values = [self.sanitize_metadata_value(v) for v in value if self.is_human_readable(v)]
                    if readable_values:
                        metadata[tag] = readable_values

        # Extract technical info dynamically
        if audio.info:
            for attribute in dir(audio.info):
                if not attribute.startswith('_') and not callable(getattr(audio.info, attribute)):
                    value = getattr(audio.info, attribute)
                    if not callable(value):
                        sanitized_value = self.sanitize_metadata_value(value)
                        metadata[attribute] = sanitized_value

        return metadata