# Suppose we have a NotificationService class that is responsible for sending
# notifications. The NotificationService class directly depends on the EmailSender class
# to send emails.
# In this implementation, the NotificationService class directly depends on the
# EmailSender class, which violates the Dependency Inversion Principle. The high-level
# NotificationService should not depend on the low-level EmailSender, as it tightly
# couples the classes together.
# Redesign this program to follow the Dependency Inversion Principle (DIP) principle
# which represents that “Abstractions should not depend upon details. Details
# should depend upon abstractions.”



from abc import ABC, abstractmethod

class EmailSender:
    def send_email(self, recipient, subject, message):
        # Code to send an email2
        print(f"Sending email to {recipient}: {subject} - {message}")


class NotificationService:
    def __init__(self, email_source):
        self.email_source = email_source  # Depends on abstraction, not implementation class

    def send_notification(self, recipient, message):
        self.email_source.get_email(recipient, message)


class EmailSource(ABC):
    @abstractmethod
    def get_email(self, recipient, message):
        pass


class EmailSourceImplementation(EmailSource):  # Concrete implementation of EmailSource
    def __init__(self):
        self.email_sender = EmailSender()

    def get_email(self, recipient, message):
        self.email_sender.send_email(recipient, "Notification", message)


if __name__ == "__main__":
    # Using the NotificationService to send a notification
    email_source = EmailSourceImplementation()
    notification_service = NotificationService(email_source)
    notification_service.send_notification("user@example.com", "Hello, this is a notification!")
