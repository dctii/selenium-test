import os


def get_file_path(file):
    return os.path.abspath(file)


def get_curr_dir(file):
    return os.path.dirname(os.path.abspath(file))


def get_root_dir(file):
    return os.path.dirname(os.path.dirname(os.path.abspath(file)))
