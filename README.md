# Flask Transaction Management Application

This project is a Flask-based web application designed to manage a list of financial transactions. It provides a basic interface for creating, reading, updating, and deleting transactions (CRUD operations). Additionally, it includes search functionality and displays the total balance.

## Features

*   **View Transactions:** Displays all transactions in a table format with the Date, Amount and Actions for each transaction.
*   **Add Transaction:** Allows users to add new transactions through a form.
*   **Edit Transaction:** Allows users to modify existing transaction details using a form.
*   **Delete Transaction:** Allows users to remove transactions.
*   **Search Transactions:** Provides a search functionality to find transactions within a specified amount range.
*   **Total Balance:** Displays the total balance of all transactions.

## Project Structure

The project is organized as follows:
Use code with caution.
Markdown
obmnl-flask_assignment/
├── app.py # Main Flask application logic
├── templates/
│ ├── transactions.html # HTML template to display transactions
│ ├── form.html # HTML template for adding transactions
│ ├── edit.html # HTML template for editing transactions
│ └── search.html # HTML template for searching transactions
└── README.md # Project documentation

*   **`app.py`**: This file contains the Flask application setup, route definitions, and the main logic for handling transactions.
*   **`templates/`**: This directory contains the HTML templates for rendering the web pages.
    *   `transactions.html`: Displays all transactions in a table format, along with actions to edit and delete, as well as a button to add a new transaction. Also displays the total balance.
    *   `form.html`: Provides a form for adding new transaction details.
    *   `edit.html`: Provides a form for editing existing transaction details.
    *  `search.html`: Provides a form for searching transactions within an amount range.
*   **`README.md`**: This file contains the project documentation.

## How to Run

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/JayJay247in/Flask_Web-app.git
    ```

2.  **Navigate to the project directory:**

    ```bash
    cd Flask_Web-app
    ```

3.  **Install Flask:**

    ```bash
    pip install flask
    ```

4.  **Run the Flask application:**

    ```bash
    python app.py
    ```

    The application will start on `http://0.0.0.0:5000/`. You can access it from your browser using `http://localhost:5000/`.

## Usage

### Viewing Transactions

*   Navigate to `http://localhost:5000/` in your web browser.
*   A table with all transactions will be displayed.

### Adding Transactions

*   Click the "Add Transaction" button on the main transactions page or go to `http://localhost:5000/add`.
*   Enter the transaction `Date` and `Amount` into the form.
*   Click the "Add Transaction" button.
*   You will be redirected to the list of transactions.

### Editing Transactions

*   Click the "Edit" button next to the transaction you want to modify from the main transactions page.
*   Edit the transaction `Date` and `Amount` details in the form.
*   Click the "Update Transaction" button.
*   You will be redirected to the list of transactions.

### Deleting Transactions

*   Click the "Delete" button next to the transaction you want to remove.
*   You will be redirected to the list of transactions.

### Searching Transactions

*   Click the "Search Transactions" button on the main transactions page or go to `http://localhost:5000/search`.
*   Enter the desired minimum and maximum amount.
*   Click the "Search" button.
*   Only transactions within the specified amount range will be displayed.

### Total Balance

*   The total balance of all transactions is displayed at the bottom of the transactions table on the main page `http://localhost:5000`.
*   You can also get a string of the balance by going to `http://localhost:5000/balance`

## Code Explanation

### `app.py`

*   The Flask app is instantiated with `app = Flask(__name__)`.
*   Sample data of transactions is stored as a list of dictionaries.
*   Routes are defined for `/`, `/add`, `/edit/<int:transaction_id>`, `/delete/<int:transaction_id>`, `/search` and `/balance`.
*   Each route handles HTTP requests to display web pages or perform actions, such as adding, updating or deleting transactions.
*   The `render_template()` function is used to display the HTML files while passing variables that can be used by Jinja within the html files.
* The `url_for()` function is used to get a url from a given method using its decorator
* The `redirect()` function is used to direct the user to a different route based on an action.

### HTML Templates

*   Each template in the `templates/` folder is responsible for rendering a specific page.
*   `transactions.html` is used to list all transactions and is reused to display searched transactions as well. It displays the total balance at the bottom of the table.
*   `form.html` is used to create new transactions with date and amount fields.
*    `edit.html` is used to edit a particular transaction with date and amount fields prepopulated with existing data.
*   `search.html` provides the form to input the minimum and maximum amount.
* Bootstrap CSS is used to style all HTML files to produce consistent and appealing styling.

## Additional Information

*   This application uses Flask's built-in development server.
*   Debug mode is enabled to show detailed error messages in the browser for development.
*   The application is built to learn basic Flask concepts and CRUD functionality.

## License

This project is open-source and available for educational purposes. Feel free to modify and distribute it as you wish.