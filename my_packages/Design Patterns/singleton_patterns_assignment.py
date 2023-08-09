"""
Implement a configuration manager using the Singleton
Design Pattern. The configuration manager should read configuration settings from a
file and provide access to these settings throughout the application. Demonstrate how
the Singleton Design Pattern ensures that there is only one instance of the
configuration manager, preventing unnecessary multiple reads of the configuration file.
"""
# pylint: disable=unspecified-encoding
class ConfigurationManager:
    """
    Singleton class for managing configuration settings.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._initialized = False
        if not self._initialized:
            self._config = {}
            self._initialized = True

    def init(self, config_file):
        """
        Initialize the configuration manager with settings from the specified file.

        Args:
            config_file (str): The path to the configuration file.
        """
        if not self._initialized:
            self._load_config(config_file)

    def _load_config(self, config_file):
        """
        Load configuration settings from the specified file.

        Args:
            config_file (str): The path to the configuration file.
        """
        try:
            with open(config_file, 'r') as file:
                for line in file:
                    key, value = line.strip().split('=')
                    self._config[key.strip()] = value.strip()
        except IOError:
            print(f"Error reading configuration file: {config_file}")

    def get_setting(self, key):
        """
        Get a configuration setting by its key.

        Args:
            key (str): The key of the setting.

        Returns:
            str: The value of the setting, or None if not found.
        """
        return self._config.get(key)

    def set_setting(self, key, value):
        """
        Set or update a configuration setting.

        Args:
            key (str): The key of the setting.
            value (str): The new value for the setting.
        """
        self._config[key] = value


if __name__ == "__main__":
    CONFIG_FILE_PATH = "config.txt"

    # Create a configuration manager instance (Singleton)
    config_manager1 = ConfigurationManager()
    config_manager1.init(CONFIG_FILE_PATH)

    # Try to create another instance (should return the same instance)
    config_manager2 = ConfigurationManager()
    config_manager2.init(CONFIG_FILE_PATH)

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
