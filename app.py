from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300},
    {'id': 4, 'date': '2023-06-04', 'amount': 50},
    {'id': 5, 'date': '2023-06-05', 'amount': -100}
]

@app.route("/")
def get_transactions():
    total_balance = sum(transaction['amount'] for transaction in transactions)
    return render_template('transactions.html', transactions=transactions, total_balance=total_balance)


@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == "GET":
        return render_template('form.html')
    elif request.method == "POST":
        transaction = {
            'id': len(transactions) + 1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
        }
        transactions.append(transaction)
        return redirect(url_for('get_transactions'))


@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    transaction = next((t for t in transactions if t['id'] == transaction_id), None)
    if transaction is None:
      return "Transaction not found", 404

    if request.method == "GET":
        return render_template('edit.html', transaction=transaction)
    elif request.method == "POST":
        transaction['date'] = request.form['date']
        transaction['amount'] = float(request.form['amount'])
        return redirect(url_for('get_transactions'))

@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    global transactions
    transactions = [t for t in transactions if t['id'] != transaction_id]
    return redirect(url_for('get_transactions'))


@app.route("/search", methods=["GET", "POST"])
def search_transactions():
    if request.method == "POST":
        min_amount = float(request.form['min_amount'])
        max_amount = float(request.form['max_amount'])
        filtered_transactions = [
            t for t in transactions if min_amount <= t['amount'] <= max_amount
        ]
        return render_template('transactions.html', transactions=filtered_transactions)
    return render_template('search.html')



@app.route("/balance")
def total_balance():
    total_balance = sum(transaction['amount'] for transaction in transactions)
    return f"Total Balance: {total_balance}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)