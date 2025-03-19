from re import match
from ..helpers.get_all_python_file_paths_from_directory import (
    get_all_python_file_paths_from_directory,
)
from ..helpers.get_lines_with_visible_content_from_file import (
    get_lines_with_visible_content_from_file,
)
from ..helpers.remove_all_comments_from_content_lines import (
    remove_all_comments_from_content_lines,
)


def count_methods_from_project(project_path: str) -> dict:
    python_file_paths_in_project = get_all_python_file_paths_from_directory(
        project_path
    )

    methods_list = {}

    for file_path in python_file_paths_in_project:
        methods_list[file_path] = _count_methods_from_file(file_path)

    return methods_list


def _count_methods_from_file(file_path: str) -> dict:
    lines_with_visible_content = get_lines_with_visible_content_from_file(file_path)

    lines_without_comments = remove_all_comments_from_content_lines(
        lines_with_visible_content
    )

    class_methods_count = _extract_methods_and_classes(lines_without_comments)

    #if there is no class in the file this will be empty
    if not class_methods_count:
  
        total_methods = _count_methods(lines_without_comments)
        return {"No classes found": total_methods}

    return class_methods_count


def _extract_methods_and_classes(content_lines: list[str]) -> dict:
    class_methods = {}
    current_class = None
    method_count = 0

    for content_line in content_lines:
        class_name = _extract_class_name(content_line)
        
        if class_name:  
            if current_class:
                class_methods[current_class] = method_count
            
            current_class = class_name
            method_count = 0  

        elif current_class and _is_method(content_line):
            method_count += 1
        
        elif not current_class and _is_method(content_line):
            method_count += 1
    

    if current_class:
        class_methods[current_class] = method_count

    return class_methods


def _extract_class_name(line: str) -> str:
 
    class_pattern = r"^\s*class\s+(\w+)"
    
    is_class = match(class_pattern, line)
    
    if is_class:
        return is_class.group(1)
    
    return None  


def _is_method(line: str) -> bool:
    
    method_pattern = r"^\s*def\s+\w+"  

    if match(method_pattern, line):
        return True
    
    return False


def _count_methods(content_lines: list[str]) -> int:
    method_count = 0
    for line in content_lines:
        if _is_method(line):
            method_count += 1
    return method_count