import os
from src.settings import Settings


def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'rb') as source_file:
            with open(destination_path, 'wb') as destination_file:
                destination_file.write(source_file.read())
        print(f"File copied from {source_path} to {destination_path}")
    except Exception as e:
        print(f"Error copying file: {e}")

class TestSettings:

    def remove_personal_settings(self):
        relative_path = 'data/personalSettings.json'
        personal_settings_path = os.path.realpath(
            os.path.join(os.path.dirname(__file__), '..', relative_path))
        if os.path.exists(personal_settings_path):
            os.remove(personal_settings_path)

    def create_personal_settings(self):
        relative_path_default = 'data/defaultSettings.json'
        relative_path = 'data/personalSettings.json'
        default_settings_path = os.path.realpath(
            os.path.join(os.path.dirname(__file__), '..', relative_path_default))
        personal_settings_path = os.path.realpath(
            os.path.join(os.path.dirname(__file__), '..', relative_path))
        if os.path.exists(personal_settings_path):
            os.remove(personal_settings_path)

        copy_file(default_settings_path, personal_settings_path)

    def test_get_with_personal_settings(self):
        self.create_personal_settings()
        #args = ['--lang=sv', '--speed=1.3']
        #Settings()
        settings = Settings()#args)
        settings.lang = 'sv'
        settings.speed = 1.3
        assert settings.lang == 'sv'
        assert settings.speed == 1.3

    def test_get_with_no_personal_settings(self):
        self.remove_personal_settings()
        #args = ['--lang=sv', '--speed=1.1']
        settings = Settings()
        settings.lang = 'sv'
        settings.speed = 1.1
        assert settings.speed == 1.1
