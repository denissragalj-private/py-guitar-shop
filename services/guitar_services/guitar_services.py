from core.guitars.guitars import Guitar


class GuitarService:
    def __init__(self):
        self.guitars = []
        # prop to initialize database connection or any storage mechanism
        # repository = DatabaseRepository()

    def create_guitar(self, guitar: Guitar):
        self.guitars.append(guitar)
        # Save to database or any storage mechanism
        return guitar

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