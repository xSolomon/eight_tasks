''' Find all files in directory (including subdirectories). '''

import os

def find_all_files(directory_path : str, directory_content : list[str],
    current_item_index : int, result : list[str]) -> list[str]:
    ''' If we meet a directory, we browse it's content too. '''
    if current_item_index >= len(directory_content):
        return result
    if os.path.isdir(os.path.join(directory_path, directory_content[current_item_index])):
        subdirectory_path : str = os.path.join(directory_path,
            directory_content[current_item_index])
        find_all_files(subdirectory_path, os.listdir(subdirectory_path), 0, result)
    if os.path.isfile(os.path.join(directory_path, directory_content[current_item_index])):
        result.append(directory_content[current_item_index])
    return find_all_files(directory_path, directory_content, current_item_index + 1, result)

def find_all_files_in_directory(directory_path : str) -> list[str]:
    ''' Recursively scans subdirectories. '''
    if os.path.isdir(directory_path):
        return find_all_files(directory_path, os.listdir(directory_path), 0, [])
