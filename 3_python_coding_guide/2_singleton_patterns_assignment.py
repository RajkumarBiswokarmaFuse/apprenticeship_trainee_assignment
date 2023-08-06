# Implement a configuration manager using the Singleton
# Design Pattern. The configuration manager should read configuration settings from a
# file and provide access to these settings throughout the application. Demonstrate howthe Singleton Design Pattern ensures that there is only one instance of the
# configuration manager, preventing unnecessary multiple reads of the configuration file.


class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def init(self, config_file):
        if not self._initialized:
            self._config = {}
            self._load_config(config_file)
            self._initialized = True

    def _load_config(self, config_file):
        try:
            with open(config_file, 'r') as file:
                for line in file:
                    key, value = line.strip().split('=')
                    self._config[key.strip()] = value.strip()
        except IOError:
            print(f"Error reading configuration file: {config_file}")

    def get_setting(self, key):
        return self._config.get(key)

    def set_setting(self, key, value):
        self._config[key] = value


if __name__ == "__main__":
    config_file = "config.txt"

    # Create a configuration manager instance (Singleton)
    config_manager1 = ConfigurationManager()
    config_manager1.init(config_file)

    # Try to create another instance (should return the same instance)
    config_manager2 = ConfigurationManager()
    config_manager2.init(config_file)

    # Check if both instances are the same
    print(f"config_manager1 is config_manager2: {config_manager1 is config_manager2}")

    # Access configuration settings
    setting1 = config_manager1.get_setting("setting1")
    setting2 = config_manager2.get_setting("setting2")

    print(f"Setting 1: {setting1}")
    print(f"Setting 2: {setting2}")

    # Modify a configuration setting
    config_manager1.set_setting("setting1", "Hello World!")
    setting1_new = config_manager1.get_setting("setting1")

    # Verify that the setting has been updated in both instances
    print(f"Setting 1 (after update): {setting1_new}")
    print(f"Setting 2 (unchanged): {setting2}")
