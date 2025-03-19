from ..helpers.get_all_python_file_paths_from_directory import (
    get_all_python_file_paths_from_directory,
)
from ..helpers.get_lines_with_visible_content_from_file import (
    get_lines_with_visible_content_from_file,
)
from ..helpers.remove_all_comments_from_content_lines import (
    remove_all_comments_from_content_lines,
)


def count_physical_lines_from_project(project_path: str) -> tuple[int, dict]:
    python_file_paths_in_project = get_all_python_file_paths_from_directory(
        project_path
    )

    project_physical_lines_count = 0
    files_physical_lines_count = {}

    for file_path in python_file_paths_in_project:
        files_physical_lines_count[file_path] = _count_physical_lines_from_file(file_path)
        project_physical_lines_count += files_physical_lines_count[file_path]
        

    return project_physical_lines_count, files_physical_lines_count

def _count_physical_lines_from_file(file_path: str) -> int:
        
        lines_with_visible_content = get_lines_with_visible_content_from_file(file_path)
        lines_without_comments = remove_all_comments_from_content_lines(
            lines_with_visible_content
        )

        physical_lines_count_in_file = len(lines_without_comments)

        
        return physical_lines_count_in_file
