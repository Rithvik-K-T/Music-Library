import os

# folder path
dir_path = r'G:\\sft\\Music-Library\\Music\\'




res = []
cmd=input()
if (cmd=='<program> --input <path to music folder> --list-files'):

    for path in os.listdir(dir_path):
        
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    print(res)

