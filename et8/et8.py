''' Find all files in directory (including subdirectories). '''

import os

def find_all_files_in_directory(directory_path : str) -> list[str]:
    ''' Recursively scans subdirectories. '''
    result : list[str] = []
    if os.path.isdir(directory_path):
        for item in os.listdir(directory_path):
            path_to_item : str = os.path.join(directory_path, item)
            if os.path.isfile(path_to_item):
                result.append(item)
                continue
            result.extend(find_all_files_in_directory(path_to_item))
    return result
