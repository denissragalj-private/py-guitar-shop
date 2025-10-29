import json

from core.guitars.guitars import Guitar


class GuitarRepo:
    def __init__(self, repo_type: str):
        self._repo_type = repo_type
        self._file_path = ''
        self._db_connection_string = ''
        self._configure(repo_type)

    def _configure(self, repo_type: str):
        if repo_type == 'file':
            self._file_path = 'data/files/guitars.json'
        elif repo_type == 'db':
            self._db_connection_string = 'database_connection_string'

    def save_guitar(self, guitar: Guitar) -> Guitar:
        if self._repo_type == 'file':
            # dodati gitaru u listu i onda cijelu listu snimiti u datoteku
            guitars = self._read_guitars_from_file()
            guitars.append(guitar.to_dict())
            with open(self._file_path, 'w') as file_writer:
                json.dump(guitars, file_writer, indent=4)
            return guitar
        elif self._repo_type == 'db':
            # Implement database save logic here
            pass

    def get_all_guitars(self) -> Guitar:
        guitars = []
        if self._repo_type == 'file':
            with open(self._file_path, 'r') as f:
                for line in f:
                    guitars.append(Guitar.from_json(line))
        elif self._repo_type == 'db':
            # Implement database retrieval logic here
            pass
        return guitars

    def _read_guitars_from_file(self):
        try:
            with open(self._file_path, 'r') as file_reader:
                guitars_data = json.load(file_reader)
                if len(guitars_data) == 0:
                    return []
                elif len(guitars_data) == 1:
                    return [guitars_data]
                return guitars_data
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
        except Exception as ex:
            print(f"An unexpected error occurred while reading guitars: {ex}")
            return []
