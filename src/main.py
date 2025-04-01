from .models.lines_count_report import LinesCountReport

from .usecases.count_physical_lines_from_project import (
    count_physical_lines_from_project,
)
from .usecases.count_methods_from_project import(
    count_methods_from_project,
)


def main():
    project_name = input("Please enter the project name: ")

    project_path = input("Please enter the project path: ")

    try:
        project_physical_lines_count, files_physical_lines_count = count_physical_lines_from_project(project_path)
        project_methods_count_list = count_methods_from_project(project_path)

        print(
            LinesCountReport(
                project_name, project_physical_lines_count, 
                files_physical_lines_count, project_methods_count_list
            )
        )
    except Exception as error:
        print(
            f"Oh no! An error occurred while getting the line count. Verify that the project path is correct and you have read permissions to the directory: {error}"
        )


if __name__ == "__main__":
    main()
