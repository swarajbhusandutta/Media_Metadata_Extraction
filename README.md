# Media_Metadata_Extraction
Source code for extract metadata from medial file like audio, video file as part of Cyber Forensic Analysis

# How to use

    python3 wrapper.py -audio

    python3 wrapper.py -video

# File path

add the file path under config.json file.

        {
          "audio": {
            "file_path": "<file_path>"
          },
          "video": {
            "file_path": "<file_path>"
          }
        }