# Shopping Receipt Management System (Python CLI)

## Overview
This project is a simple command-line application built using Python that simulates a shopping receipt system. It allows users to manage transaction data in a structured way using basic CRUD operations (Create, Read, Update, Delete).

The goal of this project is to demonstrate how a small-scale software system can be designed with clear logic, user interaction, and data handling, even without using a full database.

---

## Features
- Add new items to the receipt
- View all stored items
- Search items by ID
- Update item details (type, name, quantity, price)
- Delete items from the system
- Input validation to prevent invalid data

---

## How It Works
The program runs through a command-line interface (CLI), where users interact with a menu system. Each menu option directs the user to a specific function, such as adding or editing data.

The system continuously runs until the user chooses to exit, making it easy to perform multiple operations in one session.

---

## System Architecture
The system is designed using a simple layered approach:

- **Presentation Layer**  
  Handles user interaction through the CLI menu and input prompts.

- **Application Logic Layer**  
  Contains the core functionality, including CRUD operations and input validation.

- **Data Layer**  
  Uses an in-memory data structure (a list of dictionaries) to store all transaction data.

This separation makes the program easier to understand and maintain.

---

## Technologies Used
- Python
- Colorama (for colored CLI output)

---

## Example Data Structure
Each item is stored as a dictionary:

```python
{
  "id": "A001",
  "tipe": "Saniteri",
  "barang": "Sabun Batang",
  "jumlah": 12,
  "harga": 10000
}
