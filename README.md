# Lidl_Comfy_Nodes
Some helpers for our Lidl-ComfyUI-Workflows


Installation: 
- Install git from https://git-scm.com/install/
- Open a terminal in //ComfyUI/custom_nodes by typing cmd into the folder bar
- Copy into terminal: "git clone https://github.com/kaski23/Lidl_Comfy_Nodes.git" without the "" and press enter

Updating:
- open a terminal in //ComfyUI/custom_nodes/Lidl_Comfy_Nodes/
- Copy into terminal: "git pull origin main" without the "" and press enter


Nodes:
Load Image with Filename -> Loads Image with Filename
Load Video with Filename -> Loads Video with Filename
String Split and select -> Splits a string at the determinator (standart: _) and outputs the element at the index (eg. string: hello_you, determinator: _ , index: 1 -> output: you)
Generate ID -> Generates a valid File ID string that matches our project.
Extract ID -> Extracts a valid File ID string from a string
Modify ID -> Modifies ID if not set to "KEEP" or -1 for the integers. Needs to get a valid ID for our project
