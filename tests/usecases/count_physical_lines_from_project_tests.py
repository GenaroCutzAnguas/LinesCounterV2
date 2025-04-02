from unittest import TestCase
import os

from src.usecases.count_physical_lines_from_project import (
    count_physical_lines_from_project,
)


class CountPhysicalLinesFromProjectTests(TestCase):
    def test_that_a_directory_without_python_files_should_return_zero(self):
        project_physical_lines_count = count_physical_lines_from_project(
            "tests/assets/empty_dir"
        )

        self.assertEqual(project_physical_lines_count[0], 0)

    def test_that_a_project_with_only_comments_should_return_zero(self):
        project_physical_lines_count = count_physical_lines_from_project(
            "tests/assets/empty_python_project"
        )

        self.assertEqual(project_physical_lines_count[0], 0)

    def test_that_a_project_with_only_code_should_count_the_physical_lines_per_file(
        self,
    ):
        files_physical_lines_count = count_physical_lines_from_project(
            "tests/assets/only_code_python_project"
        )

        file_names = {
            os.path.basename(file_path): line_count
            for file_path, line_count in files_physical_lines_count[1].items()
        }

        self.assertEqual(file_names["fruit.py"], 9)
        self.assertEqual(file_names["fruit_repository.py"], 12)
        self.assertEqual(file_names["in_memory_fruit_repository.py"], 23)

    def test_that_a_project_with_code_and_comments_should_count_the_physical_lines_per_file(
        self,
    ):
        files_physical_lines_count = count_physical_lines_from_project(
            "tests/assets/documented_python_project"
        )

        file_names = {
            os.path.basename(file_path): line_count
            for file_path, line_count in files_physical_lines_count[1].items()
        }

        self.assertEqual(file_names["fruit.py"], 9)
        self.assertEqual(file_names["fruit_repository.py"], 12)
        self.assertEqual(file_names["in_memory_fruit_repository.py"], 23)

    def test_that_a_project_with_only_code_should_count_the_physical_lines(self):
        project_physical_lines_count = count_physical_lines_from_project(
            "tests/assets/only_code_python_project"
        )

        self.assertEqual(project_physical_lines_count[0], 44)

    def test_that_a_project_with_code_and_comments_should_count_the_physical_lines(
        self,
    ):
        project_physical_lines_count = count_physical_lines_from_project(
            "tests/assets/documented_python_project"
        )

        self.assertEqual(project_physical_lines_count[0], 44)
