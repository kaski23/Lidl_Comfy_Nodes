from .loaders import *
from .input_conformers import *
from .string_tools import *


NODE_CLASS_MAPPINGS = {
    "StringSplitSelect_LIDL": StringSplitSelect,
    "ExtractIDFromString_LIDL": ExtractIDFromString,
    "VideoSizeLengthConformer_LIDL": VideoSizeLengthConformer,
    "WanVaceInputConform_LIDL": WanVaceInputConform,
    "LoadVideoWithFilename_LIDL": LoadVideoWithFilename,
    "LoadImageWithFilename_LIDL": LoadImageWithFilename,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StringSplitSelect_LIDL": "String Split and Select",
    "ExtractIDFromString_LIDL": "Extract File ID from String",
    "VideoSizeLengthConformer_LIDL": "Conform Video Size and Length",
    "WanVaceInputConform_LIDL": "Conform Video for Wan 2.1",
    "LoadVideoWithFilename_LIDL": "Load Video with Filename",
    "LoadImageWithFilename_LIDL": "Load Image with Filename",
}