from core import (Guitar,
                  GuitarType,
                  Amplifier,
                  AmpType,
                  GuitarString,
                  StringType)
from services import GuitarService


guitar_service = GuitarService()


electric_guitar = GuitarType(name="Electric")
ibanez = Guitar(name="Ibanez RG",
                guitar_type=electric_guitar,
                number_of_strings=6)
guitar_service.create_guitar(ibanez)
guitar_from_db = guitar_service.get_guitar(5)

if not ibanez.is_deleted:
    print(ibanez)
    print(ibanez.created_at)
    print(ibanez.updated_at)
    print(ibanez.guitar_type.name)


amp_type = AmpType(name="Tube")
fender_amp = Amplifier(name="Fender Twin Reverb",
                       amp_type=amp_type,
                       power=60)
if not fender_amp.is_deleted:
    print(fender_amp)
    print(fender_amp.created_at)
    print(fender_amp.updated_at)
    print(fender_amp.amp_type.name)


string_type = StringType(name="Electric Guitar Strings")
guitar_string = GuitarString(name="Ernie Ball Regular Slinky",
                             gauge=0.010,
                             type=string_type)
if not guitar_string.is_deleted:
    print(guitar_string)
    print(guitar_string.created_at)
    print(guitar_string.updated_at)
    print(guitar_string.type.name)
