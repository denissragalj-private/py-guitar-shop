from config import AppConfig
from core.guitars.guitars import Guitar
from infrastructure.guitar_repos.guitar_repo import GuitarRepo


class GuitarService:
    def __init__(self, app_config: AppConfig):
        self.guitars = []
        self.app_config = app_config
        # prop to initialize database connection or any storage mechanism
        self.repo = GuitarRepo(app_config.repo_type)

    def create_guitar(self, guitar: Guitar):
        # Nakon sto se doda u bazu, objekt dobije ID pa se vrati
        # kako bi se nastavio koristiti u aplikaciji
        return self.repo.save_guitar(guitar)

    def get_guitar(self, guitar_id: int, is_deleted: bool = False):
        for guitar in self.guitars:
            if guitar.id == guitar_id and guitar.is_deleted == is_deleted:
                return guitar
        return None

    def get_all_guitars(self, is_deleted: bool = False):
        return [guitar for guitar in self.guitars if guitar.is_deleted == is_deleted]

    def update_guitar(self, guitar_id: int, is_deleted: bool = False):
        for guitar in self.guitars:
            if guitar.id == guitar_id:
                guitar.is_deleted = is_deleted
                # Save changes to database or any storage mechanism
                return guitar
        return None

    def delete_guitar(self, guitar_id: int):
        # Get the guitar and mark it as deleted
        guitar = self.get_guitar(guitar_id)
        if guitar:
            guitar.is_deleted = True
            # Save changes to database or any storage mechanism
            return guitar
        return None