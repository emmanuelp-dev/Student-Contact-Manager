# Student-Contact-Manager
A beginner-friendly Python application for managing student, parent, and teacher contact information using dictionaries, sets, and input validation.

# Student Contact Manager

## Overview

Student Contact Manager is a beginner-friendly Python application that allows school administrators to store and manage contact information for students, parents, and teachers.

The program uses dictionaries to store contact records and sets to prevent duplicate email addresses and phone numbers. It provides a simple menu-driven interface for managing contacts efficiently.

## Features

* Add new contacts
* Update existing contacts
* Delete contacts
* Search for contacts by unique identifier
* List all contacts
* Prevent duplicate email addresses
* Prevent duplicate phone numbers
* Validate user input

## Data Structure

Each contact is stored in a dictionary using a unique identifier such as a Student ID or email address as the key.

Example:

```python
contacts = {
    "ST001": {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "08012345678",
        "role": "Student"
    }
}
```

## Technologies Used

* Python
* Dictionaries
* Nested Dictionaries
* Sets
* Functions
* Loops and Conditional Statements

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/student-contact-manager.git
```

2. Navigate to the project folder:

```bash
cd student-contact-manager
```

3. Run the program:

```bash
python student_contact_manager.py
```

## Menu Options

* Add Contact
* Update Contact
* Delete Contact
* Search Contact
* List All Contacts
* Exit

## Learning Objectives

This project was developed to practice:

* Python fundamentals
* Data structures
* CRUD operations (Create, Read, Update, Delete)
* Input validation
* Problem-solving with Python

## Future Improvements

* Save contacts to a file
* Load contacts automatically when the program starts
* Search by name, email, or role
* Graphical User Interface (GUI)
* Database integration using SQLite

## Author

Emmanuel Peter

## License

This project is open source and available for learning and educational purposes.
