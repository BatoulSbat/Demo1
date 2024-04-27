class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True

# Initialise an empty list to store email objects
inbox = []

def populate_inbox():
    # Sample emails
    email1 = Email("sender1@example.com", "Welcome to HyperionDev!", "Dear student, welcome to HyperionDev!")
    email2 = Email("sender2@example.com", "Great work on the BootCamp!", "Keep up the excellent work!")
    email3 = Email("sender3@example.com", "Your excellent marks!", "Congratulations on your outstanding performance!")

    # Add sample emails to the inbox
    inbox.append(email1)
    inbox.append(email2)
    inbox.append(email3)

def list_emails():
    print("Inbox:")
    for index, email in enumerate(inbox):
        print(f"{index}: {email.subject_line}")

def read_email(index):
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"\nEmail from {email.email_address} - Subject: {email.subject_line}\n")
        print(email.email_content)
        email.mark_as_read()
        print("\nEmail marked as read.")
    else:
        print("Invalid email index.")

def main():
    # Populate inbox with sample emails
    populate_inbox()

    while True:
        print("\nMenu:")
        print("1. Read an email")
        print("2. View unread emails")
        print("3. Quit application")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_emails()
            index = int(input("Enter the index of the email you want to read: "))
            read_email(index)
        elif choice == '2':
            print("\nUnread emails:")
            for email in inbox:
                if not email.has_been_read:
                    print(email.subject_line)
        elif choice == '3':
            print("Quitting application...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True

# Initialise an empty list to store email objects
inbox = []

def populate_inbox():
    # Sample emails
    email1 = Email("sender1@example.com", "Welcome to HyperionDev!", "Dear student, welcome to HyperionDev!")
    email2 = Email("sender2@example.com", "Great work on the BootCamp!", "Keep up the excellent work!")
    email3 = Email("sender3@example.com", "Your excellent marks!", "Congratulations on your outstanding performance!")

    # Add sample emails to the inbox
    inbox.append(email1)
    inbox.append(email2)
    inbox.append(email3)

def list_emails():
    print("Inbox:")
    for index, email in enumerate(inbox):
        print(f"{index}: {email.subject_line}")

def read_email(index):
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"\nEmail from {email.email_address} - Subject: {email.subject_line}\n")
        print(email.email_content)
        email.mark_as_read()
        print("\nEmail marked as read.")
    else:
        print("Invalid email index.")

def main():
    # Populate inbox with sample emails
    populate_inbox()

    while True:
        print("\nMenu:")
        print("1. Read an email")
        print("2. View unread emails")
        print("3. Quit application")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_emails()
            index = int(input("Enter the index of the email you want to read: "))
            read_email(index)
        elif choice == '2':
            print("\nUnread emails:")
            for email in inbox:
                if not email.has_been_read:
                    print(email.subject_line)
        elif choice == '3':
            print("Quitting application...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
