


class AppConfig:
    def __init__(self, debug: bool, database_url: str, repo_type: str):
        self.debug = debug
        self.database_url = database_url
        self.repo_type = repo_type
