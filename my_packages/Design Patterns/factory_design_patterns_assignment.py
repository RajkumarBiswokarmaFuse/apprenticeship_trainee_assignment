"""
    This program demonstrates the use of Factory Design Patterns.

"""
# pylint: disable=unspecified-encoding
from abc import ABC, abstractmethod

# Logger interface


class Logger(ABC):
    """This is a Logger Class."""
    @abstractmethod
    def write_log(self, message):
        """This is a function which writes log."""


# LoggerFactory class
class LoggerFactory:
    """This is a LoggerFactory class."""
    @staticmethod
    def get_logger(logger_type):
        """This is a get_logger function which gets
        a logger type when object created."""
        if logger_type == 'file':
            return FileLogger()
        elif logger_type == 'console':
            return ConsoleLogger()
        elif logger_type == 'database':
            return DatabaseLogger()
        else:
            raise ValueError(f"Invalid logger type: {logger_type}")

# File Logger


class FileLogger(Logger):
    """This is a FileLogger Class."""

    def write_log(self, message):
        with open('./data/log_builder.txt', 'a') as file:
            file.write(f"{message}\n")

# Console Logger


class ConsoleLogger(Logger):
    """This is a ConsoleLogger."""

    def write_log(self, message):
        print(f"Console: {message}")

# Database Logger


class DatabaseLogger(Logger):
    """This is a DatabaseLogger Class."""

    def write_log(self, message):
        # Implement code to write logs to the database here
        print(f"Database: {message}")


def main():
    """This is a main function."""
    logger_type = input("Enter logger type (file/console/database): ").lower()

    try:
        logger = LoggerFactory.get_logger(logger_type)
        logger.write_log("Application started.")
        logger.write_log("Something happened in the application.")
        logger.write_log("Error occurred in the application.")
    except ValueError as value_error:
        print(value_error)


if __name__ == "__main__":
    main()
