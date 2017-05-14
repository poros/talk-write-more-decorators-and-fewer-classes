from importlib import import_module
import glob
import os
import inspect
from statmonster import Log


def collect():
    for file_path in glob.iglob(os.path.join("users", "*.py")):
        module_name = '.'.join(file_path[:-3].split('/'))
        import_module(module_name)

    module = import_module("users.logs")
    for name, obj in inspect.getmembers(module):
        if isinstance(obj, Log):
            yield name, obj


if __name__ == "__main__":
    for name, log in collect():
        print(f"{name}:{log}")
