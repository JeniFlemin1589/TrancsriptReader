class TranscriptProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_transcript(self):
        """
        Loads the transcript from the provided file path.
        Returns the transcript content as a string.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                transcript = file.read()
            return transcript
        except FileNotFoundError:
            raise FileNotFoundError(f"Transcript file not found at {self.file_path}")
        except Exception as e:
            raise Exception(f"Error loading transcript: {e}")
