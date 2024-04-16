# Hotel Management System

## Project Overview
This Hotel Management System is designed to facilitate the management of hotel operations through an interactive Python application interfaced with a MySQL database. It allows users to handle various hotel management tasks including customer check-ins, billing for services like restaurant meals, laundry, and gaming, and searching and managing customer information. 

## Features
- **Customer Management**: Add and search for customers in the hotel database.
- **Billing System**: Calculate and update bills for different services such as accommodation, restaurant meals, laundry, and gaming.
- **Room Management**: Manage room assignments and calculate room rent based on room type and duration of stay.
- **Financial Reporting**: Generate total bills for customers, facilitating easy checkout processes.

## What's Needed to Execute:
- **Python**: The main programming language used.
- **MySQL**: Used for database management to store all customer and transaction data.
- **MySQL Connector Python**: A library used to connect the Python application to the MySQL database.

## Installation

### Prerequisites
- Python 3.8 or higher
- MySQL Server
- MySQL Connector Python

You can install MySQL Connector Python via pip:
```bash
pip install mysql-connector-python
```
## Usage
Run the program using Python from the command line:
```bash
python hotel_management_system.py
```

Follow the on-screen prompts to navigate through the menu options:

1. Enter Customer Details
2. Calculate Restaurant Bill
3. Calculate Laundry Bill
4. Calculate Game Bill
5. Search Customer
6. Generate Total Bill
7. Exit

## Contributing
Contributions are welcome! Please feel free to submit pull requests, create issues for bugs and feature requests, and provide feedback on improvements.
