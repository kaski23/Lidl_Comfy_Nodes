import re
from datetime import datetime

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
    CATEGORY = "LIDL/stringtools"

    def split_and_select(self, text: str, delimiter: str, index: int):
        if not delimiter:
            return ("NONE",)  # if no delimiter is specified, kill the whole thing

        parts = text.split(delimiter)
        if 0 <= index < len(parts):
            return (parts[index],)
        else:
            return ("NONE",)


class GenerateID:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "film": (["Mood", "Fin", "Gelati", "Saskia",]),
                "shot_no": ("INT", {"default": 0, "min": 0, "max": 10000, "step": 1}),
                "pipeline_step": (["firstFrame", "notEnhanced", "enhanced", "cgDepth", "cgNormal", "lastFrame", "f"]),
                "frame_no": ("INT", {"default": 0, "min": 0, "max": 10000, "step": 1}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("generated ID",)
    FUNCTION = "generate"
    CATEGORY = "LIDL/stringtools"
    
    def generate(self, film: str, shot_no: int, pipeline_step: str, frame_no: int):
        if pipeline_step == "f":
            pipeline_step = f"f{frame_no}"
        date_str = self._get_date_string()
        shot_no_padded =  f"{shot_no:03d}"
        
        out = f"{date_str}_{film}_{shot_no_padded}_{pipeline_step}_v"
        
        return (out,)
    
    @staticmethod
    def _get_date_string():
        return datetime.now().strftime("%Y%m%d")
        



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
    CATEGORY = "LIDL/stringtools"

    REGEX = re.compile(r"(_\w+_\d{3}_\w+)")

    def extract(self, text: str):
        date_str = self._get_date_string()
        match = self.REGEX.search(text)

        suffix = match.group(1) if match else "NO_VALID_ID_FOUND"
        return (date_str + suffix,)

    @staticmethod
    def _get_date_string():
        return datetime.now().strftime("%Y%m%d")