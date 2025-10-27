from core import Guitar


ibanez = Guitar(name="Ibanez RG", guitar_type=None, number_of_strings=6)

if not ibanez.is_deleted:
    print(ibanez)
    print(ibanez.created_at)
    print(ibanez.updated_at)
