import os
from src.Settings import Settings


class TestSettings:

    def remove_personal_settings(self):
        relative_path = 'src/personalSettings.json'
        personal_settings_path = os.path.realpath(
            os.path.join(os.path.dirname(__file__), '..', relative_path))
        os.remove(personal_settings_path)

    def test_get_with_personal_settings(self):
        args = ['--lang=sv', '--speed=1.3']
        Settings()
        settings = Settings(args)
        assert settings.speed == 1.3

    def test_get_with_no_personal_settings(self):
        self.remove_personal_settings()
        args = ['--lang=sv', '--speed=1.1']
        settings = Settings(args)
        assert settings.speed == 1.1
