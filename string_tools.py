import re

class StringSplitSelect:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": False}),
                "delimiter": ("STRING", {"default": "_"}),
                "index": ("INT", {"default": 0, "min": 0, "max": 1000, "step": 1}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "split_and_select"
    CATEGORY = "string"

    def split_and_select(self, text: str, delimiter: str, index: int):
        if not delimiter:
            return ("NONE",)  # if no delimiter is specified, kill the whole thing

        parts = text.split(delimiter)
        if 0 <= index < len(parts):
            return (parts[index],)
        else:
            return ("NONE",)


class ExtractIDFromString:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("extracted ID",)
    FUNCTION = "extract"
    CATEGORY = "string"
    
    REGEX = r"(\d{8}_\w+_\d{3}_\w+)"

    def extract(self, text: str):
        match = re.search(self.REGEX, text)
        
        if match:
            return (match.group(1),)
        else:
            return ("NO_VALID_ID_FOUND",)
          