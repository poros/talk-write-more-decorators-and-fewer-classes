from importlib import import_module
import glob
import os

if __name__ == "__main__":
    for file_path in glob.iglob(os.path.join("users", "*.py")):
        module_name = '.'.join(file_path[:-3].split('/'))
        module = import_module(module_name)
        print(module)
