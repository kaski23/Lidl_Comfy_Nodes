import re
from datetime import datetime

REGEX_ID =  re.compile(
        r"\d{8}_(Mood|Fin|Gelati|Saskia)_\d{3}_(firstFrame|notEnhanced|enhanced|cgDepth|cgNormal|lastFrame|f\d+)_(v\d+|vN)"
    )

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
                "film": (["Mood", "Fin", "Gelati", "Saskia"],),
                "shot_no": ("INT", {"default": 0, "min": 0, "max": 10000, "step": 1}),
                "pipeline_step": (["firstFrame", "notEnhanced", "enhanced", "cgDepth", "cgNormal", "lastFrame", "f"],),
                "frame_no": ("INT", {"default": 0, "min": 0, "max": 10000, "step": 1}),
                "version": ("INT", {"default": -1, "min": -1, "max": 10000, "step": 1}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("generated ID",)
    FUNCTION = "generate"
    CATEGORY = "LIDL/stringtools"
    
    def generate(self, film: str, shot_no: int, pipeline_step: str, frame_no: int, version: int):
        if pipeline_step == "f":
            if frame_no < 0:
                raise ValueError("LIDL-Nodes: pipeline_step 'f' requires valid frame_no")
            pipeline_step = f"f{frame_no}"
            
        version_string = ""
        if version != -1:
            version_string = f"v{version}"
        else:
            version_string = "vN"
        
        date_str = self._get_date_string()
        shot_no_padded =  f"{shot_no:03d}"
        
        out = f"{date_str}_{film}_{shot_no_padded}_{pipeline_step}_{version_string}"
        
        return (out,)
    
    @staticmethod
    def _get_date_string():
        return datetime.now().strftime("%Y%m%d")
        


class ModifyID:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "idx": ("STRING", {"multiline": False}),
                "update_date": ("BOOLEAN", {"default": True}),
                "film": (["KEEP", "Mood", "Fin", "Gelati", "Saskia"],),
                "shot_no": ("INT", {"default": -1, "min": -1, "max": 10000, "step": 1}),
                "pipeline_step": (["KEEP", "firstFrame", "notEnhanced", "enhanced", "cgDepth", "cgNormal", "lastFrame", "f"],),
                "frame_no": ("INT", {"default": -1, "min": -1, "max": 10000, "step": 1}),
                "version": ("INT", {"default": -1, "min": -1, "max": 10000, "step": 1}),
            },
        }
        
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("generated ID",)
    FUNCTION = "modify"
    CATEGORY = "LIDL/stringtools"
    
    def modify(self, idx: str, update_date: bool, film: str, shot_no: int, pipeline_step: str, frame_no: int, version: int):
        
        # 1. Validate by Regex -> Gatekeep
        if not REGEX_ID.fullmatch(idx):
            raise ValueError(f"LIDL-Nodes: Couldn't match Regex: Invalid ID format: {idx}")
        
        # 2. Split
        parts = idx.split("_")
        
        # Expected structure of parts:
        # [date, film, shot, step, version]
        if len(parts) != 5:
            raise ValueError(f"LIDL-Nodes: Malformed ID (split failed): {idx}")
        
        date_str, old_film, old_shot, old_step, old_version = parts
        
        # --- DATE ---
        if update_date:
            date_str = datetime.now().strftime("%Y%m%d")
        
        # --- FILM ---
        if film != "KEEP":
            old_film = film
        
        # --- SHOT ---
        if shot_no != -1:
            old_shot = f"{shot_no:03d}"
        
        # --- PIPELINE STEP ---
        if pipeline_step != "KEEP":
            if pipeline_step == "f":
                if frame_no == -1:
                    raise ValueError("LIDL-Nodes: pipeline_step 'f' requires a valid frame_no")
                old_step = f"f{frame_no}"
            else:
                old_step = pipeline_step
        
        # --- VERSION ---
        if version != -1:
            old_version = f"v{version}"
        
        # 3. Rebuild
        out = f"{date_str}_{old_film}_{old_shot}_{old_step}_{old_version}"
        
        return (out,)



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

    

    def extract(self, text: str):
        match = REGEX_ID.search(text)
        if not match:
            return ("NO_VALID_ID_FOUND",)

        return (match.group(0),)