class LinesCountReport:
    project_name: str
    project_physical_lines_count: int
    files_physical_lines_count: dict
    files_methods_count: dict

    def __init__(
        self, project_name: str, project_physical_lines_count: int, 
        files_physical_lines_count: dict, files_methods_count: dict
    ):
        self.project_name = project_name
        self.project_physical_lines_count = project_physical_lines_count
        self.files_physical_lines_count = files_physical_lines_count
        self.files_methods_count = files_methods_count
        

    def __str__(self):
        return (
            f"Project: {self.project_name}\n"
            f"Class List:\n{self._file_metrics_count_to_string()}\n"
            f"Total Physical lines: {self.project_physical_lines_count}\n"
        )
    

    def _process_file_metrics_count(self)-> dict:
        file_metrics_count = {}

        for file_path in self.files_physical_lines_count:
            file_metrics_count[file_path] = [self.files_methods_count[file_path], self.files_physical_lines_count[file_path]]

        return file_metrics_count
    

    def _file_metrics_count_to_string(self)-> str:    
        resultado = []
        for file_name, (methods, physical_lines) in self._process_file_metrics_count().items():
            resultado.append(f"File Name: {file_name}")
            for class_name, (method_count) in methods.items():
                #For structured programming files
                if (class_name == "No classes found"):
                    resultado.append(f"Number of functions: {method_count}")
                else:
                    resultado.append(f"Class: {class_name}")
                    resultado.append(f"\tNumber of methods: {method_count}")

            resultado.append(f"Physical lines: {physical_lines}")
            resultado.append("-" * 20)  
        return "\n".join(resultado)  