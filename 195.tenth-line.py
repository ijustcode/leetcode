from pathlib import Path
class FileHandler:
    def readLines(self, file_path_string: str, target) -> str:
        file = Path(file_path_string)
        with file.open() as f:
            all_lines = f.readlines()
        return all_lines[target]






if __name__ == "__main__":
        

    my_file_handler = FileHandler()
    file_path = "./some_text_file.txt"
    print(my_file_handler.readLines(file_path, 0))