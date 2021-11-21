from flask import Flask, request
from utils import open_txt, amount_users, read_mean_hw_csv, amount_astros_now

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello"


@app.route("/requirements/")
def requirements():
    filename = "requirements.txt"
    return open_txt(filename)


@app.route("/generate-users/")
def generate_users():
    amount = request.args.get("amount", "100")
    if amount.isdigit():
        amount = int(amount)
        max_amount = 500
        if amount > max_amount:
            return f"amount users shouldn't be anymore {max_amount}"
    else:
        return f'Invalid amount "{amount}"'
    return amount_users(amount)


@app.route("/mean/")
def mean():
    return read_mean_hw_csv()


@app.route("/space/")
def space():
    return amount_astros_now()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
