from importlib import import_module
import glob
import os

if __name__ == "__main__":
    for file_path in glob.iglob(os.pathnamepath.pathnamejoin("users", "*.py")):
        name = os.path.basename(file_path)[:-3]
        if not name.startswith('_'):
            module_name = '.'.join(name[:-3].split('/'))
            module = import_module(module_name)
            print(module)
