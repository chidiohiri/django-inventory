# Django Inventory

Django Inventory is a web-based application built using Django that helps organizations efficiently track and manage their stock of items. The system supports functionalities like item registration, stock updates through incoming and outgoing transactions, and historical audit trails. It aims to reduce manual inventory tracking efforts and minimize human error, ensuring real-time visibility of stock levels and usage.

### Getting Started

These instructions will guide you through setting up Django Inventory on your local machine for development and testing purposes. This guide assumes you are working on a Windows environment. Mac and Linux users can adapt the commands accordingly.

### Prerequisites

Below are the dependencies for the project. For quicker installation, please refer to the [requirements.txt](requirements.txt) file.
- [Python](https://www.python.org/downloads/) - The programming language used to build the backend of the application.
- [Django](https://www.djangoproject.com/download/) - The web framework that powers the server-side logic, database models, and URL routing.
- [Visual Studio Code](https://code.visualstudio.com/) -  A lightweight, flexible code editor recommended for writing and managing the project code.
- [Django Widget Tweaks](https://pypi.org/project/django-widget-tweaks/) - A Django template tag library used to customize form fields directly in templates.
- [Django Filter](https://pypi.org/project/django-filter/) - Adds filtering capabilities to Django views, making it easy to implement search and filter functionality.

### Installing

Create and initialize a virtual environment (optional)

    pip install virtualenv
    virtualenv inventory_env
    cd inventory_env
    Scripts\activate

Clone the Repository

    clone https://github.com/chidiohiri/django-inventory.git
    cd django-inventory

Move the project into the virtual environment, then install dependencies. The project dependencies can found in [requirements.txt](requirements.txt)

    pip install -r requirements.txt

Migrate all tables to the Sqlite3 DB

    python manage.py makemigrations
    python manage.py migrate

Create a super user. This account will be used to access the admin dashboard and manage users.

    python manage.py createsuperuser

Run server on your terminal (cmd or powershell). Open your browser and navigate to http://127.0.0.1:8000/ to access the application.

    python manage.py runserver

### Core Features

- Item Management: Easily add, update, and delete items in the inventory. Each item includes essential details like name, quantity, and a customizable restock alert threshold.

- Stock Inflow and Outflow Tracking: Log every instance of stock received or given out. The system automatically updates item quantities and prevents issuing more stock than available.

- Detailed Transaction History: View a complete timeline of all incoming and outgoing transactions for each item. Helps track stock movement and maintain an audit trail for accountability.

- Date Range Filtering:Filter item history by specific start and end dates to focus on relevant transaction periods for reporting or analysis.

- Search Functionality: Quickly find items using a simple, intuitive keyword search across the inventory database.

- User Activity Logging: All actions—adding items, issuing stock, receiving stock—are tied to the logged-in user, providing traceability and improved accountability.

- Pagination Support: Clean and organized views for both item listings and transaction logs, with pagination to enhance readability and performance.

### Deployment

For production deployment, you will need to configure your application with a production-grade database (such as PostgreSQL), static file handling, and secure hosting. You may refer to the official [Django Documentation](https://docs.djangoproject.com/en/5.1/howto/deployment/) on deployment

### Authors

  - **Chidi Ohiri** - *For updates, networking, or feedback, feel free to connect:* -
    [Linkedin](https://www.linkedin.com/in/chidiebere-ohiri/)

### License

This project is licensed under the [MIT LICENSE](LICENSE.md), which permits reuse, modification, and distribution with proper attribution.

### Acknowledgments

  - Guido van Rossum, the creator of Python
  - The Django core team and community for building and maintaining such a robust framework
  - Developers and open-source contributors whose work inspired or supported the development of this project

