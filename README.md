# Website Blocker

## Description
The Website Blocker is a Python-based application that allows users to block and unblock websites using the system's host file. It provides a simple GUI built with Tkinter to facilitate easy management of blocked websites.

## Features
- Block multiple websites by entering them in the input field.
- Unblock previously blocked websites.
- Uses the system's host file to prevent access to specified websites.
- Cross-platform support (Windows, Linux, macOS).
- User-friendly graphical interface.

## Technologies Used
- Python
- Tkinter (GUI)
- Platform (OS detection)
- OS module (File handling)
- MessageBox (User notifications)

## Installation
### Prerequisites
Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/AkshatNeolia/WebsiteBlocker.git
   cd WebsiteBlocker
   ```
2. Run the script:
   ```sh
   python website_blocker.py
   ```

## Usage
1. Enter the websites to be blocked in the input field (space-separated).
2. Click the **Block Websites** button to restrict access.
3. Click the **Unblock Websites** button to remove restrictions.

## Screenshot
![Screenshot 2025-02-10 130440](https://github.com/user-attachments/assets/966067e5-4bdc-4f6f-98c3-8db66373cea8)

## Important Notes
- **Admin Privileges Required**: Modifying the host file requires administrator/root access.
- **Backup Recommended**: Before making changes, consider backing up your host file.
