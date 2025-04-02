from unittest import TestCase

from src.usecases.count_methods_from_project import (
    count_methods_from_project,
    _extract_methods_and_classes,
)


class ExtractMethodsAndClasses(TestCase):
    def test_that_empty_lines_should_return_empty_list_of_physical_lines(self):
        file_class_methods = _extract_methods_and_classes([])
        self.assertEqual(file_class_methods, {})

    def test_that_a_string_with_a_single_class_without_methods_return_zero(self):
        content_of_file = ["class MyClass:"]
        file_class_methods = _extract_methods_and_classes(content_of_file)
        self.assertEqual(file_class_methods, {"MyClass": 0})

    def test_that_a_string_with_a_single_class_return_correct_method_count(self):
        content_of_file = [
            "class MyClass:",
            "    def method1(self):",
            "        pass",
            "    def method2(self):",
            "        pass",
        ]
        file_class_methods = _extract_methods_and_classes(content_of_file)
        self.assertEqual(file_class_methods, {"MyClass": 2})

    def test_that_a_string_with_multiple_classes_return_correct_method_count(self):
        content_of_file = [
            "class ClassA:",
            "    def method1(self):",
            "        pass",
            "",
            "class ClassB:",
            "    def method2(self):",
            "        pass",
            "    def method3(self):",
            "        pass",
        ]
        file_class_methods = _extract_methods_and_classes(content_of_file)
        self.assertEqual(file_class_methods, {"ClassA": 1, "ClassB": 2})


class CountMethodsFromProyectTests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.project_path = "tests/assets/only_code_python_project"
        cls.methods_data = count_methods_from_project(cls.project_path)

    def test_that_in_a_project_with_code_it_detect_all_the_classes(self):
        self.assertEqual(len(self.methods_data), 7)

        found_classes = set()
        for file_data in self.methods_data.values():
            found_classes.update(file_data.keys())

        self.assertIn("Fruit", found_classes)
        self.assertIn("FruitRepository", found_classes)
        self.assertIn("InMemoryFruitRepository", found_classes)

    def test_the_method_count_from_fruit_class(self):
        for file_data in self.methods_data.values():
            if "Fruit" in file_data:
                self.assertEqual(file_data["Fruit"], 1)
                break
        else:
            self.fail("Fruit class not founded")

    def test_the_method_count_from_fruit_repository(self):
        for file_data in self.methods_data.values():
            if "FruitRepository" in file_data:
                self.assertEqual(file_data["FruitRepository"], 5)
                break
        else:
            self.fail("FruitRepository class not founded")

    def test_the_method_count_from_in_memory_repository(self):
        for file_data in self.methods_data.values():
            if "InMemoryFruitRepository" in file_data:
                self.assertEqual(file_data["InMemoryFruitRepository"], 6)
                break
        else:
            self.fail("InMemoryFruitRepository class not founded")

    def test_that_a_file_with_no_classes_should_return_no_classes_found(self):
        project_method_count = count_methods_from_project("tests/assets/empty_python_project")

        for file_data in project_method_count.values():
            self.assertIn("No classes found", file_data)
            self.assertEqual(file_data["No classes found"], 0)
