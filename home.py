import os

# folder path
dir_path = r'G:\\sft\\Music-Library\\Music\\'



# list to store files
res = []
cmd=input()
if (cmd=='<program> --input <path to music folder> --list-files'):
# Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    print(res)

