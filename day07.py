from typing import Optional, List


class Directory:
    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.child_dirs: List[Directory] = []
        self.files_in_dir: List[File] = []
        self.parent_dir: Optional[Directory] = None

    def find_child(self, name):
        for child in self.child_dirs:
            if child.dir_name == name:
                return child
        return None

    def get_size(self):
        size = 0
        for file in self.files_in_dir:
            size += file.size
        for child in self.child_dirs:
            size += child.get_size()
        return size

    def get_all_dirs(self, dir_list: List):
        child_dir: Directory
        for child_dir in self.child_dirs:
            dir_list.append(child_dir)
            child_dir.get_all_dirs(dir_list)


class File:
    def __init__(self, file_name, size):
        self.file_name = file_name
        self.size = size


def init_filesystem(terminal_output):
    line: str
    current_dir: Optional[Directory] = None
    for line in terminal_output:
        if line.startswith("$ cd"):
            _, _, dir_name = line.split()
            if current_dir:
                if dir_name == "..":
                    current_dir = current_dir.parent_dir
                else:
                    current_dir = current_dir.find_child(dir_name)
            else:
                current_dir = Directory(dir_name)
            continue
        if line.startswith("$ ls"):
            continue
        if line.startswith("dir"):
            _, dir_name = line.split()
            child_dir = Directory(dir_name)
            child_dir.parent_dir = current_dir
            current_dir.child_dirs.append(child_dir)
            continue
        # we have a plain file
        size, file_name = line.split()
        current_dir.files_in_dir.append(File(file_name, int(size)))

    at_root_dir = False
    while not at_root_dir:
        if not current_dir.parent_dir:
            at_root_dir = True
        else:
            current_dir = current_dir.parent_dir
    return current_dir


def get_sum_of_small_dirs(terminal_output):
    root_dir: Directory = init_filesystem(terminal_output)
    list_of_dirs: List[Directory] = []
    root_dir.get_all_dirs(list_of_dirs)
    sum_of_small_dirs: int = 0
    for directory in list_of_dirs:
        if directory.get_size() < 100000:
            sum_of_small_dirs += directory.get_size()
    return sum_of_small_dirs


def delete_directory(terminal_output) -> int:
    space_available = 70000000
    unused_needed = 30000000
    root_dir: Directory = init_filesystem(terminal_output)
    used_space: int = root_dir.get_size()
    unused_space: int = space_available - used_space
    need_to_free: int = unused_needed - unused_space
    list_of_dirs: List[Directory] = []
    root_dir.get_all_dirs(list_of_dirs)
    dict_of_dirs = {}
    a_dir: Directory
    for a_dir in list_of_dirs:
        dict_of_dirs[a_dir.dir_name] = a_dir.get_size()
    sorted_dict = dict(sorted(dict_of_dirs.items(), key=lambda x: x[1]))
    for dir_name in sorted_dict:
        if sorted_dict[dir_name] > need_to_free:
            return sorted_dict[dir_name]
