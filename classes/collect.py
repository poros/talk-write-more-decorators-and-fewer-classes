from importlib import import_module
import glob
import os
import inspect
from statmonster import Log, Trigger


DEFAULT_DIR = "users"


def collect():
    all_triggers = {}
    for module_name, module in get_triggers_modules():
        log, triggers = get_log_and_triggers(module_name, module)
        if log:
            all_triggers[log] = triggers
    return all_triggers


def get_log_and_triggers(module_name, module):
    log = None
    triggers = []
    for name, cls in inspect.getmembers(module, inspect.isclass):
        if is_valid_log(module_name, cls):
            assert not log, "Multiple logs in the same module: %s" % module
            log = cls()
        elif is_valid_trigger(module_name, cls):
            triggers.append(cls())
    return log, set(triggers)


def is_valid_log(module_name, log):
    return (issubclass(log, Log) and
            log.__module__ == f"{DEFAULT_DIR}.{module_name}")


def is_valid_trigger(module_name, trigger):
    return (issubclass(trigger, Trigger) and
            trigger.__module__ == "%s.%s" % (DEFAULT_DIR, module_name))


def get_triggers_modules(triggers_folder=DEFAULT_DIR):
    for file_path in glob.iglob(os.path.join(triggers_folder, "*.py")):
        name = os.path.basename(file_path)[:-3]
        # Filter eg. _service and __init__
        if not name.startswith('_'):
            yield name, dynamic_import_module(file_path)


def dynamic_import_module(module_path):
    module_name = '.'.join(module_path[:-3].split('/'))
    return import_module(module_name)


if __name__ == "__main__":
    for log, triggers in collect().items():
        print(f"{log}:{triggers}")
