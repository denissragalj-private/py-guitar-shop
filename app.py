import json

from core import (Guitar,
                  GuitarType,
                  Amplifier,
                  AmpType,
                  GuitarString,
                  StringType)
from services import GuitarService
from config import AppConfig
from constants import REPO_TYPE_FILE, CONFIG_FILE_PATH


def load_config(file_path: str) -> AppConfig:
    try:
        with open(file_path, 'r') as file_reader:
            config_data = dict(json.load(file_reader))

        return AppConfig(
            debug=config_data.get('debug', False),
            database_url=config_data.get('database_url', ''),
            repo_type=config_data.get('repo_type', REPO_TYPE_FILE)
        )

    except FileNotFoundError:
        print(f"Configuration file not found: {file_path}")
        return None

    except json.JSONDecodeError:
        print(f"Error decoding JSON from config file: {file_path}")
        return None

    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
        return None


def main():
    # ucitavanje konfiguracije iz fajla
    app_config = load_config(CONFIG_FILE_PATH)
    if app_config is None:
        print("Failed to load application configuration. Exiting.")
        return

    guitar_service = GuitarService(app_config)

    electric_guitar = GuitarType(name="Electric")
    ibanez = Guitar(name="Ibanez RG",
                    guitar_type=electric_guitar,
                    number_of_strings=6)
    ibanez = guitar_service.create_guitar(ibanez)

    fender = Guitar(name="Fender Stratocaster",
                    guitar_type=electric_guitar,
                    number_of_strings=6)
    fender = guitar_service.create_guitar(fender)

if __name__ == "__main__":
    main()
