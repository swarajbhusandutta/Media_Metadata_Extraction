"""
Description:
    Extract metadata from video file as part of Cyber Forensic Analysis

Author:
    Swaraj Bhusan Dutta

Created:
    26 May, 2024
"""

import json
from pathlib import Path
from tinytag import TinyTag


class DynamicVideoMetaExtraction:

    def __init__(self):
        self.config = json.loads(Path('config.json').read_text())

    def extract(self):
        video_metadata = self.__get_dynamic_video_metadata(self.config['video'].get('file_path', ''))
        print(video_metadata)

    def is_human_readable(self, s):
        return isinstance(s, str) and all(32 <= ord(c) <= 126 for c in s)

    def sanitize_metadata_value(self, value):
        if not isinstance(value, str):
            value = str(value)

        value = value.strip()

        # Make sure the value contains only printable ASCII characters
        sanitized_value = ''.join(c for c in value if 32 <= ord(c) <= 126)

        # Check if the sanitized value is different from the original value
        # This may indicate that unwanted characters were removed
        if sanitized_value != value:
            raise ValueError("Unwanted characters detected in metadata value")

        return sanitized_value

    def __get_dynamic_video_metadata(self, file_path):
        try:
            tag = TinyTag.get(file_path)
            metadata = {}
            for attr in dir(tag):
                if not attr.startswith("__") and attr != "images":
                    value = getattr(tag, attr)
                    if value:
                        sanitized_value = self.sanitize_metadata_value(value)
                        metadata[attr] = sanitized_value
            return metadata
        except Exception as e:
            raise RuntimeError(f"Failed to extract metadata for {file_path}: {e}")