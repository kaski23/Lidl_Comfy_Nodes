from .loaders import *
from .input_conformer import *
from .string_tools import *
from .async_tools import *
from .api_adaptions import *


NODE_CLASS_MAPPINGS = {
    "StringSplitSelect_LIDL": StringSplitSelect,
    "ExtractID_LIDL": ExtractIDFromString,
    "GenerateID_LIDL": GenerateID,
    "ModifyID_LIDL": ModifyID,
    
    "VideoSizeLengthConformer_LIDL": VideoSizeLengthConformer,
    "WanVaceInputConform_LIDL": WanVaceInputConform,
    
    "LoadVideoWithFilename_LIDL": LoadVideoWithFilename,
    "LoadImageWithFilename_LIDL": LoadImageWithFilename,
    
    "AsyncDelay_LIDL": AsyncDelay,
    
    "NanobananaPro_LIDL": GeminiImage2,
    "NanobananaSettings_LIDL": GeminiSettings,
    
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StringSplitSelect_LIDL": "String Split and Select",
    "ExtractID_LIDL": "Extract ID",
    "GenerateID_LIDL": "Generate ID",
    "ModifyID_LIDL": "Modify ID",
    
    "VideoSizeLengthConformer_LIDL": "Conform Video Size and Length",
    "WanVaceInputConform_LIDL": "Conform Video for Wan 2.1",
    
    "LoadVideoWithFilename_LIDL": "Load Video with Filename",
    "LoadImageWithFilename_LIDL": "Load Image with Filename",
    
    "AsyncDelay_LIDL": "Async Delay",
    
    "NanobananaPro_LIDL": "Nanobanana Pro IO-unlocked",
    "NanobananaSettings_LIDL": "Nanobanana Settings",
}