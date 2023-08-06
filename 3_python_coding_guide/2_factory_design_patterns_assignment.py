# Build a logging system using the Factory Design Pattern.
# Create a LoggerFactory class that generates different types of loggers (e.g., FileLogger,
# ConsoleLogger, DatabaseLogger). Implement methods in each logger to write logs to
# their respective destinations. Show how the Factory Design Pattern helps to decouple
# the logging system from the application and allows for flexible log handling.\

from abc import ABC, abstractmethod

# Logger interface
class Logger(ABC):
    @abstractmethod
    def write_log(self, message):
        pass

# LoggerFactory class
class LoggerFactory:
    @staticmethod
    def get_logger(logger_type):
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
    def write_log(self, message):
        with open('./data/log_builder.txt', 'a') as file:
            file.write(f"{message}\n")


# Console Logger
class ConsoleLogger(Logger):
    def write_log(self, message):
        print(f"Console: {message}")


# Database Logger
class DatabaseLogger(Logger):
    def write_log(self, message):
        # Implement code to write logs to the database here
        print(f"Database: {message}")

if __name__ == "__main__":
    logger_type = input("Enter logger type (file/console/database): ").lower()

    logger = LoggerFactory.get_logger(logger_type)

    logger.write_log("Application started.")
    logger.write_log("Something happened in the application.")
    logger.write_log("Error occurred in the application.")
